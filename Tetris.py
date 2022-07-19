import pygame
import random
import sys
import os

pygame.init()
pygame.font.init()

# window variables
w_width = 800
w_height = 800
block_size = 30

# screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Tetris')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)


class Piece:
    def __init__(self, x, y, tetro):
        self.x = x
        self.y = y
        self.tetro = tetro


def create_grid():
    # (rgb), x, y, l, w
    return [[(255, 255, 255) for _ in range(10)] for _ in range(20)]


def draw_grid():
    grid = create_grid()
    x = 170
    y = 70
    for i in range(20):
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 30, 30), 1)
        y += 30
        for j in range(10):
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 30, 30), 1)
            x += 30


def game():
    # change screen color
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.flip()
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    # new_piece()
    pygame.mouse.set_visible(False)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            # spacebar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


def main_menu():
    # main menu
    # start game button
    start_button = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(320, 350, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('Arial', 30)
    start_text = font.render('Start', False, (0, 0, 0))
    start_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_rect)
    quit_text = font.render('Quit', False, (0, 0, 0))
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
                    game()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


main_menu()


# def game_loop(board_state, score):
#   draw_board
#   spawn piece
#   while piece is moving
#       check for collision
#       take input
#       drop piece
#   stop piece, check for full row
#   determine game state


# def draw_board(game_pieces):
#   if board_state == 0
#       create_grid()
#       break
#   draw grid row by row
#   treat existing blocks as individual squares


# def collision_detection(piece_position):
#   identify lowest parts of current game piece
#   check color of adjacent block


# def rotate(piece_orientation):
#   on event up key down rotate
#   change surrounding colors
