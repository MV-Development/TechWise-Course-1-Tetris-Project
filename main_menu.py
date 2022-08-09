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
tetris_button = interface.MenuButton(SCREEN, interface.BLUE, SIZE * 0.4, SIZE * 0.15, SIZE, 'BLOCK GAME',
                                     interface.WHITE, 'javanesetext', 50)
tetris_button.draw_button()

font = pygame.font.SysFont('franklingothicmedium', 50)
# start game button
start_button = interface.MenuButton(SCREEN, interface.GREEN, SIZE * (320 / 800), SIZE * (350 / 800), SIZE, 'START',
                                    interface.WHITE, 'franklingothicmedium', 50)
start_button.draw_button()

# quit game button
quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * (320 / 800), SIZE * (550 / 800), SIZE, 'QUIT',
                                   interface.BLACK, 'franklingothicmedium', 50)
quit_button.draw_button()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        # on event click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked", pygame.mouse.get_pos())
            if start_button.is_clicked():
                print("start_button clicked")
                select_screen.difficulty_select()
            if quit_button.is_clicked():
                print("quit_button clicked")
                pygame.quit()
                sys.exit(0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
