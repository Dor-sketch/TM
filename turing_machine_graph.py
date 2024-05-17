"""
A module to draw a graph of a Turing machine
"""

import math
import random
import time
from collections import deque
import pygame
import pygame.gfxdraw
from PIL import Image, ImageDraw
from config import SCREEN_WIDTH, SCREEN_HEIGHT, STATE_COLOR, TEXT_COLOR, LINES_COLOR, font, palettes
ARROW = "\u2192"
BLANK = "\u23B5"
ARROW_LENGTH = 10
MARGIN_X = 0
MARGIN_Y = 500
SPACING_X = 120
SPACING_Y = 120

def draw_3d_circle(surface, x, y, radius, color, text=None, text_color=(255, 255, 255)):
    """
    Draw a 3D circle with a gradient and a shadow
    """
    x, y, radius = int(x), int(y), int(radius)
    # Draw the shadow
    shadow_color = (0, 0, 0, 50)  # semi-transparent black for shadow
    pygame.gfxdraw.filled_circle(
        surface, x + radius // 4, y + radius // 4, radius, shadow_color)
    # Draw the circle with a gradient
    for i in range(radius):
        alpha = round(255 * (i / radius))  # calculate alpha for gradient
        pygame.gfxdraw.filled_circle(
            surface, x, y, radius - i, (*color, alpha))

    # Draw the text after the circle
    if text is not None:
        font = pygame.font.Font(None, 24)  # Choose the font for the text
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)


class TuringGraph:
    def __init__(self, states, transitions):
        self.line_color = LINES_COLOR
        self.circle_color = STATE_COLOR
        self.text_color = TEXT_COLOR
        self.graph = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.states_list = list(states)
        self.transitions = transitions
        self.positions = {state: (random.uniform(0, SCREEN_WIDTH), random.uniform(
            0, SCREEN_HEIGHT)) for state in self.states_list}
        self.init_positions()
        self.generate_graph()


    def set_theme(self):
        """
        Set the theme of the graph
        """
        t = time.time()

        # Use the current time to select a palette and two colors from the palette
        palette_index = int(t / 10) % len(palettes)
        color_index1 = int(t) % len(palettes[palette_index])
        color_index2 = (color_index1 + 1) % len(palettes[palette_index])
        color1 = palettes[palette_index][color_index1]
        color2 = palettes[palette_index][color_index2]

        # Create a new gradient image
        gradient = Image.new('RGB', self.graph.get_size())
        draw = ImageDraw.Draw(gradient)

        # Draw the gradient
        for i in range(self.graph.get_width()):
            r = color1[0] * (1 - i/self.graph.get_width()) + color2[0] * (i/self.graph.get_width())
            g = color1[1] * (1 - i/self.graph.get_width()) + color2[1] * (i/self.graph.get_width())
            b = color1[2] * (1 - i/self.graph.get_width()) + color2[2] * (i/self.graph.get_width())
            draw.line([(i, 0), (i, self.graph.get_height())], fill=(int(r), int(g), int(b)))

        # Convert the PIL Image to a Pygame surface
        gradient_pygame = pygame.image.fromstring(gradient.tobytes(), gradient.size, gradient.mode)

        # Use the gradient image as the background
        self.graph.blit(gradient_pygame, (0, 0))

        # Calculate complementary colors for the lines and circles
        self.line_color = (255 - color2[0], 255 - color2[1], 255 - color2[2])
        self.circle_color = ((255 + color2[0]) // 2, (255 + color2[1]) // 2, (255 + color2[2]) // 2)

    def generate_graph(self):
        """
        Generate the graph of the Turing machine
        """
        self.set_theme()

        drawn = {}
        self.draw_transitions(drawn)
        self.draw_states()

    def draw_transitions(self, drawn):
        """
        Draw the transitions of the Turing machine
        """
        for state, transitions in self.transitions.items():
            for symbol, (next_state, write_symbol, move_direction) in transitions.items():
                if state == next_state:
                    self.draw_loop(state, drawn, symbol,
                                   write_symbol, move_direction)
                else:
                    self.draw_line(state, next_state, symbol,
                                   write_symbol, move_direction)

    def draw_loop(self, state, drawn, symbol, write_symbol, move_direction):
        """
        Draw a loop transition
        """
        if state in drawn:
            x, y = drawn[state]
            self.blit_text(x, y - 20, symbol, write_symbol, move_direction)
        else:
            x, y = self.positions[state]
            self.draw_arc(x, y)
            self.blit_text(x + 10, y - 50, symbol,
                           write_symbol, move_direction)
            drawn[state] = (x, y)
        # make white background for screen

    def draw_arc(self, x, y):
        """
        Draw an arc for a loop transition
        """
        rect = pygame.Rect(x, y - 30, 30, 30)
        start_angle = math.pi / 2
        stop_angle = 2.5 * math.pi
        pygame.draw.arc(self.graph, color=self.text_color, rect=rect,
                        start_angle=start_angle, stop_angle=stop_angle, width=2)

    def draw_line(self, state, next_state, symbol, write_symbol, move_direction):
        start_x, start_y = self.positions[state]
        end_x, end_y = self.positions[next_state]
        start_x += 20
        end_x -= 20

        # Draw an anti-aliased line with increased thickness
        pygame.draw.aaline(self.graph, self.line_color,
                           (start_x, start_y), (end_x, end_y))

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
        pygame.draw.polygon(self.graph, self.line_color, [
                            (end_x, end_y), ARROW_point1, ARROW_point2])

    def blit_text(self, x, y, symbol, write_symbol, move_direction):
        text_surface = font.render(
            f"{symbol}{ARROW}{write_symbol},{move_direction}", True, self.text_color)
        text_surface.set_alpha(200)
        text_surface.set_colorkey((0, 255, 0))
        self.graph.blit(text_surface, (x, y))

    def draw_states(self):
        for state in self.states_list:
            x, y = self.positions[state]
            draw_3d_circle(self.graph, x, y, 20, self.circle_color, text=state, text_color=self.text_color)
            # self.blit_state_text(x, y, state)

    def blit_state_text(self, x, y, state):
        text_surface = font.render(state, True, self.circle_color)
        text_surface.set_alpha(200)
        text_surface.set_colorkey((0, 255, 0))
        text_center = text_surface.get_rect(center=(x, y))
        self.graph.blit(text_surface, text_center)

    def calculate_layers_and_nodes(self):
        """
        Calculate the number of layers and nodes in each layer
        """
        self.start_state = 'q1'
        visited = {state: False for state in self.states_list}
        queue = deque([(self.start_state, 0)])
        layer_nodes = {}

        max_layer = 0
        max_nodes_in_layer = 0

        while queue:
            state, layer = queue.popleft()
            if not visited[state]:
                visited[state] = True
                layer_nodes.setdefault(layer, []).append(state)
                max_layer = max(max_layer, layer)
                max_nodes_in_layer = max(max_nodes_in_layer, len(layer_nodes[layer]))
                for next_state in self.transitions[state].values():
                    queue.append((next_state[0], layer + 1))

        return max_layer + 1, max_nodes_in_layer

    def calculate_spacing(self, num_layers, max_nodes_in_layer):
        """
        Calculate the spacing between nodes in the graph
        """
        SPACING_X = SCREEN_WIDTH // (num_layers + 1)
        SPACING_Y = SCREEN_HEIGHT // (max_nodes_in_layer + 1)
        MARGIN_X = SPACING_X
        MARGIN_Y = SPACING_Y * 2
        return SPACING_X, SPACING_Y, MARGIN_X, MARGIN_Y

    def initialize_queue(self):
        """
        Initialize the queue for BFS
        """
        self.start_state = 'q1'
        visited = {state: False for state in self.states_list}
        queue = deque([(self.start_state, 0)])
        layer_nodes = {}
        return visited, queue, layer_nodes

    def update_positions(self, state, layer, SPACING_X, SPACING_Y, MARGIN_X, layer_nodes):
        """
        Update the positions of the nodes in the graph
        """
        x = MARGIN_X + layer * SPACING_X
        num_nodes_in_layer = len(layer_nodes.get(layer, []))
        layer_height = SPACING_Y * (num_nodes_in_layer - 1)
        start_y = (SCREEN_HEIGHT - layer_height) // 2
        for i, state in enumerate(layer_nodes.get(layer, [])):
            y = start_y + i * SPACING_Y
            self.positions[state] = (x, y)
        layer_nodes.setdefault(layer, []).append(state)

    def init_positions(self):
        """
        Initialize the positions of the nodes in the graph
        """
        num_layers, max_nodes_in_layer = self.calculate_layers_and_nodes()
        SPACING_X, SPACING_Y, MARGIN_X, MARGIN_Y = self.calculate_spacing(num_layers, max_nodes_in_layer)
        visited, queue, layer_nodes = self.initialize_queue()

        while queue:
            state, layer = queue.popleft()
            if not visited[state]:
                visited[state] = True
                self.update_positions(state, layer, SPACING_X, SPACING_Y, MARGIN_X, layer_nodes)
                for next_state in self.transitions[state].values():
                    queue.append((next_state[0], layer + 1))