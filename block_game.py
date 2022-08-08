##########################################################################################
# Import statements
import pygame
import random
import interface
import pieces
import main_menu

##########################################################################################
# Initialization

pygame.init()
pygame.display.init()
pygame.font.init()

##########################################################################################
# Display setup

SIZE = pygame.display.list_modes()[0][1] / 2
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('''Block Game''')
pygame.display.set_icon(pygame.image.load('icon.png'))

pygame.mouse.set_visible(True)

##########################################################################################
# Global Variables
BLOCK_SIZE = SIZE * 0.0375
PIECE_NAMES = pieces.PIECE_NAMES


def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f'{score}', True, interface.WHITE)
    screen.blit(text, (550, 50))


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


##########################################################################################
# Initializing falling block
# Takes falling block object,
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


main_menu.menu(SIZE, BLOCK_SIZE)
