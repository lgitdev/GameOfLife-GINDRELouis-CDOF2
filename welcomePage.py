import pygame
from pygame.locals import *
from constants import *

s = ""

def welcoming():
    while True:
        draw()  # Draw the game window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ""  # Close the game when clicking the close button
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                # Detect the selected initialization method by coordinates
                if 300 <= y <= 320:
                    if 260 <= x <= 380:
                        s = "Manually"
                    elif 580 <= x <= 700:
                        s = "Random"
                    elif 840 <= x <= 1080:
                        s = "Shapes"

                # Button to start the game
                if 490 <= x <= 790 and 380 <= y <= 410:
                    return s  # Return the selected method when 'Begin' is clicked

        pygame.display.update()

    pygame.quit()

def draw():
    # Title
    font_title = pygame.font.SysFont('Arial', WIDTH // 15)
    title_img = font_title.render('Game Of Life', True, BLACK)
    screen.blit(title_img, (WIDTH // 2 - title_img.get_width() // 2, 20))

    # Subtitle: Initialization Method Selection
    font_subtitle = pygame.font.SysFont('Arial', WIDTH // 22)
    subtitle_img = font_subtitle.render('How do you want to initialize the cells?', True, BLACK)
    screen.blit(subtitle_img, (WIDTH // 2 - subtitle_img.get_width() // 2, 180))

    # Draw options for initialization method
    font_options = pygame.font.SysFont('Arial', WIDTH // 35)
    options = ["Manually", "Randomly", "Using specific forms"]
    column_width = WIDTH // 4
    column_x_start = WIDTH // 2 - column_width

    # Render each option centered in their respective columns
    for i, option in enumerate(options):
        option_img = font_options.render(option, True, BLACK)
        column_x = column_x_start + i * column_width
        screen.blit(option_img, (column_x - option_img.get_width() // 2, 300))

    # Begin the game button
    font_subtitle = pygame.font.SysFont('Arial', WIDTH // 22)
    begin_button_img = font_subtitle.render('Begin the game', True, WHITE)
    begin_button_rect = pygame.Rect(WIDTH // 2 - 150, 380, 300, 30)  # Defining the button area
    pygame.draw.rect(screen, (0, 128, 255), begin_button_rect)  # Blue background for button
    screen.blit(begin_button_img, (WIDTH // 2 - begin_button_img.get_width() // 2, 380))  # Center text

    # Optional: Hover effect for button (change color when hovering)
    if begin_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 100, 255), begin_button_rect)  # Change color on hover
