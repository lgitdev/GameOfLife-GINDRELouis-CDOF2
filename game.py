import pygame
from pygame.locals import *

# color constants
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# values of the cells
cells = [[0] * 64 for i in range(39)]
cellSize = 20 

def main():
    global screen, clock # let these parameters accessible everywhere so we can access these variables in every method
    # initialisation of py game 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    screen.fill(WHITE)
    running = True

    while running:
        drawGrid() # create a grid for the game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                updateGrid(event)

        pygame.display.update()
    
    pygame.quit()



def drawGrid():
    for x in range(0, 1280, cellSize): # create the grid
        for y in range(0, 780, cellSize):
            rect = pygame.Rect(x, y, cellSize, cellSize)
            if cells[y//20][x//20] == 0: # cell dead
                pygame.draw.rect(screen, BLACK, rect, 10)
            else: # cell alive
                pygame.draw.rect(screen, WHITE, rect, 10)

def updateGrid(event):
    x, y = event.pos # from the mouse click, change if a cell is alive or not
    x //= 20
    y //= 20
    cells[y][x] = 1 - cells[y][x]


main()