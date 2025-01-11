import pygame
from pygame.locals import *
from init import *
from welcomePage import *
from constants import *
from selectShapes import *

choice = welcoming()
if choice != "" :
    screen.fill(WHITE)
    if choice == "Manually":
        createGridWithMouseInit()
    elif choice == "Random":
        createGridRandom()
    else: # shapes
        selectShape()
# begin 