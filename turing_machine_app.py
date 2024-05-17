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
import random
import os
import sys
import math
import pygame
import pygame_gui
from miditm import midi_to_tm
from utils import load_transitions_from_csv, get_green_shade, get_blue_shade, get_red_shade
from particlesystem import ParticleSystem
from turing_machine import TuringMachine
from turing_machine_graph import TuringGraph
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    HEAD_WIDTH,
    INITIAL_STATE,
    TAPE_WIDTH,
    font,
    BACKGROUND_COLOR,
    FPS,
)


class TuringMachineApp:
    """
    A class to represent the Turing Machine Simulator application
    """
    def __init__(self, tm, input_ta=None):
        self.tm = tm
        self.running = True
        self.particle_system = ParticleSystem()
        self.keydown_timers = {}
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
            pygame.Rect((330, 10), (100, 50)), "Reset", self.manager
        )
        self.load_button = pygame_gui.elements.UIButton(
            pygame.Rect((220, 10), (100, 50)), "Load", self.manager
        )
        self.tm_graph = TuringGraph(self.tm.states, self.tm.transitions)
        if input_ta is not None:
            self.tm.set_input(input_ta.read())

    def reset(self):
        """
        Reset the Turing Machine to its initial state
        """
        self.textinput.set_text("")
        self.running = True
        self.tm.current_state = INITIAL_STATE
        self.tm.head = 0
        # clear the tape
        self.tm.tape = ["_"] * 20
        # clear the graph
        self.tm_graph = TuringGraph(self.tm.states, self.tm.transitions)

    def load(self):
        """
        Load transitions from a CSV file or a MIDI file
        """
        # open file dialog
        os.chdir('mids')
        dialog = pygame_gui.windows.UIFileDialog(
            pygame.Rect((100, 100), (400, 400)),
            self.manager,
            window_title="Open File",
        )
        dialog.set_blocking(True)
        os.chdir('..')

    def get_tape_subset(self, mode, cells_on_screen):
        """
        Get a subset of the tape to display on the screen
        """
        if mode == "scroll":
            start_index = max(0, self.tm.head)
            end_index = start_index + 20
        elif mode == "scroll_from_half":
            start_index = max(0, self.tm.head - cells_on_screen // 2)
            end_index = start_index + cells_on_screen
        else:
            start_index = (self.tm.head // cells_on_screen) * cells_on_screen
            end_index = start_index + cells_on_screen
        return self.tm.tape[start_index:end_index], start_index

    def draw_cells(self, tape_subset, start_index, start_x, start_y, cell_width, cell_height, tape_color, text_color):
        """
        Draw the cells of the tape on the screen
        """
        for i, symbol in enumerate(tape_subset):
            rect = pygame.Rect(start_x + i * cell_width, start_y, cell_width, cell_height)
            pygame.draw.rect(self.screen, tape_color, rect, TAPE_WIDTH)
            symbol_text = font.render(symbol, True, text_color)
            text_rect = symbol_text.get_rect(center=rect.center)
            self.screen.blit(symbol_text, text_rect)

    def draw_head(self, start_index, start_x, start_y, cell_width, cell_height, state_color):
        """
        Draw the head of the Turing Machine on the tape
        """
        head_rect = pygame.Rect(start_x + (self.tm.head - start_index) * cell_width, start_y, cell_width, cell_height)
        pygame.draw.rect(self.screen, state_color, head_rect, HEAD_WIDTH)

    def draw_tape(self, mode="highlight"):
        """
        Draw the tape on the screen
        """
        cell_height = 40
        start_x = 0
        start_y = SCREEN_HEIGHT - 100
        cells_on_screen = SCREEN_WIDTH // cell_height
        tape_color = self.tm_graph.line_color
        text_color = self.tm_graph.text_color
        state_color = self.tm_graph.circle_color

        tape_subset, start_index = self.get_tape_subset(mode, cells_on_screen)
        cell_width = SCREEN_WIDTH // len(tape_subset)

        self.draw_cells(tape_subset, start_index, start_x, start_y, cell_width, cell_height, tape_color, text_color)
        self.draw_head(start_index, start_x, start_y, cell_width, cell_height, state_color)

    def process_event(self, event):
        """
        Process the events generated by the user
        """
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
        """
        Process the user events generated by the GUI elements
        """
        if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
            self.load_transitions(event.text)
        elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.textinput:
                self.tm.set_input(self.textinput.get_text())
        elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.process_button_press(event)

    def load_midi_transitions(self, text):
        """
        Load transitions from a MIDI file
        """
        self.tm = midi_to_tm(text)
        self.reset()
        try:
            with open("input_string.txt", "r") as input_ta:
                self.tm.set_input(input_ta.read())
        except FileNotFoundError:
            raise FileNotFoundError("input_string.txt not found")

    def load_csv_transitions(self, text):
        """
        Load transitions from a CSV file
        """
        try:
            transitions = load_transitions_from_csv(text)
            states = set(transitions.keys())
            self.tm = TuringMachine(states, self.tm.input_symbols, self.tm.tape_symbols, transitions)
            self.reset()
        except FileNotFoundError:
            raise FileNotFoundError("Transitions file not found")

    def load_transitions(self, text):
        """
        Load transitions from a file
        """
        try:
            if text.endswith('.mid'):
                self.load_midi_transitions(text)
            else:
                self.load_csv_transitions(text)
        except Exception as e:
            print(e)
            return

    def process_keydown_event(self, event):
        """
        Process the keydown events generated by the user
        """
        if event.key in [pygame.K_DOWN, pygame.K_RIGHT]:
            self.step_tm()
        elif event.key in [pygame.K_UP]:
            self.reset()
        elif event.key in [pygame.K_LEFT]:
            self.tm_graph = TuringGraph(self.tm.states, self.tm.transitions)

    def add_particle(self, x, y, color_func):
        """
        Add a particle to the particle system
        """
        color = color_func()
        self.particle_system.add_particle(x, y, 7, color)

    def step_tm(self):
        """
        Step the Turing Machine
        """
        result_stat, _ = self.tm.step()
        finished = result_stat in ["q_accept", "q_reject"]
        if finished:
            self.display_result(result_stat)
        else:
            self.add_particles_for_each_position()

    def display_result(self, result_stat):
        window = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((100, 100), (400, 200)),
            manager=self.manager,
            window_title="Result",
            html_message=f"<font size=4>{result_stat}</font>",
        )

    def add_particles_for_each_position(self):
        positions = self.tm.last_chord
        for pos in positions:
            x, y = self.tm_graph.positions[pos]
            self.add_particles_based_on_state(x, y)

    def add_particles_based_on_state(self, x, y):
        if self.tm.current_state == "q_accept":
            self.add_particle(x, y, get_green_shade)
        elif self.tm.current_state == "q_reject":
            self.add_particle(x, y, get_red_shade)
        else:
            self.add_random_blue_particles(x, y)

    def add_random_blue_particles(self, x, y):
        num = random.randint(1, 20)
        for i in range(num):
            self.add_particle(x, y, get_blue_shade)

    def run(self):
        while self.running:
            self.update_time_delta()
            self.process_events()
            self.draw_screen()
            self.update_particle_system()
            pygame.display.flip()
        self.quit()

    def update_time_delta(self):
        time_delta = self.clock.tick(FPS) / 1000.0
        self.manager.update(time_delta)

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            self.process_event(event)

    def draw_screen(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.tm_graph.graph, (0, 0))
        self.draw_tape()
        self.manager.draw_ui(self.screen)

    def update_particle_system(self):
        self.particle_system.update(self.screen)

    def quit(self):
        pygame.quit()
        sys.exit()

    def process_button_press(self, event):
        if event.ui_element == self.reset_button:
            self.reset()
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


if __name__ == "__main__":
    tm = midi_to_tm("./mids/Memorial.mid")
    input_ta = open("input_string.txt", "r")
    app = TuringMachineApp(tm, input_ta)
    app.run()
