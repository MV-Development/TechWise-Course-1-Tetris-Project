########################################################################################################################
# Import statements
import sys
import pygame
import random
import block_game
import interface
import hud
import pieces
import game_over

SCREEN = block_game.screen
SIZE = block_game.SIZE
PIECE_NAMES = pieces.PIECE_NAMES
########################################################################################################################
# Global Variables
BLOCK_SIZE = int(SIZE * 0.0375)


########################################################################################################################
# Next Piece Window
def draw_next_piece(piece):
    pygame.draw.rect(SCREEN, interface.BLACK,
                     (int(SIZE * 0.75), int(SIZE * 0.3125), int(SIZE * 0.1875), int(SIZE * 0.1875)))
    pygame.draw.rect(SCREEN, interface.WHITE,
                     (int(SIZE * 0.75), int(SIZE * 0.3125), int(SIZE * 0.1875), int(SIZE * 0.1875)), 3)
    font = pygame.font.SysFont('franklingothicmedium', int(BLOCK_SIZE))
    next_text = font.render('Next Piece ', False, interface.WHITE)
    SCREEN.blit(next_text,
                (int(SIZE * (601 / 800)), int(SIZE * (200 / 800)), int(SIZE * (30 / 800)), int(SIZE * (30 / 800))))
    shape = piece.tetro[piece.rotation % len(piece.tetro)]

    for y, row in enumerate(shape):
        row = list(row)
        for x, col in enumerate(row):
            if col == 'o':
                pygame.draw.rect(SCREEN, piece.color,
                                 (int(SIZE * 0.75) + x * BLOCK_SIZE, int(SIZE * (260 / 800) + y * BLOCK_SIZE),
                                  BLOCK_SIZE, BLOCK_SIZE), 0)


########################################################################################################################
# Score Display
def display_score(score):
    font = pygame.font.Font(None, int(BLOCK_SIZE))
    text = font.render(f'{score}', True, interface.WHITE)
    SCREEN.blit(text, (SIZE * (550 / 800), SIZE * 50 / 800))


########################################################################################################################
# Game Logic
def lose_game(fallen):
    for positions in fallen:
        x, y = positions
        if y < 1:
            return True


def clear_rows(grid, fallen, score):
    i = 0
    for row in range(len(grid)):
        i += 1
        for col in range(len(grid[row])):
            lowest = min(fallen, key=lambda t: t[1])
            if interface.BLACK not in grid[row]:
                del fallen[col, row]
                score += 1
                for x in range(i, lowest[1], -1):
                    if (col, x - 1) in fallen:
                        fallen[(col, x)] = fallen[(col, x - 1)]
                        del fallen[col, x - 1]
    return score


########################################################################################################################
# Grid Management
def draw_lines():  # Uses pygame.draw.line function to draw the gridlines on the SCREEN
    start_x = int(SIZE * 0.3125)
    start_y = int(SIZE * 0.125)
    height = 20 * BLOCK_SIZE
    width = 10 * BLOCK_SIZE

    for row in range(21):
        pygame.draw.line(SCREEN, interface.WHITE, (start_x, start_y), (start_x + width, start_y),
                         int(SIZE * (5 / 800)))
        start_y += BLOCK_SIZE
    start_y = int(SIZE * 0.125)
    for column in range(11):
        pygame.draw.line(SCREEN, interface.WHITE, (start_x, start_y), (start_x, start_y + height),
                         int(SIZE * (5 / 800)))
        start_x += BLOCK_SIZE


def update_grid(grid):
    x = int(SIZE * (221 / 800))
    y = int(SIZE * (71 / 800))
    for row in range(len(grid)):
        y += BLOCK_SIZE
        for col in range(len(grid[row])):
            pygame.draw.rect(SCREEN, grid[row][col], (x + BLOCK_SIZE * (col + 1), y, BLOCK_SIZE - 1, BLOCK_SIZE - 1))
    pygame.display.update()


def create_grid(fallen={}):
    # (rgb), x, y, l, w
    grid = [[interface.BLACK for _ in range(10)] for _ in range(20)]
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
    valid_grid = [[(col, row) for col in range(10) if grid[row][col] == interface.BLACK] for row in range(20)]
    valid_grid = [col for sublist in valid_grid for col in sublist]
    new_grid = draw_shape(tetro)
    for pos in new_grid:
        if pos not in valid_grid:
            if pos[1] > -1:
                return False
    return True


########################################################################################################################
# Main Game loop
def game():
    SCREEN.fill(interface.BLACK)
    start_time = pygame.time.get_ticks()
    fallen = {}
    active_piece = new_piece()
    next_piece = new_piece()
    change_piece = False
    clock = pygame.time.Clock()
    active_time = 0
    active_fall_speed = 0.1
    score = 0
    draw_lines()
    while True:
        grid = create_grid(fallen)
        draw_next_piece(next_piece)
        hud.create_hud(SCREEN, start_time)
        display_score(score)
        clock.tick(30)
        active_time += clock.get_rawtime()

        for event in pygame.event.get():
            # space bar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
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

            active_piece = next_piece
            next_piece = new_piece()
            change_piece = False
            score = clear_rows(grid, fallen, score)
        if lose_game(fallen):
            game_over.game_over(score)
        update_grid(grid)
