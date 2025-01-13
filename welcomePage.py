import pygame
from pygame.locals import *
from constants import *

s = ""

def welcoming():
    while True:
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ""
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos

                # Définir les zones de clic pour les boutons
                button_width = 300
                button_height = 50
                column_width = WIDTH // 4
                column_x_start = WIDTH // 2 - column_width
                button_y = 290

                buttons = {
                    "Manually": pygame.Rect(column_x_start - button_width // 2, button_y, button_width, button_height),
                    "Random": pygame.Rect(column_x_start + column_width - button_width // 2, button_y, button_width, button_height),
                    "Shapes": pygame.Rect(column_x_start + 2 * column_width - button_width // 2, button_y, button_width, button_height),
                }

                # Vérifier si un bouton est cliqué
                for key, rect in buttons.items():
                    if rect.collidepoint(x, y):
                        s = key

                # Zone de clic pour le bouton "Begin the game"
                begin_button_width = 320
                begin_button_height = 100
                begin_button_rect = pygame.Rect(
                    WIDTH // 2 - begin_button_width // 2, 380, begin_button_width, begin_button_height
                )

                if begin_button_rect.collidepoint(x, y):
                    return s

        pygame.display.update()

    pygame.quit()

def draw():
    screen.fill((220, 220, 220))

    # Titre principal
    font_title = pygame.font.SysFont('Arial', WIDTH // 15)
    title_img = font_title.render('Game Of Life', True, (0, 128, 255))
    screen.blit(title_img, (WIDTH // 2 - title_img.get_width() // 2, 20))

    # Additional introductory text
    intro_text = [
        "In this simulation, cells live, die, or thrive based on simple rules.",
        "Your task is to initialize the grid and watch how patterns evolve over time.",
        "The famous game by mathematician John Horton Conway provides endless possibilities!",
        "Choose an initialization method below to get started!"
    ]
    font_text = pygame.font.SysFont(None, WIDTH // 40)
    for i, line in enumerate(intro_text):
        line_img = font_text.render(line, True, BLACK)
        screen.blit(line_img, (WIDTH // 2 - line_img.get_width() // 2, 140 + i * 30))

    # Sous-titre
    font_subtitle = pygame.font.SysFont('Arial', WIDTH // 22)
    subtitle_img = font_subtitle.render('How do you want to initialize the cells?', True, (50, 50, 50))
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 280))


    # Options de boutons
    font_options = pygame.font.SysFont('Arial', WIDTH // 35)
    options = ["Manually", "Randomly", "Using specific forms"]
    column_width = WIDTH // 4
    column_x_start = WIDTH // 2 - column_width

    button_width = 300  # Largeur des boutons
    button_height = 50  # Hauteur des boutons
    button_y = 350      # Position Y des boutons

    for i, option in enumerate(options):
        option_img = font_options.render(option, True, (255, 255, 255))
        column_x = column_x_start + i * column_width
        button_rect = pygame.Rect(column_x - button_width // 2, button_y, button_width, button_height)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 0, 0), button_rect)  
        else:
            pygame.draw.rect(screen, (240, 0, 0), button_rect)  

        screen.blit(option_img, (column_x - option_img.get_width() // 2, button_y + button_height // 4))

   
    font_subtitle = pygame.font.SysFont('Arial', WIDTH // 22)
    begin_button_img = font_subtitle.render('Begin the game', True, (255, 255, 255))
    begin_button_width = 320 
    begin_button_height = 100  
    begin_button_rect = pygame.Rect(WIDTH // 2 - begin_button_width // 2, 430, begin_button_width, begin_button_height)

   
    if begin_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (200, 0, 0), begin_button_rect) 
    else:
        pygame.draw.rect(screen, (240, 0, 0), begin_button_rect) 

    screen.blit(begin_button_img, (WIDTH // 2 - begin_button_img.get_width() // 2, 430 + begin_button_height // 4))
