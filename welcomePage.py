import pygame
from pygame.locals import *
from constants import *

"""
This function is used if the user wants to create the initialization manually, using the mouse to select the living cells
"""
s = ""
def welcoming():
    while True:
        draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ""
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= y <= 320:
                    if 260 <= x <= 380:
                        s = "Manually"
                    elif 580 <= x <= 700:
                        s = "Random"
                    elif 840 <= x <= 1080:
                        s = "Shapes"

                if 490 <= x <= 790 and 380 <= y <= 410:
                    return s

                    # next : put choice for if periodic boundary or not
                

        pygame.display.update()
    
    pygame.quit()

def draw():
    # Title
    font_title = pygame.font.SysFont(None, WIDTH // 15)
    title_img = font_title.render('Game Of Life', True, BLACK)
    screen.blit(title_img, (WIDTH // 2 - title_img.get_width() // 2, 20))

     # Introductory sentence
    font_intro = pygame.font.SysFont(None, WIDTH // 30)
    intro_img = font_intro.render('Welcome to the Game of Life, a cellular automaton simulation!', True, BLACK)
    screen.blit(intro_img, (WIDTH // 2 - intro_img.get_width() // 2, 100))

    # Introductory text
    intro_text = [
        "In this simulation, cells live, die, or thrive based on simple rules.",
        "Your task is to initialize the grid and watch how patterns evolve over time.",
        "The famous game by mathematician John Horton Conway provides endless possibilities!",
        "Choose an initialization method below to get started!"
    ]
    font_text = pygame.font.SysFont(None, WIDTH // 45)
    for i, line in enumerate(intro_text):
        line_img = font_text.render(line, True, BLACK)
        screen.blit(line_img, (WIDTH // 2 - line_img.get_width() // 2, 140 + i * 30))

    # Select the initialization method
    font_subtitle = pygame.font.SysFont(None, WIDTH // 22)
    subtitle_img = font_subtitle.render('How do you want to initialize the cells?', True, BLACK)
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 260))

    # draw the columns with options for initialization
    font_options = pygame.font.SysFont(None, WIDTH // 35)
    options = ["Manually", "Randomly", "Using specific forms"]
    column_width = WIDTH // 4  
    column_x_start = WIDTH // 2 - column_width # center the columns with a padd

    for i, option in enumerate(options): # render each option 
        option_img = font_options.render(option, True, BLACK)
        column_x = column_x_start + i * column_width 
        screen.blit(option_img, (column_x - option_img.get_width() // 2, 320))

    # begin button
    font_subtitle = pygame.font.SysFont(None, WIDTH // 22)
    subtitle_img = font_subtitle.render('Begin the game', True, BLACK)
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 400))