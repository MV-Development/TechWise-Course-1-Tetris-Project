import pygame
import random
import sys
import os

pygame.init()
pygame.font.init()

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
start_button = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(320, 350, 160, 100))

# quit game button
quit_button = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(320, 550, 160, 100))

# text on buttons
font = pygame.font.SysFont('Arial', 30)
start_text = font.render('Start', False, (0, 0, 0))
start_rect = start_text.get_rect(center=start_button.center)
screen.blit(start_text, start_rect)
quit_text = font.render('Quit', False, (0, 0, 0))
quit_rect = quit_text.get_rect(center=quit_button.center)
screen.blit(quit_text, quit_rect)

# add everything to screen
pygame.mouse.set_visible(True)
pygame.display.flip()

# add menu music
# pygame.mixer.init()
# pygame.mixer.music.load('birthofahero.wav')
# pygame.mixer.music.play(-1)


def game():
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)

    pygame.mouse.set_visible(False)
    while True:
        for event in pygame.event.get():
            # spacebar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


# more code stuff

def main_menu():
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    # change screen color
                    screen.fill((255, 255, 255))
                    pygame.display.flip()
                    game()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


main_menu()
# def game():
#     while True:
# stuff
