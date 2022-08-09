########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import interface
import game_loop

########################################################################################################################
# Global Variables
from interface import MenuButton

SCREEN = block_game.screen
SIZE = block_game.SIZE


########################################################################################################################
# Main Function

def difficulty_select():
    SCREEN.fill(interface.BLACK)

    ####################################################################################################################
    # Time Limit Buttons
    limit5_button = interface.MenuButton(SCREEN, interface.WHITE, SIZE * 0.4, SIZE * 0.3125, SIZE, '5 Minute',
                                         interface.BLACK, 'franklingothicmedium', 28)
    limit5_button.draw_button()

    limit10_button = interface.MenuButton(SCREEN, (30, 144, 255), SIZE * 0.4, SIZE * (350 / 800), SIZE, "10 Minute",
                                          interface.BLACK, 'franklingothicmedium', 28)
    limit10_button.draw_button()

    limit15_button = interface.MenuButton(SCREEN, (41, 238, 238), SIZE * 0.4, SIZE * (450 / 800), SIZE, "15 Minute",
                                          interface.BLACK, 'franklingothicmedium', 28)
    limit15_button.draw_button()

    ####################################################################################################################
    # Quit Button
    quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * 0.4, SIZE * (550 / 800), SIZE, "QUIT",
                                       interface.BLACK, 'franklingothicmedium', 28)
    quit_button.draw_button()

    pygame.display.flip()

    ####################################################################################################################
    # Input Loop
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if limit5_button.is_clicked():
                    game_loop.game()
                if limit10_button.is_clicked():
                    game_loop.game()
                if limit15_button.is_clicked():
                    game_loop.game()
                if quit_button.is_clicked():
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
