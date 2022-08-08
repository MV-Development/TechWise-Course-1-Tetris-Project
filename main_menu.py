##########################################################################################
# Import statements
import pygame
import block_game
import interface
import select_screen

SCREEN = block_game.screen
SIZE = block_game.SIZE

##########################################################################################
# Global Variables


def menu(size, block_size):
    # main menu
    tetris_button = pygame.draw.rect(SCREEN, interface.BLACK, pygame.Rect(320, 130, 160, 100))

    # start game button
    start_button = pygame.draw.rect(SCREEN, (118, 238, 198), pygame.Rect(320, 350, 160, 100))


# quit game button
quit_button = pygame.draw.rect(SCREEN, interface.RED, pygame.Rect(320, 550, 160, 100))

# text on buttons
tetris_font = pygame.font.SysFont('javanesetext', 100)
tetris_text = tetris_font.render('Block Game', False, interface.WHITE)
tetris_rect = tetris_text.get_rect(center=tetris_button.center)
SCREEN.blit(tetris_text, tetris_rect)
font = pygame.font.SysFont('franklingothicmedium', 50)
start_text = font.render('Start', False, interface.BLACK)
start_rect = start_text.get_rect(center=start_button.center)
SCREEN.blit(start_text, start_rect)
quit_text = font.render('Quit', False, interface.BLACK)
quit_rect = quit_text.get_rect(center=quit_button.center)
SCREEN.blit(quit_text, quit_rect)

# add everything to SCREEN
pygame.mouse.set_visible(True)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        # on event click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            mouse = pygame.mouse.get_pos()
            if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                select_screen.difficulty(SCREEN, SIZE)
            elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                pygame.quit()
                sys.exit(0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
