import pygame
from pygame.locals import *

# Color constants
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# Grid and screen settings
cells = [[0] * 60 for i in range(35)]
cellSize = 20
WIDTH = 1280
HEIGHT = 720

# initialisation of py game 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill(WHITE)
