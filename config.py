"""
Configuration file for the Turing Machine Simulator
"""
import pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
HEAD_WIDTH = 4
FPS = 120
BACKGROUND_COLOR = (100, 100, 100)  # Black
STATE_COLOR = (100, 255, 0)  # Green
TEXT_COLOR = (255, 255, 255)  # White
LINES_COLOR = (0, 0, 255)  # Blue
TAPE_COLOR = (200, 200, 200)
INITIAL_STATE = "q1"
TAPE_WIDTH = 2
FONT_SIZE = 11
FONT_PATH = pygame.font.match_font('Monaco')
font = pygame.font.Font(FONT_PATH, FONT_SIZE)

# Define a palette of Apple-inspired colors
palettes = [
    [  # Palette 1: Grayscale with blue accent
        (60, 60, 60),    # Dark Gray
        (0, 122, 255)    # Apple Blue
    ],
    [  # Palette 2: Grayscale with green accent
        (60, 60, 60),    # Dark Gray
        (76, 217, 100)   # Apple Green
    ],
    [  # Palette 3: Grayscale with red accent
        (60, 60, 60),    # Dark Gray
        (255, 59, 48)    # Apple Red
    ],
    [  # Palette 4: Grayscale with yellow accent
        (60, 60, 60),    # Dark Gray
        (255, 204, 0)    # Apple Yellow
    ],
    [  # Palette 5: Grayscale with purple accent
        (60, 60, 60),    # Dark Gray
        (88, 86, 214)    # Apple Purple
    ]
]
