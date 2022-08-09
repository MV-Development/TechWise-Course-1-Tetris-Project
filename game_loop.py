##########################################################################################
# Import statements
import pygame
import random
import sys
import hud
import pieces
import main_menu
from collections import deque

##########################################################################################
# Global Variables
WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
COLORS = [BLUE, RED, GREEN]
BLOCK_SIZE = 30

# window variables
w_width = 800
w_height = 800

# screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Block Game')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)

##########################################################################################
# Source of Pieces
PIECE_NAMES = pieces.PIECE_NAMES


def clear_rows(grid, fallen, score):
    i = 0
    for row in range(len(grid)):
        i += 1
        for col in range(len(grid[row])):
            lowest = min(fallen, key=lambda t: t[1])
            if BLACK not in grid[row]:
                del fallen[col, row]
                score += 1
                for x in range(i, lowest[1], -1):
                    if (col, x - 1) in fallen:
                        fallen[(col, x)] = fallen[(col, x - 1)]
                        del fallen[col, x - 1]
    return score


def draw_next_piece(pieces):
    pygame.draw.rect(screen, BLACK, (600, 130, 150, 575))
    pygame.draw.rect(screen, WHITE, (600, 130, 150, 575), 3)
    font = pygame.font.SysFont('franklingothicmedium', 30)
    next_text = font.render('Next Pieces', False, WHITE)
    screen.blit(next_text, (601, 90, 30, 30))
    i = -130
    for n in range(len(pieces)):
        shape = pieces[n].tetro[pieces[n].rotation % len(pieces[n].tetro)]
        i += 130
        for y, row in enumerate(shape):
            row = list(row)
            for x, col in enumerate(row):
                if col == 'o':
                    pygame.draw.rect(screen, pieces[n].color,
                                     (600 + x * BLOCK_SIZE, 140 + i + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f'{score}', True, WHITE)
    screen.blit(text, (550, 50))


def lose_game(fallen):
    for positions in fallen:
        x, y = positions
        if y < 1:
            return True


def hold(active_piece, next_pieces):
    held = active_piece
    active_piece = next_pieces.popleft()
    next_pieces.append(new_piece())
    return held, active_piece, next_pieces


def swap_hold(held, active_piece):
    held, active_piece = active_piece, held
    active_piece.x, active_piece.y = 5, 0
    return held, active_piece


def hold_display(held):
    shape = held.tetro[held.rotation % len(held.tetro)]

    for y, row in enumerate(shape):
        row = list(row)
        for x, col in enumerate(row):
            if col == 'o':
                pygame.draw.rect(screen, held.color,
                                 (50 + x * BLOCK_SIZE, 140 + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


def hold_box():
    pygame.draw.rect(screen, BLACK, (50, 130, 150, 150))
    pygame.draw.rect(screen, WHITE, (50, 130, 150, 150), 3)
    font = pygame.font.SysFont('franklingothicmedium', 30)
    held_text = font.render('Held', False, WHITE)
    screen.blit(held_text, (90, 90, 30, 30))


##########################################################################################
# Grid Management
def draw_lines():  # Uses pygame.draw.line function to draw the gridlines on the screen
    x = 250
    y = 100

    for _ in range(21):
        pygame.draw.line(screen, WHITE, (250, y), (w_width - 250, y))
        y += BLOCK_SIZE
    for _ in range(11):
        pygame.draw.line(screen, WHITE, (x, 100), (x, w_width - 100))
        x += BLOCK_SIZE


def update_grid(grid):
    x = 221
    y = 71
    for row in range(len(grid)):
        y += BLOCK_SIZE
        for col in range(len(grid[row])):
            pygame.draw.rect(screen, grid[row][col], (x + BLOCK_SIZE * (col + 1), y, BLOCK_SIZE - 1, BLOCK_SIZE - 1))
    pygame.display.update()


def create_grid(fallen={}):
    # (rgb), x, y, l, w
    grid = [[BLACK for _ in range(10)] for _ in range(20)]
    # for every row and column, check if it's in fallen dict; if so, add rgb value of fallen block to main grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col, row) in fallen:
                f = fallen[(col, row)]
                grid[row][col] = f
    return grid


def draw_shape(piece):
    pos = []
    shape = piece.tetro[piece.rotation % len(piece.tetro)]

    for y, row in enumerate(shape):
        row = list(row)
        for x, col in enumerate(row):
            if col == 'o':
                pos.append((piece.x + x, piece.y + y))
    for n, loc in enumerate(pos):
        pos[n] = (loc[0] - 2, loc[1] - 4)
    return pos


def new_piece():
    return pieces.Piece(5, 0, random.choice(PIECE_NAMES))


def empty_space(tetro, grid):
    valid_grid = [[(col, row) for col in range(10) if grid[row][col] == BLACK] for row in range(20)]
    valid_grid = [col for sublist in valid_grid for col in sublist]
    new_grid = draw_shape(tetro)
    for pos in new_grid:
        if pos not in valid_grid:
            if pos[1] > -1:
                return False
    return True


##########################################################################################
# Main Game loop
def game(timeLimit):
    # change screen color
    screen.fill(BLACK)
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    # new_piece()
    draw_lines()
    # pygame.mouse.set_visible(False)
    start_time = pygame.time.get_ticks()
    fallen = {}
    grid = create_grid(fallen)
    active_piece = new_piece()
    change_piece = False
    clock = pygame.time.Clock()
    active_time = 0
    min_speed = .2
    max_speed = .05
    active_fall_speed = 0.2
    score = 0
    next_pieces = []
    next_pieces = deque(next_pieces)
    held = None
    round_hold = False
    for i in range(4):
        next_pieces.append(new_piece())
    while True:
        hold_box()
        grid = create_grid(fallen)
        draw_next_piece(next_pieces)
        fall_interval = (max_speed - min_speed)/timeLimit
        minutes = "00"
        gameLimit = hud.create_hud(screen, start_time, timeLimit)
        if minutes != gameLimit:
           active_fall_speed += fall_interval
           minutes = gameLimit
        if gameLimit == -1:
            game_over(score)
        display_score(score)
        clock.tick(30)
        active_time += clock.get_rawtime()
        if held:
            hold_display(held)

        for event in pygame.event.get():
            # space bar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if held is None and not round_hold:
                        held, active_piece, next_pieces = hold(active_piece, next_pieces)
                        round_hold = True
                    elif not round_hold:
                        held, active_piece = swap_hold(held, active_piece)
                        round_hold = True
                if event.key == pygame.K_RIGHT:
                    active_piece.x += 1
                    if not (empty_space(active_piece, grid)):
                        active_piece.x -= 1
                if event.key == pygame.K_LEFT:
                    active_piece.x -= 1
                    if not (empty_space(active_piece, grid)):
                        active_piece.x += 1
                if event.key == pygame.K_DOWN:
                    active_piece.y += 1
                    if not (empty_space(active_piece, grid)):
                        active_piece.y -= 1
                if event.key == pygame.K_UP:
                    active_piece.rotation += 1 % len(active_piece.tetro)
                    if not (empty_space(active_piece, grid)):
                        active_piece.rotation -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        if active_time / 1000 >= active_fall_speed:
            active_time = 0
            active_piece.y += 1
            if not (empty_space(active_piece, grid)) and active_piece.y > 0:
                active_piece.y -= 1
                change_piece = True

        tetro_pos = draw_shape(active_piece)
        for n in range(len(tetro_pos)):
            x, y = tetro_pos[n]
            if y > -1:
                grid[y][x] = active_piece.color
        if change_piece:
            for pos in tetro_pos:
                n = (pos[0], pos[1])
                fallen[n] = active_piece.color
            round_hold = False
            active_piece = next_pieces.popleft()
            next_pieces.append(new_piece())
            change_piece = False
            score = clear_rows(grid, fallen, score)
        if lose_game(fallen):
            game_over(score)
        update_grid(grid)


##########################################################################################
# Game Over
def game_over(score):
    screen.fill(BLACK)
    font = pygame.font.SysFont('franklingothicmedium', 60)
    game_over_space = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 150, 160, 100))
    game_over_text = font.render('GAME OVER', False, WHITE)
    game_over_rect = game_over_text.get_rect(center=game_over_space.center)
    screen.blit(game_over_text, game_over_rect)
    score_space = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 250, 160, 100))
    score_text = font.render(f'FINAL SCORE: {score}', False, WHITE)
    score_rect = score_text.get_rect(center=score_space.center)
    screen.blit(score_text, score_rect)
    restart_button = pygame.draw.rect(screen, GREEN, pygame.Rect(320, 350, 160, 100))
    restart_text = font.render('Retry', False, BLACK)
    restart_rect = restart_text.get_rect(center=restart_button.center)
    screen.blit(restart_text, restart_rect)
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
                    main_menu.game_select()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
