##########################################################################################
# Import statements
import pygame
import block_game
import interface
import game_loop

SCREEN = block_game.screen

##########################################################################################
# Main Function
def difficulty(screen, size):
    screen.fill(interface.BLACK)
    # main menu
    # start game button

    # limit5_button = pygame.draw.rect(screen, interface.RED, pygame.Rect((size * 0.4), 250, (size * 0.2), (size * 0.125)))
    limit5_button = interface.MenuButton.__init__(screen, interface.RED, size * 0.4, size * 0.3125, size,
                                                  '''5 Min Limit''')
    # limit10_button = pygame.draw.rect(screen, (30, 144, 255),
    #                                  pygame.Rect((size * 0.4), 350, (size * 0.2), (size * 0.125)))
    # limit15_button = pygame.draw.rect(screen, (141, 238, 238),
    #                                  pygame.Rect((size * 0.4), 450, (size * 0.2), (size * 0.125)))

    # quit game button
    quit_button = pygame.draw.rect(screen, interface.RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('franklingothicmedium', 28)
    font_title = pygame.font.SysFont('franklingothicmedium', 60)

    # limit5_text = font.render('5 Min Limit', False, interface.BLACK)
    # limit10_text = font.render('10 Min Limit', False, interface.BLACK)
    # limit15_text = font.render('15 Min Limit', False, interface.BLACK)
    #  limit5_rect = limit5_text.get_rect(center=limit5_button.center)
    # limit10_rect = limit10_text.get_rect(center=limit10_button.center)
    # limit15_rect = limit15_text.get_rect(center=limit15_button.center)
    # screen.blit(limit5_text,  limit5_button)
    limit5_button.draw_button()
    # screen.blit(limit10_text, limit10_rect)
    # screen.blit(limit15_text, limit15_rect)
    quit_text = font.render('Quit', False, interface.BLACK)
    quit_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_rect)
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
