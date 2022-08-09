########################################################################################################################
# Import statements
import sys
import pygame
import block_game
import interface
import select_screen

########################################################################################################################
# Global Variables
import select_screen

SCREEN = block_game.screen
SIZE = block_game.SIZE

########################################################################################################################
# main menu
tetris_button = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(320, 130, 160, 100))
tetris_font = pygame.font.SysFont('javanesetext', 100)
tetris_text = tetris_font.render('Block Game', False, interface.WHITE)
tetris_rect = tetris_text.get_rect(center=tetris_button.center)
SCREEN.blit(tetris_text, tetris_rect)

# start game button
# start_button = pygame.draw.rect(SCREEN, (118, 238, 198), pygame.Rect(SIZE * 0.1475, SIZE * 0.4375, SIZE * 0.2, SIZE * 0.125))
# start_text = font.render('Start', False, interface.BLACK)
# start_rect = start_text.get_rect(center=start_button.center)
# SCREEN.blit(start_text, start_rect)

start_button = interface.MenuButton(SCREEN, interface.GREEN, SIZE * 0.1475, SIZE * 0.4375, SIZE, 'START',
                                    'franklingothicmedium', 50)
start_button.draw_button()

# quit game button
# quit_button = pygame.draw.rect(SCREEN, interface.RED, pygame.Rect(SIZE * 0.4, SIZE * 0.6875, SIZE * 0.2, SIZE * 0.125))
# quit_text = font.render('Quit', False, interface.BLACK)
# quit_rect = quit_text.get_rect(center=quit_button.center)
# SCREEN.blit(quit_text, quit_rect)

quit_button = interface.MenuButton(SCREEN, interface.RED, SIZE * 0.1475, SIZE * 0.6875, SIZE, 'QUIT',
                                   'franklingothicmedium', 50)
quit_button.draw_button()

# add everything to SCREEN

pygame.mouse.set_visible(True)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        # on event click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position

            if start_button.is_clicked():
                select_screen.difficulty_select()
            if quit_button.is_clicked():
                pygame.quit()
                sys.exit(0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
