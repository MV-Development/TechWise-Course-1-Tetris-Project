########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import interface
import game_loop

########################################################################################################################
# Global Variables

SCREEN = block_game.screen
SIZE = block_game.SIZE


########################################################################################################################
# Main Function

def difficulty_select():
    SCREEN.fill(interface.BLACK)

    font = pygame.font.SysFont('franklingothicmedium', 28)
    font_title = pygame.font.SysFont('franklingothicmedium', 60)

    limit5_button = pygame.draw.rect(SCREEN, interface.RED,
                                     pygame.Rect((SIZE * 0.4), 250, (SIZE * 0.2), (SIZE * 0.125)))
    limit5_text = font.render('5 Min Limit', False, interface.BLACK)
    limit5_rect = limit5_text.get_rect(center=limit5_button.center)
    SCREEN.blit(limit5_text, limit5_rect)
    # limit5_button = interface.MenuButton.__init__(SCREEN, interface.RED, SIZE * 0.4, SIZE * 0.3125, SIZE,
    #                                              '''5 Min Limit''')
    # limit5_button.draw_button()

    limit10_button = pygame.draw.rect(SCREEN, (30, 144, 255),
                                      pygame.Rect((SIZE * 0.4), 350, (SIZE * 0.2), (SIZE * 0.125)))
    limit10_text = font.render('10 Min Limit', False, interface.BLACK)
    limit10_rect = limit10_text.get_rect(center=limit10_button.center)
    SCREEN.blit(limit10_text, limit10_rect)

    limit15_button = pygame.draw.rect(SCREEN, (141, 238, 238),
                                      pygame.Rect((SIZE * 0.4), 450, (SIZE * 0.2), (SIZE * 0.125)))
    limit15_text = font.render('15 Min Limit', False, interface.BLACK)
    limit15_rect = limit15_text.get_rect(center=limit15_button.center)
    SCREEN.blit(limit15_text, limit15_rect)

    # quit game button
    quit_button = pygame.draw.rect(SCREEN, interface.RED, pygame.Rect(320, 550, 160, 100))
    quit_text = font.render('Quit', False, interface.BLACK)
    quit_rect = quit_text.get_rect(center=quit_button.center)
    SCREEN.blit(quit_text, quit_rect)

    pygame.mouse.set_visible(True)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    game_loop.game()
                elif 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    game_loop.game()
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    game_loop.game()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
