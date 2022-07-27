import pygame
import random
import sys
import os
import hud

WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
BLOCK_SIZE = 30
NEW_X = 371
NEW_Y = 101

# window variables
w_width = 800
w_height = 800

# grid sides
GRID_LEFT = 251
GRID_TOP = 100
GRID_BOTTOM = 700
GRID_RIGHT = 550

# screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Tetris')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)

COLORS = [BLUE, RED, GREEN]
TETROS = ['O.png', 'L.png']

def fallen(tetro):
    return tetro_bottom(tetro) >= GRID_BOTTOM

def tetro_bottom(tetro):
    return tetro.rect[1] + tetro.rect[3]

def new_piece():
    choice = random.choice(TETROS)
    sprite_path = f'sprites/{choice}'
    sprite_image = pygame.image.load(sprite_path).convert_alpha()
    return sprite_image


class Piece(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        # creating sprite and putting it inside rect to control
        self.image = new_piece()
        self.rect = self.image.get_rect()

        # where new piece spawns
        self.rect[0] = NEW_X
        self.rect[1] = NEW_Y

        # creating collision mask over sprite
        self.mask = pygame.mask.from_surface(self.image)

    # if block left is greater than the left side, move left
    def move_left(self):
        if self.rect[0] > GRID_LEFT:
            self.rect[0] -= BLOCK_SIZE

    # if block right is less than right side, move right
    def move_right(self):
        if self.rect[0] + self.rect[2] < GRID_RIGHT:
            self.rect[0] += BLOCK_SIZE

    def move_down(self):

        return 5

    def fall(self, fall_speed):
        if self.rect[1] + self.rect[3] < GRID_BOTTOM:
            self.rect[1] += fall_speed

    def resety(self, fall_speed):
        self.rect[1] -= fall_speed

    def resetx(self, size):
        self.rect[0] += size

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, -90)
        new_rect = self.image.get_rect(center=self.rect.center)
        self.rect = new_rect
        self.mask = pygame.mask.from_surface(self.image)



def draw_lines():
    x = 250
    y = 100

    for i in range(21):
        pygame.draw.line(screen, WHITE, (250, y), (w_width - 250, y))
        y += BLOCK_SIZE
    for j in range(11):
        pygame.draw.line(screen, WHITE, (x, 100), (x, w_width - 100))
        x += BLOCK_SIZE


pygame.init()
pygame.font.init()


def game():
    # change screen color
    screen.fill(BLACK)
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load('endlessmotion.wav')
    # pygame.mixer.music.play(-1)
    draw_lines()
    pygame.mouse.set_visible(False)
    start_time = pygame.time.get_ticks()
    active_tetro = Piece()
    active_group = pygame.sprite.GroupSingle()
    active_group.add(active_tetro)
    fallen_tetros = pygame.sprite.Group()
    clock = pygame.time.Clock()
    fall_speed = 1
    while True:
        clock.tick(30)
        hud.create_hud(screen, start_time)
        ###ATTEMPT AT GAME CLOCK

        for event in pygame.event.get():
            # spacebar quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_LEFT:
                    active_group.sprite.move_left()
                if event.key == pygame.K_RIGHT:
                    active_group.sprite.move_right()
                if event.key == pygame.K_DOWN:
                    if fall_speed == 1:
                        fall_speed = 5
                    else:
                        fall_speed = 1
                if event.key == pygame.K_UP:
                    active_group.sprite.rotate()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(BLACK, rect=(251,101,551,701))
        draw_lines()
        active_group.sprite.fall(fall_speed)

        if active_group.sprite.rect.midbottom[1] > GRID_BOTTOM:
            active_group.sprite.resety(active_group.sprite.rect.midbottom[1] - GRID_BOTTOM)
        if active_group.sprite.rect.midleft[0] < GRID_LEFT:
            active_group.sprite.resetx(GRID_LEFT - active_group.sprite.rect.midleft[0])
        if active_group.sprite.rect.midright[0] > GRID_RIGHT:
            active_group.sprite.resetx(GRID_RIGHT - active_group.sprite.rect.midright[0])


        if pygame.sprite.spritecollideany(active_group.sprite, fallen_tetros, pygame.sprite.collide_mask) or fallen(active_group.sprite):
            fallen_tetros.add(active_group.sprite)
            active_group.remove(active_group.sprite)
            active_group.add(Piece())


        active_group.draw(screen)
        fallen_tetros.draw(screen)
        pygame.display.update()


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


# def drop_piece():
#   while not piece.y_position + 1 == BLACK and piece.y_position < grid_height:
#       piece.y_position += 1


# def draw_board(game_pieces):
#   set background to black
#   draw squares by color
#       empty squares are black
#   draw falling block grid
#       empty squares have no color
#   draw gridlines


# def collision_detection(piece_position):
#   check color of adjacent block


# def rotate(piece_orientation):
#   on event up key down rotate
#   change surrounding colors
