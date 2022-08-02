##########################################################################################
# Import statements
import pygame
import sys
import game_loop

##########################################################################################
# Global Variables
WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
COLORS = [BLUE, RED, GREEN]
BLOCK_SIZE = 30

# window variables
w_width = 800
w_height = 800

screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Block Game')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)

color_speed = 1
color_direction = [-1, 1, -1]
default_color = [140, 120, 230]

def color_change(color, direction):
    for i in range(len(color)):
        color[i] += color_speed * direction[i]
        # reversing the direction of the intensity
        if color[i] >= 255 or color[i] <= 0:
            direction[i] *= -1

def menu():
    # main menu
    # start game button
    start_button = pygame.draw.rect(screen, (118, 238, 198), pygame.Rect(320, 350, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('franklingothicmedium', 50)
    start_text = font.render('Start', False, BLACK)
    start_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_rect)
    quit_text = font.render('Quit', False, BLACK)
    quit_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_rect)

    # add everything to screen
    pygame.mouse.set_visible(True)
    pygame.display.flip()

    # add menu music
    # pygame.mixer.init()
    # pygame.mixer.music.load('birthofahero.wav')
    # pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    game_select()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # title game button & text
        title_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 130, 160, 100))
        title_font = pygame.font.SysFont('javanesetext', 100)
        title_text = title_font.render('BLOCK GAME', False, default_color)
        title_rect = title_text.get_rect(center=title_button.center)
        screen.blit(title_text, title_rect)

        color_change(default_color, color_direction)

        pygame.display.update()


def game_select():
    screen.fill(BLACK)
    # main menu
    # start game button

    limit5_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 250, 160, 100))
    limit10_button = pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(320, 350, 160, 100))
    limit15_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 450, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('franklingothicmedium', 28)
    font_title = pygame.font.SysFont('franklingothicmedium', 60)

    limit5_text = font.render('5 Min Limit', False, BLACK)
    limit10_text = font.render('10 Min Limit', False, BLACK)
    limit15_text = font.render('15 Min Limit', False, BLACK)
    limit5_rect = limit5_text.get_rect(center=limit5_button.center)
    limit10_rect = limit10_text.get_rect(center=limit10_button.center)
    limit15_rect = limit15_text.get_rect(center=limit15_button.center)
    screen.blit(limit5_text, limit5_rect)
    screen.blit(limit10_text, limit10_rect)
    screen.blit(limit15_text, limit15_rect)
    quit_text = font.render('Quit', False, BLACK)
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

