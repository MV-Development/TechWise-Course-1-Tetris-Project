########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import difficulty
import interface
import game_loop

########################################################################################################################
# Global Variables

SCREEN = block_game.screen
SIZE = block_game.SIZE


########################################################################################################################
# Main Function
def time_select():
    SCREEN.fill(interface.BLACK)

    ####################################################################################################################
    # Time Limit Buttons
    limit5_button = interface.MenuButton(SCREEN, interface.WHITE, SIZE * 0.4, SIZE * 0.3125, SIZE, '5 Minute',
                                         interface.BLACK, 'franklingothicmedium', int(SIZE * (28 / 800)))
    limit5_button.draw_button()

    limit10_button = interface.MenuButton(SCREEN, (30, 144, 255), SIZE * 0.4, SIZE * (350 / 800), SIZE, "10 Minute",
                                          interface.BLACK, 'franklingothicmedium', int(SIZE * (28 / 800)))
    limit10_button.draw_button()

    limit15_button = interface.MenuButton(SCREEN, (41, 238, 238), SIZE * 0.4, SIZE * (450 / 800), SIZE, "15 Minute",
                                          interface.BLACK, 'franklingothicmedium', int(SIZE * (28 / 800)))
    limit15_button.draw_button()

    ####################################################################################################################
    # Quit Button
    quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * 0.4, SIZE * (550 / 800), SIZE, "QUIT",
                                       interface.BLACK, 'franklingothicmedium', int(SIZE * (28 / 800)))
    quit_button.draw_button()

    # Update Display
    pygame.display.flip()

    ####################################################################################################################
    # Take User Input
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if limit5_button.is_clicked():
                    game_loop.game()
                    # difficulty.diff_select()
                if limit10_button.is_clicked():
                    game_loop.game()
                    # difficulty.diff_select()
                if limit15_button.is_clicked():
                    game_loop.game()
                    # difficulty.diff_select()
                if quit_button.is_clicked():
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
