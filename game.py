import pygame

# color constants
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

def main():
    global screen, clock # let these parameters accessible everywhere so we can access these variables in every method
    # initialisation of py game 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    running = True

    while running:
        drawGrid() # create a grid for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    
    pygame.quit()



def drawGrid():
    cellSize = 20 # size of a cell
    for x in range(0, 1280, cellSize): # create the grid
        for y in range(0, 780, cellSize):
            rect = pygame.Rect(x, y, cellSize, cellSize)
            pygame.draw.rect(screen, WHITE, rect, 1)



main()