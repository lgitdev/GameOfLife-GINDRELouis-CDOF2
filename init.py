import pygame
from pygame.locals import *
from constants import *

"""
This function is used if the user wants to create the initialization manually, using the mouse to select the living cells
"""
def createGridWithMouseInit():
    running = True

    while running:
        drawGrid() # create a grid for the game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                updateGrid(event)
                x, y = event.pos
                if WIDTH//2-60 <= x <= WIDTH//2+60 and HEIGHT-60 <= y <= HEIGHT:
                    running = False
                

        pygame.display.update()
    
    pygame.quit()



def drawGrid():
    font = pygame.font.SysFont(None, WIDTH//22)
    img = font.render('Game Of Life', True, BLACK)
    screen.blit(img, (WIDTH // 2 - img.get_width() // 2, 5))


    for x in range(40, WIDTH-40, cellSize): # create the grid
        for y in range(40, HEIGHT-40, cellSize):
            rect = pygame.Rect(x, y, cellSize, cellSize)
            if cells[(y-40)//20][(x-40)//20] == 0: # cell dead
                pygame.draw.rect(screen, BLACK, rect, 10)
            else: # cell alive
                pygame.draw.rect(screen, WHITE, rect, 10)

    font = pygame.font.SysFont(None, WIDTH//44)
    img = font.render('Begin the game', True, BLACK)
    screen.blit(img, (WIDTH // 2 - img.get_width() // 2, HEIGHT-30))

    


def updateGrid(event):
    x, y = event.pos # from the mouse click, change if a cell is alive or not
    x -= 40
    y -= 40
    x //= 20
    y //= 20
    cells[y][x] = 1 - cells[y][x]