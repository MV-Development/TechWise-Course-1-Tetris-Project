########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import interface
import select_screen

########################################################################################################################
# Global Variables

SCREEN = block_game.screen
SIZE = block_game.SIZE

########################################################################################################################
# main menu
tetris_button = interface.MenuButton(SCREEN, interface.BLACK, int(SIZE * 0.4), int(SIZE * 0.15), SIZE, 'BLOCK GAME',
                                     interface.WHITE, 'javanesetext', int(SIZE * 0.125))
tetris_button.draw_button()
font = pygame.font.SysFont('franklingothicmedium', 50)
start_button = interface.MenuButton(SCREEN, interface.GREEN, int(SIZE * 0.4), int(SIZE * 0.4375), SIZE, 'START',
                                    interface.WHITE, 'franklingothicmedium', int(SIZE * 0.0625))
start_button.draw_button()
quit_button = interface.MenuButton(SCREEN, interface.RED, int(SIZE * 0.4), int(SIZE * 0.6875), SIZE, 'QUIT',
                                   interface.BLACK, 'franklingothicmedium', int(SIZE * 0.0625))
quit_button.draw_button()
pygame.display.flip()

########################################################################################################################
# Take User Input
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked():
                select_screen.time_select()
            if quit_button.is_clicked():
                pygame.quit()
                sys.exit(0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
