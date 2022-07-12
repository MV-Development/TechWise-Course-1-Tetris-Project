import pygame
import random
import sys
import os

pygame.init()

# window variables
w_width = 800
w_height = 800

# screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Tetris')
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

# main menu
# start game button
while True:
    start_button = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(320, 350, 160, 100))
    # quit game button
    quit_button = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(320, 550, 160, 100))
    pygame.mouse.set_visible(True)
    pygame.display.flip()
    for event in pygame.event.get():
        # on event click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            mouse = pygame.mouse.get_pos()
            if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                # change screen color
                start_button = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320, 350, 160, 100))
                quit_button = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320, 550, 160, 100))
                screen.fill((255, 255, 255))
                pygame.display.flip()
                # game()
            if 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 450:
                pygame.quit()
                sys.exit(0)

# main loop
# more code stuff


# def game():
#     while True:
# stuff
