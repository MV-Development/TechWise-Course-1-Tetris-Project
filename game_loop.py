##########################################################################################
# Import statements
import pygame
import random
import sys
import hud
import pieces
import main_menu
from collections import deque
import pickle

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
# High Scores
d = shelve.open('highscores.txt')



# Source of Pieces
PIECE_NAMES = pieces.PIECE_NAMES

def scoring(time_limit, difficulty):
    scores = {}

def clear_rows(grid, fallen, score):
    i = 0
    add_score = 0
    for row in range(len(grid)):
        i += 1
        for col in range(len(grid[row])):
            lowest = min(fallen, key=lambda t: t[1])
            if BLACK not in grid[row]:
                del fallen[col, row]
                add_score += 1
                for x in range(i, lowest[1], -1):
                    if (col, x - 1) in fallen:
                        fallen[(col, x)] = fallen[(col, x - 1)]
                        del fallen[col, x - 1]
    if add_score == 10:
        add_score = 40
    elif add_score == 20:
        add_score = 100
    elif add_score == 30:
        add_score = 300
    elif add_score == 40:
        add_score = 1200
    return score + add_score


def draw_next_piece(pieces):
    pygame.draw.rect(screen, BLACK, (600, 130, 150, 575))
    pygame.draw.rect(screen, WHITE, (600, 130, 150, 575), 3)
    font = pygame.font.Font('font2.ttf', 25)
    next_text = font.render('Next Pieces', False, WHITE)
    screen.blit(next_text, (608, 95, 30, 30))
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
    font = pygame.font.Font('font2.ttf', 28)
    held_text = font.render('Held', False, WHITE)
    screen.blit(held_text, (95, 93, 30, 30))


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


def instant_drop(tetro, grid):
    while empty_space(tetro, grid) and tetro.y < len(grid) + 1:
        tetro.y += 1
    if not (empty_space(tetro, grid)):
        tetro.y -= 1


def empty_space(tetro, grid):
    valid_grid = [[(col, row) for col in range(10) if grid[row][col] == BLACK] for row in range(20)]
    valid_grid = [col for sublist in valid_grid for col in sublist]
    new_grid = draw_shape(tetro)
    for pos in new_grid:
        if pos not in valid_grid:
            if pos[1] > -1:
                return False
    return True


def get_min_speed(difficulty):
    if difficulty == 1:
        return .28
    elif difficulty == 2:
        return .24
    else:
        return .2


def get_max_speed(difficulty):
    if difficulty == 1:
        return .12
    elif difficulty == 2:
        return .08
    else:
        return .04


##########################################################################################
# Main Game loop

def text_maker1(text, size, text_color, rect_color, left, top, width, height):
    button = pygame.draw.rect(screen, rect_color, pygame.Rect(left, top, width, height))
    font = pygame.font.Font("font1.ttf", size)
    text_surface = font.render(text, False, text_color)
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)


def text_maker2(text, size, text_color, rect_color, left, top, width, height):
    button = pygame.draw.rect(screen, rect_color, pygame.Rect(left, top, width, height))
    font = pygame.font.Font("font2.ttf", size)
    text_surface = font.render(text, False, text_color)
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)


def game(timeLimit, difficulty):
    # change screen color
    screen.fill(BLACK)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('game_song.mp3')
    pygame.mixer.music.play(-1)

    # quit button
    text_maker2('Quit', 50, BLACK, RED, 600, 720, 150, 60)

    # new_piece()
    draw_lines()
    start_time = pygame.time.get_ticks()
    fallen = {}
    grid = create_grid(fallen)
    active_piece = new_piece()
    change_piece = False
    clock = pygame.time.Clock()
    active_time = 0
    min_speed = get_min_speed(difficulty)
    max_speed = get_max_speed(difficulty)
    active_fall_speed = min_speed
    score = 0
    minutes = "00"
    next_pieces = []
    next_pieces = deque(next_pieces)
    held = None
    round_hold = False
    print(scores)
    for i in range(4):
        next_pieces.append(new_piece())
    while True:
        hold_box()
        grid = create_grid(fallen)
        draw_next_piece(next_pieces)
        fall_interval = (min_speed - max_speed) / timeLimit
        gameLimit = hud.create_hud(screen, start_time, timeLimit)
        if minutes != gameLimit:
            active_fall_speed -= fall_interval
            minutes = str(gameLimit)
        if gameLimit == -1:
            game_over(score)
        display_score(score)
        clock.tick(30)
        active_time += clock.get_rawtime()
        if held:
            hold_display(held)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 600 <= mouse[0] <= 750 and 720 <= mouse[1] <= 820:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
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
                if event.key == pygame.K_SPACE:
                    instant_drop(active_piece, grid)

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
            scoring(timeLimit, difficulty)
            game_over(score)
        update_grid(grid)


##########################################################################################
# Game Over
def game_over(score):
    screen.fill(BLACK)
    text_maker1('GAME OVER', 35, WHITE, BLACK, 320, 150, 160, 100)
    text_maker1(f'FINAL SCORE: {score}', 35, WHITE, BLACK, 320, 250, 160, 100)

    text_maker2('Retry', 50, BLACK, (191, 239, 255), 320, 350, 160, 100)
    text_maker2('Quit', 50, BLACK, RED, 320, 550, 160, 100)

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
