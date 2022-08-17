########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import game_loop
import interface

screen = block_game.screen
SIZE = block_game.SIZE


def difficulty_select(time_limit):
    ####################################################################################################################
    # Difficulty buttons
    easy_button = interface.MenuButton(screen, interface.GREEN, SIZE * (320 / 800), SIZE * (250 / 800), SIZE, 'EASY',
                                       interface.WHITE, 'franklingothicmedium', int(SIZE * (28 / 800)))
    easy_button.draw_button()
    medium_button = interface.MenuButton(screen, interface.BLUE, SIZE * (320 / 800), SIZE * (350 / 800), SIZE, 'MEDIUM',
                                         interface.WHITE, 'franklingothicmedium', int(SIZE * (28 / 800)))
    medium_button.draw_button()
    hard_button = interface.MenuButton(screen, interface.RED, SIZE * (320 / 800), SIZE * (450 / 800), SIZE, 'HARD',
                                       interface.WHITE, 'franklingothicmedium', int(SIZE * (28 / 800)))
    hard_button.draw_button()
    quit_button = interface.MenuButton(screen, interface.RED, SIZE * (320 / 800), SIZE * (550 / 800), SIZE, 'QUIT',
                                       interface.BLACK, 'franklingothicmedium', int(SIZE * (28 / 800)))
    quit_button.draw_button()

    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if easy_button.is_clicked():
                    game_loop.game(time_limit, 1)
                elif medium_button.is_clicked():
                    game_loop.game(time_limit, 2)
                elif hard_button.is_clicked():
                    game_loop.game(time_limit, 3)
                elif quit_button.is_clicked():
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # screen.fill(BLACK)
        # my_group2.draw(screen)
        # my_group2.update()
        # my_group3.draw(screen)
        # my_group3.update()
        # my_group4.draw(screen)
        # my_group4.update()
        # my_group5.draw(screen)
        # my_group5.update()
        # clock.tick(6)

        # difficulty buttons
        # text_maker1('CHOOSE DIFFICULTY LEVEL', 30, WHITE, BLACK, 320, 100, 180, 50)
        # text_maker2('EASY', 32, BLACK, (141, 238, 238), 320, 250, 160, 100)
        # text_maker2('NORMAL', 32, BLACK, (30, 144, 255), 320, 350, 160, 100)
        # text_maker2('HARD', 32, BLACK, (141, 238, 238), 320, 450, 160, 100)
        # text_maker2('Quit', 32, BLACK, RED, 320, 550, 160, 100)

        # pygame.mouse.set_visible(True)
        # pygame.display.flip()
