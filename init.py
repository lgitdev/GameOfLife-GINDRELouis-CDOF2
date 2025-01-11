import pygame
from pygame.locals import *
from constants import *
import random
from time import sleep

"""
This function is used if the user wants to create the initialization manually, using the mouse to select the living cells
"""
def createGridWithMouseInit(cell=cells):
    running = True

    while running:
        drawGrid(cell) # create a grid for the game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                updateGrid(event)
                x, y = event.pos
                if WIDTH//2-60 <= x <= WIDTH//2+60 and HEIGHT-60 <= y <= HEIGHT:
                    while True:
                        for inner_event in pygame.event.get(): 
                            if inner_event.type == pygame.QUIT:  
                                running = False
                                break 
                        if not running:
                            break  

                        cell = run(cell)  
                        drawGrid(cell) 
                        pygame.display.update()
                        sleep(0.5) 
                

        pygame.display.update()
    
    pygame.quit()

def createGridRandom():
    cells = [[1 if random.random() < 0.2 else 0 for _ in range(60)] for _ in range(35)] # random initialization
    createGridWithMouseInit(cells)


def drawGrid(cell):
    font = pygame.font.SysFont(None, WIDTH//22)
    img = font.render('Game Of Life', True, BLACK)
    screen.blit(img, (WIDTH // 2 - img.get_width() // 2, 5))


    for x in range(40, WIDTH-40, cellSize): # create the grid
        for y in range(40, HEIGHT-40, cellSize):
            rect = pygame.Rect(x, y, cellSize, cellSize)
            if cell[(y-40)//20][(x-40)//20] == 0: # cell dead
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

def run(cell):
    rows = len(cell) 
    cols = len(cell[0]) 
    new_cells = [[0] * 60 for i in range(35)]

    for i in range(rows): # run through each cell
        for j in range(cols):
            count = 0 # number of neighbors alive

            for dx in range(-1,2): # check all neighbors
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue # ignore the cell itself

                    if 0 <= i + dx < rows and 0 <= j + dy < cols:
                        if cell[i+dx][j+dy] == 1:
                            count += 1
                    
                    if cell[i][j] == 1: # cell initially alive 
                        if not (count == 2 or count ==3):
                            new_cells[i][j] =  0 # alive cell dies if number of alive neighbors not 2 or 3 
                        else:
                            new_cells[i][j] = 1

                    if cell[i][j] == 0: # cell initially dead
                        if count == 3:
                            new_cells[i][j] = 1 # becomes alive if 3 alive neighbors
                        else:
                            new_cells[i][j] = 0


    return new_cells
  