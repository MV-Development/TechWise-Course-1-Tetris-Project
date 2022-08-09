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

SIZE = pygame.display.list_modes()[0][1] / 2
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('''Block Game''')
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.mouse.set_visible(True)

########################################################################################################################
# Global Variables
BLOCK_SIZE = SIZE * 0.0375
PIECE_NAMES = pieces.PIECE_NAMES

########################################################################################################################
# Start Game
main_menu
