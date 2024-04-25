import math
import pygame
import sys
import csv
import pygame_gui
import random
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
# Fonts
FONT_SIZE = 20
font = pygame.font.Font(None, FONT_SIZE)

# Define a function to load transitions from a CSV file


def load_transitions_from_csv(filename):
    transitions = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            current_state, input_symbol, new_state, new_symbol, move = row
            if current_state not in transitions:
                transitions[current_state] = {}
            transitions[current_state][input_symbol] = (
                new_state, new_symbol, move)
    return transitions

# Turing Machine class


class TuringMachine:
    def __init__(self, states, input_symbols, tape_symbols, transitions, start_state, accept_states, reject_states):
        self.states = states
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions
        self.start_state = 'q_start'
        self.current_state = self.start_state
        self.accept_states = accept_states
        self.reject_states = reject_states
        self.accept_states.add('q_accept')
        self.reject_states.add('q_reject')
        self.head = 0

    def get_transition(self, tape_symbol):
        return self.transitions[self.current_state].get(tape_symbol, None)

    def step(self, tape, head):
        head = self.head
        # print(self.current_state, tape, head)
        if self.current_state in self.accept_states:
            return True, 'Accepted'
        if self.current_state in self.reject_states:
            return True, 'Rejected'
        if head < 0 or head >= len(tape):
            return True, 'Error: Head out of bounds'

        tape_symbol = tape[head]
        # print head above the tape
        print(' '.join(tape), end=' ')
        print(f'| state: {self.current_state}')
        print('  ' * head + '^')

        transition = self.get_transition(tape_symbol)
        if not transition:
            return True, 'Rejected: No transition found'

        new_state, new_tape_symbol, move = transition
        tape[head] = new_tape_symbol
        self.current_state = new_state
        if move == 'R':
            head += 1
        elif move == 'L':
            head -= 1
        self.head = head
        return False, (tape, head)


class TuringMachineApp:
    def __init__(self, tm):
        self.tm = tm
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Turing Machine Simulator")
        self.clock = pygame.time.Clock()
        self.tape = ['_'] * 20  # Initialize tape with blanks
        # Initialize head in the middle of the tape
        self.head = len(self.tape) // 2
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
        # Initialize positions
        self.positions = {state: (random.uniform(0, SCREEN_WIDTH), random.uniform(
            0, SCREEN_HEIGHT)) for state in self.states_list}

        # Define margins
        MARGIN_X = 100  # Adjust as needed
        MARGIN_Y = 100  # Adjust as needed

        # Kamada-Kawai algorithm
        iterations = 500  # Adjust as needed
        for _ in range(iterations):
            # Calculate forces
            disp = {state: (0, 0) for state in self.states_list}
            for state1 in self.states_list:
                for state2 in self.states_list:
                    if state1 != state2:
                        dx, dy = self.positions[state1][0] - \
                            self.positions[state2][0], self.positions[state1][1] - \
                            self.positions[state2][1]
                        distance = math.sqrt(dx * dx + dy * dy)
                        if distance < 1:  # Prevent division by zero
                            distance = 1
                        # Change formula for force
                        force = (distance - 1) / distance
                        repulsion_force = 100 / distance**2 if distance < 100 else 0  # Adjust as needed
                        force += repulsion_force
                        disp[state1] = (disp[state1][0] + dx *
                                        force, disp[state1][1] + dy * force)

            # Update positions
            for state in self.states_list:
                dx, dy = disp[state]
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < 1:  # Prevent division by zero
                    distance = 1
                self.positions[state] = (
                    self.positions[state][0] + dx / distance, self.positions[state][1] + dy / distance)
                # make sure the states are within the screen and respect the margins
                self.positions[state] = (min(SCREEN_WIDTH - MARGIN_X, max(MARGIN_X, self.positions[state][0])), min(
                    SCREEN_HEIGHT - MARGIN_Y, max(MARGIN_Y, self.positions[state][1])))

    def reset(self):
        self.tape = ['_'] * 20
        self.head = len(self.tape) // 2
        self.textinput.set_text('')
        self.running = True
        self.tm.current_state = self.tm.start_state

    def load(self):
        # open file dialog
        dialog = pygame_gui.windows.UIFileDialog(pygame.Rect(
            (100, 100), (400, 400)), self.manager, window_title="Open File")
        dialog.set_blocking(True)

    def draw_tape(self):
        cell_width = 40
        cell_height = 40
        font = pygame.font.Font(None, 36)
        start_x = (SCREEN_WIDTH - len(self.tape) * cell_width) // 2
        start_y = SCREEN_HEIGHT // 2

        for i, symbol in enumerate(self.tape):
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
                            f"{symbol}:{write_symbol},{move_direction}", True, TEXT_COLOR)
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
                            f"{symbol}:{write_symbol},{move_direction}", True, TEXT_COLOR)
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
                pygame.draw.line(self.graph, LINES_COLOR,
                                 (start_x, start_y), (end_x, end_y), 1)
                text_surface = font.render(
                    f"{symbol}:{write_symbol},{move_direction}", True, TEXT_COLOR)
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
            self.graph.blit(text_surface, (x, y))

        # Blit the graph onto the current screen
        self.screen.blit(self.graph, (0, 0))

    def run(self):
        while self.running:
            self.head = self.tm.head
            time_delta = self.clock.tick(FPS)/1000.0
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished, result = self.tm.step(self.tape, self.head)
                        if finished:
                            print(result)
                            self.running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.textinput:
                            self.tape = list(self.textinput.get_text(
                            )) + self.tape[len(self.textinput.get_text()):]
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

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    states = {'q_start', 'q1', 'q2', 'q3', 'q4', 'q5', 'q_accept', 'q_reject'}
    input_symbols = {'0', '1'}
    tape_symbols = {'0', '1', '_', 'x', 'y'}
    transitions = load_transitions_from_csv('transitions.csv')
    start_state = 'q0'
    accept_states = {'q7'}
    reject_states = {'q6'}

    tm = TuringMachine(states, input_symbols, tape_symbols,
                       transitions, start_state, accept_states, reject_states)
    app = TuringMachineApp(tm)
    app.run()
