

# Screen dimensions and settings
ARROW = "\u2192"
BLANK = "\u23B5"
ARROW_LENGTH = 10
MARGIN_X = 100
MARGIN_Y = 200
SPACING_X = 120
SPACING_Y = 120
from collections import deque
import pygame
import random
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, STATE_COLOR, TEXT_COLOR, LINES_COLOR, font

class TuringGraph:
    def __init__(self, states, transitions):
        self.graph = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.states_list = list(states)
        self.transitions = transitions
        self.positions = {state: (random.uniform(0, SCREEN_WIDTH), random.uniform(
            0, SCREEN_HEIGHT)) for state in self.states_list}
        self.init_positions()
        self.generate_graph()

    def generate_graph(self):
        # Create an image for the graph

        drawn = {}
        # Draw transitions
        for state, transitions in self.transitions.items():
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
                ARROW_dx = ARROW_LENGTH * math.cos(angle)
                ARROW_dy = ARROW_LENGTH * math.sin(angle)

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

    def init_positions(self):
        self.start_state = 'q1'
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
                for next_state in self.transitions[state].values():
                    print(next_state)
                    # next_state[0] is the next state
                    queue.append((next_state[0], layer + 1))
        print(self.positions)
