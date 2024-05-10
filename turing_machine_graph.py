"""
A module to draw a graph of a Turing machine
"""

import pygame.gfxdraw
from config import SCREEN_WIDTH, SCREEN_HEIGHT, STATE_COLOR, TEXT_COLOR, LINES_COLOR, font
import math
import random
import pygame
from collections import deque
ARROW = "\u2192"
BLANK = "\u23B5"
ARROW_LENGTH = 10
MARGIN_X = 70
MARGIN_Y = 200
SPACING_X = 120
SPACING_Y = 120


def draw_3d_circle(surface, x, y, radius, color):
    # Draw the circle with a gradient
    for i in range(radius):
        alpha = round(255 * (i / radius))  # calculate alpha for gradient
        pygame.gfxdraw.filled_circle(
            surface, x, y, radius - i, (*color, alpha))

    # Draw the shadow
    shadow_color = (0, 0, 0, 50)  # semi-transparent black for shadow
    pygame.gfxdraw.filled_circle(
        surface, x + radius // 4, y + radius // 4, radius, shadow_color)


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
        drawn = {}
        self.draw_transitions(drawn)
        self.draw_states()

    def draw_transitions(self, drawn):
        for state, transitions in self.transitions.items():
            for symbol, (next_state, write_symbol, move_direction) in transitions.items():
                if state == next_state:
                    self.draw_loop(state, drawn, symbol,
                                   write_symbol, move_direction)
                else:
                    self.draw_line(state, next_state, symbol,
                                   write_symbol, move_direction)

    def draw_loop(self, state, drawn, symbol, write_symbol, move_direction):
        if state in drawn:
            x, y = drawn[state]
            self.blit_text(x, y - 20, symbol, write_symbol, move_direction)
        else:
            x, y = self.positions[state]
            self.draw_arc(x, y)
            self.blit_text(x + 10, y - 50, symbol,
                           write_symbol, move_direction)
            drawn[state] = (x, y)

    def draw_arc(self, x, y):
        rect = pygame.Rect(x, y - 30, 30, 30)
        start_angle = math.pi / 2
        stop_angle = 2.5 * math.pi
        pygame.draw.arc(self.graph, color=TEXT_COLOR, rect=rect,
                        start_angle=start_angle, stop_angle=stop_angle, width=2)

    def draw_line(self, state, next_state, symbol, write_symbol, move_direction):
        start_x, start_y = self.positions[state]
        end_x, end_y = self.positions[next_state]
        start_x += 20
        end_x -= 20
        pygame.draw.line(self.graph, LINES_COLOR,
                         (start_x, start_y), (end_x, end_y), 1)
        self.draw_arrow(start_x, start_y, end_x, end_y)
        self.blit_text((start_x + end_x) / 2, (start_y + end_y) /
                       2, symbol, write_symbol, move_direction)

    def draw_arrow(self, start_x, start_y, end_x, end_y):
        dx = end_x - start_x
        dy = end_y - start_y
        angle = math.atan2(dy, dx)
        ARROW_dx = ARROW_LENGTH * math.cos(angle)
        ARROW_dy = ARROW_LENGTH * math.sin(angle)
        ARROW_point1 = (end_x - ARROW_dx + ARROW_dy / 2,
                        end_y - ARROW_dy - ARROW_dx / 2)
        ARROW_point2 = (end_x - ARROW_dx - ARROW_dy / 2,
                        end_y - ARROW_dy + ARROW_dx / 2)
        pygame.draw.polygon(self.graph, LINES_COLOR, [
                            (end_x, end_y), ARROW_point1, ARROW_point2])

    def blit_text(self, x, y, symbol, write_symbol, move_direction):
        text_surface = font.render(
            f"{symbol}{ARROW}{write_symbol},{move_direction}", True, TEXT_COLOR)
        text_surface.set_alpha(200)
        text_surface.set_colorkey((0, 255, 0))
        self.graph.blit(text_surface, (x, y))

    def draw_states(self):
        for state in self.states_list:
            x, y = self.positions[state]
            draw_3d_circle(self.graph, x, y, 20, STATE_COLOR)
            self.blit_state_text(x, y, state)

    def blit_state_text(self, x, y, state):
        text_surface = font.render(state, True, STATE_COLOR)
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
