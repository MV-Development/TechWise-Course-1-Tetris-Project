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

    game_over_space = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(320, 150, 160, 100))
    game_over_text = font.render('GAME OVER', False, interface.WHITE)
    game_over_rect = game_over_text.get_rect(center=game_over_space.center)
    SCREEN.blit(game_over_text, game_over_rect)

    score_space = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(320, 250, 160, 100))
    score_text = font.render(f'FINAL SCORE: {score}', False, interface.WHITE)
    score_rect = score_text.get_rect(center=score_space.center)
    SCREEN.blit(score_text, score_rect)

    restart_button = interface.MenuButton(SCREEN, interface.BLUE, SIZE * (320 / 800), SIZE * (350 / 800), SIZE,
                                          'New Game', interface.WHITE, 'franklingothicmedium', 60)
    restart_button.draw_button()

    quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * (320 / 800), SIZE * (550 / 800), SIZE, 'Quit',
                                       interface.WHITE, 'franklingothicmedium', 60)
    quit_button.draw_button()

    pygame.mouse.set_visible(True)
    pygame.display.flip()

    ########################################################################################################################
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
