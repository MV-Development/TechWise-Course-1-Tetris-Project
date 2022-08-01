##########################################################################################
# Import statements
import pygame
import random
import sys
import hud
import pieces

##########################################################################################
# Initialization
pygame.init()
pygame.font.init()

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
pygame.display.set_caption('Tetris')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)
PIECE_NAMES = pieces.PIECE_NAMES


##########################################################################################
# Grid Management
def draw_lines():  # Uses pygame.draw.line function to draw the gridlines on the screen
    x = 250
    y = 100

    for i in range(21):
        pygame.draw.line(screen, WHITE, (250, y), (w_width - 250, y))
        y += BLOCK_SIZE
    for j in range(11):
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
    return pieces.Piece(3, 0, random.choice(PIECE_NAMES))


def empty_space(tetro, grid):
    valid_grid = [[(col, row) for col in range(10) if grid[row][col] == BLACK] for row in range(20)]
    valid_grid = [pos for sublist in valid_grid for pos in sublist]
    new_grid = draw_shape(tetro)
    for pos in new_grid:
        if pos not in valid_grid:
            if pos[1] > -1:
                return False
    return True


##########################################################################################
# Main Game loop
def game():
    # change screen color
    screen.fill(BLACK)
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    # new_piece()
    draw_lines()
    pygame.mouse.set_visible(False)
    start_time = pygame.time.get_ticks()
    fallen = {}
    grid = create_grid(fallen)
    active_piece = new_piece()
    next_piece = new_piece()
    change_piece = True
    update_grid(grid)
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.2
    while True:
        hud.create_hud(screen, start_time)  # ATTEMPT AT GAME CLOCK
        grid = create_grid(fallen)
        fall_time += clock.get_rawtime()
        clock.tick()
        pygame.display.update()
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
                if event.key == pygame.K_UP:
                    active_piece.rotation += 1
                    if not (empty_space(active_piece, grid)):
                        active_piece.rotation -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

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
        update_grid(grid)


##########################################################################################
# Main Menu Function
def main_menu():
    # main menu
    # start game button
    start_button = pygame.draw.rect(screen, BLUE, pygame.Rect(320, 350, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    font = pygame.font.SysFont('Arial', 30)
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
    #######################################################################################
    # Take user input
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


##########################################################################################
# Begin Game, Good Luck :)
main_menu()
