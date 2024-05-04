"""
Configuration file for the Turing Machine Simulator
"""
import pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
HEAD_WIDTH = 4
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
STATE_COLOR = (100, 0, 0)  # Green
TEXT_COLOR = (255, 255, 255)  # White
LINES_COLOR = (0, 0, 255)  # Blue
TAPE_COLOR = (200, 200, 200)
INITIAL_STATE = "q1"
TAPE_WIDTH = 2
FONT_SIZE = 11
FONT_PATH = pygame.font.match_font('Monaco')
font = pygame.font.Font(FONT_PATH, FONT_SIZE)