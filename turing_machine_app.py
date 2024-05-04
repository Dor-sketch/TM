"""
This module contains the TuringMachineApp class that is responsible for running
the Turing Machine simulator.
The TuringMachineApp class is responsible for creating the graphical user interface
for the Turing Machine simulator.
It uses the Pygame library to create the GUI elements and to handle user input.
The TuringMachineApp class has methods
- reset: to reset the Turing Machine to its initial state
- load: to load transitions from a CSV file
- draw_tape: to draw the tape on the screen
- generate_graph: to generate the state transition graph
- run: to run the Turing Machine simulator
"""

import sys
import math
import pygame
import pygame_gui
from utils import load_transitions_from_csv
from particlesystem import ParticleSystem
from turing_machine import TuringMachine
from turing_machine_graph import TuringGraph
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    HEAD_WIDTH,
    INITIAL_STATE,
    TAPE_WIDTH,
    STATE_COLOR,
    TEXT_COLOR,
    font,
    BACKGROUND_COLOR,
    TAPE_COLOR,
    FPS,
)


class TuringMachineApp:
    def __init__(self, tm):
        self.tm = tm
        self.running = True
        self.particle_system = ParticleSystem()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Turing Machine Simulator")
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )  # Create a UIManager
        self.textinput = pygame_gui.elements.UITextEntryLine(
            pygame.Rect((10, 10), (200, 50)), self.manager
        )  # Pass the UIManager as the second argument
        self.textinput.set_text_length_limit(20)
        self.reset_button = pygame_gui.elements.UIButton(
            pygame.Rect((10, 70), (100, 50)), "Reset", self.manager
        )
        self.load_button = pygame_gui.elements.UIButton(
            pygame.Rect((10, 130), (100, 50)), "Load", self.manager
        )
        self.tm_graph = TuringGraph(self.tm.states, self.tm.transitions)

    def reset(self):
        self.textinput.set_text("")
        self.running = True
        self.tm.current_state = INITIAL_STATE
        self.tm.head = 0

    def load(self):
        # open file dialog
        dialog = pygame_gui.windows.UIFileDialog(
            pygame.Rect((100, 100), (400, 400)), self.manager, window_title="Open File"
        )
        dialog.set_blocking(True)

    def draw_tape(self):
        cell_width = 40
        cell_height = 40
        start_x = (SCREEN_WIDTH - len(self.tm.tape) * cell_width) // 2
        start_y = SCREEN_HEIGHT - 100

        for i, symbol in enumerate(self.tm.tape):
            rect = pygame.Rect(
                start_x + i * cell_width, start_y, cell_width, cell_height
            )
            pygame.draw.rect(self.screen, TAPE_COLOR, rect, TAPE_WIDTH)
            symbol_text = font.render(symbol, True, TEXT_COLOR)
            text_rect = symbol_text.get_rect(center=rect.center)
            self.screen.blit(symbol_text, text_rect)

        # Draw the head
        head_rect = pygame.Rect(
            start_x + self.tm.head * cell_width, start_y, cell_width, cell_height
        )
        pygame.draw.rect(self.screen, STATE_COLOR, head_rect, HEAD_WIDTH)

    def process_event(self, event):
        if event.type == pygame.USEREVENT:
            self.process_user_event(event)
        elif event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            self.process_keydown_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.process_mouse_event(event)

        self.manager.process_events(event)

    def process_user_event(self, event):
        if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
            self.load_transitions(event.text)
        elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.textinput:
                self.tm.set_input(self.textinput.get_text())
        elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.process_button_press(event)

    def load_transitions(self, text):
        print(text)
        try:
            transitions = load_transitions_from_csv(text)
        except Exception as e:
            print(e)
            return
        states = set(transitions.keys())
        self.tm = TuringMachine(
            states, self.tm.input_symbols, self.tm.tape_symbols, transitions
        )
        print(self.tm.transitions)
        self.reset()

    def process_keydown_event(self, event):
        if event.key in [pygame.K_DOWN, pygame.K_RIGHT]:
            self.step_tm()
        elif event.key in [pygame.K_UP, pygame.K_LEFT]:
            self.reset()

    def step_tm(self):
        result_stat, _ = self.tm.step()
        finished = result_stat in ["q_accept", "q_reject"]
        if finished:
            window = pygame_gui.windows.UIMessageWindow(
                rect=pygame.Rect((100, 100), (400, 200)),
                manager=self.manager,
                window_title="Result",
                html_message=f"<font size=4>{result}</font>",
            )

    def process_button_press(self, event):
        if event.ui_element == self.reset_button:
            self.reset()
            self.init_positions()
        elif event.ui_element == self.load_button:
            self.load()

    def process_mouse_event(self, event):
        x, y = pygame.mouse.get_pos()
        try:
            for state, pos in self.tm_graph.positions.items():
                # If the mouse is over a state
                if math.hypot(x - pos[0], y - pos[1]) < 40:
                    print(f"Clicked on state {state}")
        except AttributeError:
            pass
        except Exception as e:
            print(e)

    def run(self):
        while self.running:
            time_delta = self.clock.tick(FPS) / 1000.0
            events = pygame.event.get()
            for event in events:
                self.process_event(event)

            self.manager.update(time_delta)

            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.tm_graph.graph, (0, 0))
            self.draw_tape()
            self.manager.draw_ui(self.screen)
            self.particle_system.add_particle(400, 300, 10, (255, 255, 255))
            self.particle_system.update(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
