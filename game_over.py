########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import interface
import select_screen

SCREEN = block_game.screen
SIZE = block_game.SIZE


########################################################################################################################
# Game Over
def game_over(score):
    SCREEN.fill(interface.BLACK)
    font = pygame.font.SysFont('franklingothicmedium', 60)

    # game_over_space = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(
    #    int(SIZE * (320 / 800)), int(SIZE * (150 / 800)), int(SIZE * (160 / 800)), int(SIZE * (100 / 800))))
    # game_over_text = font.render('GAME OVER', False, interface.WHITE)
    # game_over_rect = game_over_text.get_rect(center=game_over_space.center)
    # SCREEN.blit(game_over_text, game_over_rect)

    game_over_space = interface.MenuButton(SCREEN, interface.BLACK, int(SIZE * (320 / 800)), int(SIZE * (150 / 800)),
                                           SIZE, 'GAME OVER', interface.WHITE, 'franklingothicmedium',
                                           int(SIZE * (60 / 800)))
    game_over_space.draw_button()

    # score_space = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(320, 250, 160, 100))
    # score_text = font.render(f'FINAL SCORE: {score}', False, interface.WHITE)
    # score_rect = score_text.get_rect(center=score_space.center)
    # SCREEN.blit(score_text, score_rect)

    score_space = interface.MenuButton(SCREEN,
                                       interface.BLACK, int(SIZE * (320 / 800)), int(SIZE * (250 / 800)),
                                       SIZE, f'FINAL SCORE: {score}', interface.WHITE, 'franklingothicmedium',
                                       int(SIZE * (60 / 800)))
    score_space.draw_button()

    restart_button = interface.MenuButton(SCREEN, interface.BLUE, SIZE * (320 / 800), SIZE * (350 / 800), SIZE,
                                          'New Game', interface.WHITE, 'franklingothicmedium', int(SIZE * (25 / 800)))
    restart_button.draw_button()

    quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * (320 / 800), SIZE * (550 / 800), SIZE, 'Quit',
                                       interface.WHITE, 'franklingothicmedium', int(SIZE * (25 / 800)))
    quit_button.draw_button()

    pygame.mouse.set_visible(True)
    pygame.display.flip()

    ####################################################################################################################
    # Take User Input
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if restart_button.is_clicked():
                    select_screen.difficulty_select()
                if quit_button.is_clicked():
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
