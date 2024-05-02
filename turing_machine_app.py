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
import random
from collections import deque
import math
import pygame
import pygame_gui
from utils import load_transitions_from_csv
from turing_machine import TuringMachine

# Initialize Pygame
pygame.init()


# Screen dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
STATE_COLOR = (100, 0, 0)  # Green
TEXT_COLOR = (255, 255, 255)  # White
LINES_COLOR = (0, 0, 255)  # Blue
TAPE_COLOR = (200, 200, 200)
FONT_PATH = pygame.font.match_font('Monaco')
ARROW = "\u2192"
BLANK = "\u23B5"
ARROW_length = 10
FONT_SIZE = 11
MARGIN_X = 200
MARGIN_Y = 100
SPACING_X = 120
SPACING_Y = 120


font = pygame.font.Font(FONT_PATH, FONT_SIZE)
# Define a function to load transitions from a CSV file

from particlesystem import ParticleSystem

class TuringMachineApp:
    def __init__(self, tm):
        self.particle_system = ParticleSystem()
        self.tm = tm
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Turing Machine Simulator")
        self.clock = pygame.time.Clock()
        self.tape = self.tm.tape
        self.running = True
        self.manager = pygame_gui.UIManager(
            (SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a UIManager
        self.textinput = pygame_gui.elements.UITextEntryLine(pygame.Rect(
            (10, 10), (200, 50)), self.manager)  # Pass the UIManager as the second argument
        self.textinput.set_text_length_limit(20)
        self.reset_button = pygame_gui.elements.UIButton(
            pygame.Rect((10, 70), (100, 50)), 'Reset', self.manager)
        self.load_button = pygame_gui.elements.UIButton(
            pygame.Rect((10, 130), (100, 50)), 'Load', self.manager)
        self.states_list = list(self.tm.states)  # Convert the set to a list
        self.positions = {state: (random.uniform(0, SCREEN_WIDTH), random.uniform(
            0, SCREEN_HEIGHT)) for state in self.states_list}
        self.init_positions()

    def init_positions(self):
        self.start_state = 'q1'
        # Initialize positions
        self.positions = {}

        # Breadth-first search to layout states in layers
        visited = {state: False for state in self.states_list}
        print(visited)
        # Start with the start state at layer 0
        queue = deque([(self.start_state, 0)])
        layer_nodes = {}  # Keep track of nodes at each layer

        while queue:
            state, layer = queue.popleft()
            print(state, layer)
            if not visited[state]:
                visited[state] = True
                x = MARGIN_X + layer * SPACING_X
                # Position based on the number of nodes in this layer
                y = MARGIN_Y + len(layer_nodes.get(layer, [])) * SPACING_Y
                self.positions[state] = (x, y)
                layer_nodes.setdefault(layer, []).append(
                    state)  # Add state to nodes in this layer
                # Iterate over the values of the inner dictionary
                for next_state in self.tm.transitions[state].values():
                    print(next_state)
                    # next_state[0] is the next state
                    queue.append((next_state[0], layer + 1))

        print(self.positions)

    def reset(self):
        self.textinput.set_text('')
        self.running = True
        self.tm.current_state = 'q1'
        self.tm.head = 0

    def load(self):
        # open file dialog
        dialog = pygame_gui.windows.UIFileDialog(pygame.Rect(
            (100, 100), (400, 400)), self.manager, window_title="Open File")
        dialog.set_blocking(True)



    def draw_tape(self):
        cell_width = 40
        cell_height = 40
        start_x = (SCREEN_WIDTH - len(self.tape) * cell_width) // 2
        start_y = SCREEN_HEIGHT - 100

        for i, symbol in enumerate(self.tm.tape):
            rect = pygame.Rect(start_x + i * cell_width,
                               start_y, cell_width, cell_height)
            pygame.draw.rect(self.screen, TAPE_COLOR, rect, 2)
            symbol_text = font.render(symbol, True, TEXT_COLOR)
            text_rect = symbol_text.get_rect(center=rect.center)
            self.screen.blit(symbol_text, text_rect)

        # Draw the head
        head_rect = pygame.Rect(start_x + self.head *
                                cell_width, start_y, cell_width, cell_height)
        pygame.draw.rect(self.screen, STATE_COLOR, head_rect, 4)

    def generate_graph(self):
        # Create an image for the graph
        self.graph = pygame.Surface(
            (self.screen.get_width(), self.screen.get_height()))
        drawn = {}
        # Draw transitions
        for state, transitions in self.tm.transitions.items():
            for symbol, (next_state, write_symbol, move_direction) in transitions.items():
                if state == next_state:
                    if state in drawn:
                        x, y = drawn[state]

                        text_surface = font.render(
                            f"{symbol}{ARROW}{write_symbol},{move_direction}", True, TEXT_COLOR)
                        text_surface.set_alpha(200)
                        text_surface.set_colorkey((0, 255, 0))
                        self.graph.blit(text_surface, (x, y - 20))
                    else:
                        # draw a loop
                        x, y = self.positions[state]

                        # draw an arc going out from the circle and coming back
                        # the bounding rectangle of the arc
                        rect = pygame.Rect(x, y - 30, 30, 30)
                        start_angle = math.pi / 2  # start at the top
                        stop_angle = 2.5 * math.pi  # stop at the top, after a full loop
                        pygame.draw.arc(self.graph, color=TEXT_COLOR, rect=rect,
                                        start_angle=start_angle, stop_angle=stop_angle, width=2)

                        # render the transition text
                        text_surface = font.render(
                            f"{symbol}{ARROW}{write_symbol},{move_direction}", True, TEXT_COLOR)
                        text_surface.set_alpha(200)
                        text_surface.set_colorkey((0, 255, 0))
                        x = x + 10
                        y = y - 50
                        # adjust the position of the text surface to avoid printing inside the circle
                        self.graph.blit(text_surface, (x, y))
                        drawn[state] = (x, y)
                    continue
                start_x, start_y = self.positions[state]
                end_x, end_y = self.positions[next_state]
                # add radius to the x position of the start state to make the line start from the edge of the circle
                start_x = start_x + 20
                # make the line shorter so that it doesn't overlap with the state circle
                end_x = end_x - 20

                # make it shorter so that it doesn't overlap with the state circle

                pygame.draw.line(self.graph, LINES_COLOR,
                                 (start_x, start_y), (end_x, end_y), 1)

                # Calculate the angle of the line
                dx = end_x - start_x
                dy = end_y - start_y
                angle = math.atan2(dy, dx)

                # Calculate the points for the ARROW
                ARROW_dx = ARROW_length * math.cos(angle)
                ARROW_dy = ARROW_length * math.sin(angle)

                ARROW_point1 = (end_x - ARROW_dx + ARROW_dy / 2,
                                end_y - ARROW_dy - ARROW_dx / 2)
                ARROW_point2 = (end_x - ARROW_dx - ARROW_dy / 2,
                                end_y - ARROW_dy + ARROW_dx / 2)

                # Draw the ARROW
                pygame.draw.polygon(self.graph, LINES_COLOR, [
                                    (end_x, end_y), ARROW_point1, ARROW_point2])

                text_surface = font.render(
                    f"{symbol}{ARROW}{write_symbol},{move_direction}", True, TEXT_COLOR)
                text_surface.set_alpha(200)
                text_surface.set_colorkey((0, 255, 0))
                self.graph.blit(
                    text_surface, ((start_x + end_x) / 2, (start_y + end_y) / 2))

        # Draw states
        for state in self.states_list:
            x, y = self.positions[state]
            pygame.draw.circle(self.graph, color=STATE_COLOR,
                               center=(x, y), radius=20)
            text_surface = font.render(state, True, TEXT_COLOR)
            text_surface.set_alpha(200)
            text_surface.set_colorkey((0, 255, 0))
            text_center = text_surface.get_rect(center=(x, y))
            self.graph.blit(text_surface, text_center)

        # Blit the graph onto the current screen
        self.screen.blit(self.graph, (0, 0))

    def run(self):
        while self.running:
            self.head = self.tm.head
            time_delta = self.clock.tick(FPS)/1000.0
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                        print(event.text)
                        transitions = load_transitions_from_csv(event.text)
                        states = set(transitions.keys())
                        self.states_list = list(states)
                        self.tm = TuringMachine(states, self.tm.input_symbols,
                                                self.tm.tape_symbols, transitions)
                        print (self.tm.transitions)
                        self.states_list = list(states)
                        self.init_positions()
                        print(self.states_list)
                        print(self.positions)
                        self.reset()
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        result_stat, _ = self.tm.step()
                        finished = result_stat in ['q_accept', 'q_reject']
                        if finished:
                            window = pygame_gui.windows.UIMessageWindow(
                                rect=pygame.Rect((100, 100), (400, 200)),
                                manager=self.manager,
                                window_title="Result",
                                html_message=f"<font size=4>{result}</font>")
                    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                        self.reset()
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.textinput:
                            self.tape = list(self.textinput.get_text(
                            )) + self.tape[len(self.textinput.get_text()):]
                            self.tm.set_input(self.textinput.get_text())
                    elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.reset_button:
                            self.reset()
                            self.init_positions()
                        elif event.ui_element == self.load_button:
                            self.load()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for state, pos in self.positions.items():
                        # If the mouse is over a state
                        if math.hypot(x - pos[0], y - pos[1]) < 40:
                            print(f"Clicked on state {state}")

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.screen.fill(BACKGROUND_COLOR)  # Uncomment this line
            self.generate_graph()
            self.screen.blit(self.graph, (0, 0))
            self.draw_tape()
            self.manager.draw_ui(self.screen)
            self.particle_system.add_particle(400, 300, 10, (255, 255, 255))
            self.particle_system.update(self.screen)
            

            pygame.display.flip()

        pygame.quit()
        sys.exit()
