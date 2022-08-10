########################################################################################################################
# Import statements
import pygame
import pieces
import main_menu

########################################################################################################################
# Initialization

pygame.init()
pygame.display.init()
pygame.font.init()

########################################################################################################################
# Display setup

SIZE = int(pygame.display.list_modes()[0][1] / 2)
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('''Block Game''')
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.mouse.set_visible(True)

########################################################################################################################
# Start Game
main_menu
