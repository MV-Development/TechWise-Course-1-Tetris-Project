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

def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f'{score}', True, WHITE)
    screen.blit(text, (550, 50))

##########################################################################################
# Grid Management
def draw_lines():  # Uses pygame.draw.line function to draw the gridlines on the screen
    x = 250
    y = 100

    pygame.draw.line(screen, WHITE, (250, y), (w_width - 250, y))
    pygame.draw.line(screen, WHITE, (250, 700), (w_width - 250, 700))

    pygame.draw.line(screen, WHITE, (x, 100), (x, w_width - 100))
    pygame.draw.line(screen, WHITE, (550, 100), (550, w_width - 100))


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
            if BLACK not in grid[row]:
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
def game():
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
    next_piece = new_piece()
    change_piece = False
    clock = pygame.time.Clock()
    active_time = 0
    active_fall_speed = 0.1
    score = 0
    while True:
        grid = create_grid(fallen)
        hud.create_hud(screen, start_time)
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
            game_over(score)
        update_grid(grid)


##########################################################################################
# Main Menu Function
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
                    game_select()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


# def game5():
#     # change screen color
#     screen.fill(BLACK)
#     # draw_grid()
#     # pygame.mixer.music.stop()
#     # pygame.mixer.music.load('endlessmotion.wav')
#     # pygame.mixer.music.play(-1)
#     # new_piece()
#     draw_lines()
#     pygame.mouse.set_visible(False)
#     start_time = pygame.time.get_ticks()
#     clock = pygame.time.Clock
#     while True:
#         theTime = hud.limit5(screen, start_time)
#         if theTime == "ASSY":
#             game_over()
#         ###ATTEMPT AT GAME CLOCK
#         pygame.display.update()
#         for event in pygame.event.get():
#             # spacebar quits game
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     pygame.quit()
#                     sys.exit(0)
#
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit(0)


def main_menu():
    # main menu
    tetris_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 130, 160, 100))

    # start game button
    start_button = pygame.draw.rect(screen, (118, 238, 198), pygame.Rect(320, 350, 160, 100))

    # quit game button
    quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

    # text on buttons
    tetris_font = pygame.font.SysFont('javanesetext', 100)
    tetris_text = tetris_font.render('TETRIS', False, WHITE)
    tetris_rect = tetris_text.get_rect(center=tetris_button.center)
    screen.blit(tetris_text, tetris_rect)
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
                    game()
                elif 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    game()
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    game()
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


main_menu()
