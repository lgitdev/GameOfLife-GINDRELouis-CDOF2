import pygame
from pygame.locals import *
from constants import *
from init import *

"""
This function is used if the user wants to create the initialization with shapes
"""
s = ""
def selectShape():
    running = True
    while running:
        select()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 240 <= y <= 260: # Still 
                    if 280 <= x <= 360: # Block
                        initShape("Block")
                    elif 580 <= x <= 700: # Bee
                        initShape("Bee")
                    elif 930 <= x <= 990: # Leaf
                        initShape("Leaf")
                elif 380 <= y <= 400: # Oscillator
                    if 270 <= x <= 380: # Blinker
                        initShape("Blinker")
                    elif 580 <= x <= 690: # Beacon
                        initShape("Beacon")
                    elif 910 <= x <= 1010: # Pulsar
                        initShape("Pulsar")
                elif 520 <= y <= 540: # Spaceship
                    if 170 <= x <= 260: # Glider
                        initShape("Glider")
                    elif 550 <= x <= 730: # Light weight
                        initShape("Light")
                if 600 <= y <= 630 and 490 <= x <= 790: # begin the same 
                    initShape("Begin")
                

        pygame.display.update()
    
    pygame.quit()

def initShape(shape):
    global cells
    match shape:
        case "Block":
            cells = [[0] * 60 for i in range(35)]
            cells[16][30] = 1
            cells[16][31] = 1
            cells[17][30] = 1
            cells[17][31] = 1
        case "Bee":
            cells = [[0] * 60 for i in range(35)]
            cells[16][30] = 1
            cells[16][31] = 1
            cells[17][32] = 1
            cells[18][31] = 1
            cells[18][30] = 1
            cells[17][29] = 1
        case "Leaf":
            cells = [[0] * 60 for i in range(35)]
            cells[16][30] = 1
            cells[16][31] = 1
            cells[17][32] = 1
            cells[18][32] = 1
            cells[19][31] = 1
            cells[18][30] = 1
            cells[17][29] = 1
        case "Blinker":
            cells = [[0] * 60 for i in range(35)]
            cells[16][30] = 1
            cells[16][31] = 1
            cells[16][32] = 1
        case "Beacon":
            cells = [[0] * 60 for i in range(35)]
            cells[15][29] = 1
            cells[15][30] = 1
            cells[16][29] = 1
            cells[16][30] = 1
            cells[17][31] = 1
            cells[17][32] = 1
            cells[18][31] = 1
            cells[18][32] = 1
        case "Pulsar":
            cells = [[0] * 60 for i in range(35)]
            cells[10][10] = 1
            cells[11][10] = 1
            cells[12][10] = 1
            cells[8][12] = 1
            cells[8][13] = 1
            cells[8][14] = 1
            cells[10][15] = 1
            cells[11][15] = 1
            cells[12][15] = 1
            cells[13][12] = 1
            cells[13][13] = 1
            cells[13][14] = 1

            cells[10][17] = 1
            cells[11][17] = 1
            cells[12][17] = 1
            cells[8][18] = 1
            cells[8][19] = 1
            cells[8][20] = 1
            cells[10][22] = 1
            cells[11][22] = 1
            cells[12][22] = 1
            cells[13][18] = 1
            cells[13][19] = 1
            cells[13][20] = 1

            cells[16][10] = 1
            cells[17][10] = 1
            cells[18][10] = 1
            cells[15][12] = 1
            cells[15][13] = 1
            cells[15][14] = 1
            cells[16][15] = 1
            cells[17][15] = 1
            cells[18][15] = 1
            cells[20][12] = 1
            cells[20][13] = 1
            cells[20][14] = 1

            cells[16][17] = 1
            cells[17][17] = 1
            cells[18][17] = 1
            cells[15][18] = 1
            cells[15][19] = 1
            cells[15][20] = 1
            cells[16][22] = 1
            cells[17][22] = 1
            cells[18][22] = 1
            cells[20][18] = 1
            cells[20][19] = 1
            cells[20][20] = 1
        case "Glider":
            cells = [[0] * 60 for i in range(35)]
            cells[2][2] = 1
            cells[2][4] = 1
            cells[3][3] = 1
            cells[3][4] = 1
            cells[4][3] = 1
        case "Light":
            cells = [[0] * 60 for i in range(35)]
            cells[17][2] = 1
            cells[18][2] = 1
            cells[17][3] = 1
            cells[18][3] = 1
            cells[19][3] = 1
            cells[16][4] = 1
            cells[18][4] = 1
            cells[19][4] = 1
            cells[16][5] = 1
            cells[17][5] = 1
            cells[18][5] = 1
            cells[17][6] = 1
        case "Begin":
            screen.fill(WHITE)
            createGridWithMouseInit(cells)
        case _:
            pass
    

def select():
    # Title
    font_title = pygame.font.SysFont(None, WIDTH // 15)
    title_img = font_title.render('Game Of Life', True, BLACK)
    screen.blit(title_img, (WIDTH // 2 - title_img.get_width() // 2, 20))

    # Sub-title
    font_subtitle = pygame.font.SysFont(None, WIDTH // 22)
    subtitle_img = font_subtitle.render('Please select a specific shape to put on the grid', True, BLACK)
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 100))

    # Still Life options
    font_category = pygame.font.SysFont(None, WIDTH // 30)
    still_life_img = font_category.render('Still life', True, BLACK)
    screen.blit(still_life_img, (WIDTH // 2 - still_life_img.get_width() // 2, 200))

    still_life_options = ["Block", "Bee-hive", "Leaf"]
    still_life_column_width = WIDTH // 4
    still_life_x_start = WIDTH // 2 - still_life_column_width

    for i, option in enumerate(still_life_options):
        option_img = font_category.render(option, True, BLACK)
        column_x = still_life_x_start + i * still_life_column_width
        screen.blit(option_img, (column_x - option_img.get_width() // 2, 240))

    # Oscillators options
    oscillators_img = font_category.render('Oscillators', True, BLACK)
    screen.blit(oscillators_img, (WIDTH // 2 - oscillators_img.get_width() // 2, 340))

    oscillators_options = ["Blinker", "Beacon", "Pulsar"]
    oscillators_column_width = WIDTH // 4
    oscillators_x_start = WIDTH // 2 - oscillators_column_width

    for i, option in enumerate(oscillators_options):
        option_img = font_category.render(option, True, BLACK)
        column_x = oscillators_x_start + i * oscillators_column_width
        screen.blit(option_img, (column_x - option_img.get_width() // 2, 380))

    # Spaceships options
    spaceships_img = font_category.render('Spaceships', True, BLACK)
    screen.blit(spaceships_img, (WIDTH // 2 - spaceships_img.get_width() // 2, 480))

    spaceships_options = ["Glider", "Light-weight"]
    spaceships_column_width = WIDTH // 3
    spaceships_x_start = WIDTH // 2 - spaceships_column_width

    for i, option in enumerate(spaceships_options):
        option_img = font_category.render(option, True, BLACK)
        column_x = spaceships_x_start + i * spaceships_column_width
        screen.blit(option_img, (column_x - option_img.get_width() // 2, 520))

    # begin button
    font_subtitle = pygame.font.SysFont(None, WIDTH // 22)
    subtitle_img = font_subtitle.render('Begin the game', True, BLACK)
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 600))
