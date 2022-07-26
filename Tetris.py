import pygame
import random
import sys
import os
import hud

pygame.init()
pygame.font.init()

WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
BLOCK_SIZE = 30

# window variables
w_width = 800
w_height = 800

# screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Tetris')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)

COLORS = [BLUE, RED, GREEN]


class Piece:
    def __init__(self, x, y, tetro):
        self.x = x
        self.y = y
        self.tetro = tetro

    def move_piece_left(self):
        self.x -= BLOCK_SIZE

    def move_piece_right(self):
        self.x += BLOCK_SIZE


def create_grid():
    # (rgb), x, y, l, w
    grid = [[BLACK for _ in range(10)] for _ in range(20)]
    return grid


def update_grid(grid):
    x = 221
    y = 71
    # grid[0][0] = RED
    # grid[0][9] = GREEN
    # grid[19][0] = BLUE
    # grid[19][9] = WHITE
    for i in range(len(grid)):
        y += BLOCK_SIZE
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, grid[i][j], (x + (BLOCK_SIZE) * (j + 1), y, BLOCK_SIZE - 1, BLOCK_SIZE - 1))
    pygame.display.update()


def draw_lines():
    x = 250
    y = 100

    for i in range(21):
        pygame.draw.line(screen, WHITE, (250, y), (w_width - 250, y))
        y += BLOCK_SIZE
    for j in range(11):
        pygame.draw.line(screen, WHITE, (x, 100), (x, w_width - 100))
        x += BLOCK_SIZE


def new_piece(color):
    x = 221
    y = 71
    grid = create_grid()
    piece_sel = ('L')
    choice = random.choice(piece_sel)

    # if choice == 'O':
    # grid[0][4] = color
    # grid[0][5] = color
    # grid[1][4] = color
    # grid[1][5] = color
    if choice == 'L':
        grid[0][4] = color
        grid[0][5] = color
        grid[0][6] = color
        grid[1][6] = color
    return grid


def sort_blocks():
    print("blocks sorted")

def game():
    # change screen color
    screen.fill(BLACK)
    # draw_grid()
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    # new_piece()
    draw_lines()
    pygame.mouse.set_visible(False)
    start_time = pygame.time.get_ticks()
    color = random.choice(COLORS)
    grid = create_grid()
    piece_grid = new_piece(color)
    update_grid(piece_grid)

    while True:
        hud.create_hud(screen, start_time)
        ###ATTEMPT AT GAME CLOCK
        pygame.display.update()
        for event in pygame.event.get():
            # spacebar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_RIGHT:
                    for row in range(len(grid)):
                        for col in range(len(grid[row]) - 1):
                            if grid[row][col + 1] == BLACK and piece_grid[row][col] == color:
                                piece_grid[row][col] = BLACK
                                piece_grid[row][col + 1] = color
                                break
                if event.key == pygame.K_LEFT:
                    for row in range(len(grid)):
                        for col in range(len(grid[row])):
                            if grid[row][col - 1] == BLACK and piece_grid[row][col] == color:
                                piece_grid[row][col] = BLACK
                                piece_grid[row][col - 1] = color
                                break

                update_grid(piece_grid)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

def game_over():
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 60)
    game_over_space = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 250, 160, 100))
    game_over_text = font.render('GAME OVER', False, WHITE)
    game_over_rect = game_over_text.get_rect(center=game_over_space.center)
    screen.blit(game_over_text, game_over_rect)

    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))
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
                    game_select()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

def game5():
    # change screen color
    screen.fill(BLACK)
    # draw_grid()
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    # new_piece()
    draw_lines()
    pygame.mouse.set_visible(False)
    start_time = pygame.time.get_ticks()
    color = random.choice(COLORS)
    grid = create_grid()
    piece_grid = new_piece(color)
    update_grid(piece_grid)
    clock = pygame.time.Clock
    while True:
        theTime = hud.limit5(screen, start_time)
        if theTime == "ASSY":
            game_over()
        ###ATTEMPT AT GAME CLOCK
        pygame.display.update()
        for event in pygame.event.get():
            # spacebar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_RIGHT:
                    for row in range(len(grid)):
                        for col in range(len(grid[row]) - 1):
                            if grid[row][col + 1] == BLACK and piece_grid[row][col] == color:
                                piece_grid[row][col] = BLACK
                                piece_grid[row][col + 1] = color
                                break
                if event.key == pygame.K_LEFT:
                    for row in range(len(grid)):
                        for col in range(len(grid[row])):
                            if grid[row][col - 1] == BLACK and piece_grid[row][col] == color:
                                piece_grid[row][col] = BLACK
                                piece_grid[row][col - 1] = color
                                break

                update_grid(piece_grid)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


def main_menu():
    # main menu
    # start game button
    start_button = pygame.draw.rect(screen, BLUE, pygame.Rect(320, 350, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('Arial', 50)
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

def game_select():
    screen.fill(BLACK)
    # main menu
    # start game button

    limit5_button = pygame.draw.rect(screen, GREEN, pygame.Rect(320, 250, 160, 100))
    limit10_button = pygame.draw.rect(screen, BLUE, pygame.Rect(320, 350, 160, 100))
    limit15_button = pygame.draw.rect(screen, GREEN, pygame.Rect(320, 450, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('Arial', 30)
    font_title = pygame.font.SysFont('Arial', 60)

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
                    game()
                elif 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    game5()
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    game()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)



main_menu()



# 4x4 grid
# 0   1    2    3
# 4   5    6    7
# 8   9    10   11
# 12  13   14   15

# def game_loop(board_state, score):
#   draw_board
#   spawn_piece
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
