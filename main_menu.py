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

class LShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(LShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Lshape.png'))
        self.images.append(pygame.image.load('Images/Lshape1.png'))
        self.images.append(pygame.image.load('Images/Lshape2.png'))
        self.images.append(pygame.image.load('Images/Lshape3.png'))
        self.images.append(pygame.image.load('Images/Lshape4.png'))
        self.images.append(pygame.image.load('Images/Lshape5.png'))
        self.images.append(pygame.image.load('Images/Lshape6.png'))
        self.images.append(pygame.image.load('Images/Lshape7.png'))
        self.images.append(pygame.image.load('Images/Lshape8.png'))
        self.images.append(pygame.image.load('Images/Lshape9.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(500, 500, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class ZShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(ZShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Zshape.png'))
        self.images.append(pygame.image.load('Images/Zshape1.png'))
        self.images.append(pygame.image.load('Images/Zshape2.png'))
        self.images.append(pygame.image.load('Images/Zshape3.png'))
        self.images.append(pygame.image.load('Images/Zshape4.png'))
        self.images.append(pygame.image.load('Images/Zshape5.png'))
        self.images.append(pygame.image.load('Images/Zshape6.png'))
        self.images.append(pygame.image.load('Images/Zshape7.png'))
        self.images.append(pygame.image.load('Images/Zshape8.png'))
        self.images.append(pygame.image.load('Images/Zshape8.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(500, 200, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class TShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Tshape.png'))
        self.images.append(pygame.image.load('Images/Tshape1.png'))
        self.images.append(pygame.image.load('Images/Tshape2.png'))
        self.images.append(pygame.image.load('Images/Tshape3.png'))
        self.images.append(pygame.image.load('Images/Tshape4.png'))
        self.images.append(pygame.image.load('Images/Tshape5.png'))
        self.images.append(pygame.image.load('Images/Tshape6.png'))
        self.images.append(pygame.image.load('Images/Tshape7.png'))
        self.images.append(pygame.image.load('Images/Tshape8.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 500, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class OShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(OShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Oshape.png'))
        self.images.append(pygame.image.load('Images/Oshape1.png'))
        self.images.append(pygame.image.load('Images/Oshape2.png'))
        self.images.append(pygame.image.load('Images/Oshape3.png'))
        self.images.append(pygame.image.load('Images/Oshape4.png'))
        self.images.append(pygame.image.load('Images/Oshape5.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 200, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Block Game')
program_icon = pygame.image.load('icon.png')
pygame.display.set_icon(program_icon)

my_sprite2 = LShapeSprite()
my_group2 = pygame.sprite.Group(my_sprite2)
my_sprite3 = OShapeSprite()
my_group3 = pygame.sprite.Group(my_sprite3)
my_sprite4 = TShapeSprite()
my_group4 = pygame.sprite.Group(my_sprite4)
my_sprite5 = ZShapeSprite()
my_group5 = pygame.sprite.Group(my_sprite5)
clock = pygame.time.Clock()

color_speed = 1
color_direction = [-1, 1, -1]
default_color = [140, 120, 230]
color_direction1 = [-1, 1, 1]
default_color1 = [120, 140, 240]

def color_change(color, direction):
    for i in range(len(color)):
        color[i] += color_speed * direction[i]
        # reversing the direction of the intensity
        if color[i] >= 255 or color[i] <= 0:
            direction[i] *= -1

def menu():
    # add menu music
    pygame.mixer.init()
    pygame.mixer.music.load('menu_song.mp3')
    pygame.mixer.music.play(-1)

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

        screen.fill(BLACK)
        my_group2.draw(screen)
        my_group2.update()
        my_group3.draw(screen)
        my_group3.update()
        my_group4.draw(screen)
        my_group4.update()
        my_group5.draw(screen)
        my_group5.update()
        clock.tick(6)

        # title game button & text
        title_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 100, 160, 100))
        title_font = pygame.font.Font("font1.ttf", 90)
        title_text = title_font.render('BLOCK', False, default_color)
        title_rect = title_text.get_rect(center=title_button.center)
        screen.blit(title_text, title_rect)

        title1_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 180, 160, 100))
        title1_font = pygame.font.Font("font1.ttf", 85)
        title1_text = title1_font.render('GAME', False, default_color1)
        title1_rect = title1_text.get_rect(center=title1_button.center)
        screen.blit(title1_text, title1_rect)

        color_change(default_color, color_direction)
        color_change(default_color1, color_direction1)

        # start game button
        start_button = pygame.draw.rect(screen, (191,239,255), pygame.Rect(320, 350, 160, 100))

        # quit game button
        quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

        # text on buttons
        font = pygame.font.Font("font2.ttf", 50)
        start_text = font.render('Start', False, BLACK)
        start_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rect)
        quit_text = font.render('Quit', False, BLACK)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_rect)

        # add everything to screen
        pygame.mouse.set_visible(True)
        pygame.display.flip()


def game_select():
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    diff_select(10)
                elif 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    diff_select(5)
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    diff_select(15)
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(BLACK)
        my_group2.draw(screen)
        my_group2.update()
        my_group3.draw(screen)
        my_group3.update()
        my_group4.draw(screen)
        my_group4.update()
        my_group5.draw(screen)
        my_group5.update()
        clock.tick(6)

        # time limit buttons
        time_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 100, 180, 50))
        time_font = pygame.font.Font("font1.ttf", 40)
        time_text = time_font.render('CHOOSE TIME LIMIT', False, WHITE)
        time_rect = time_text.get_rect(center=time_button.center)
        screen.blit(time_text, time_rect)

        limit5_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 250, 160, 100))
        limit10_button = pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(320, 350, 160, 100))
        limit15_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 450, 160, 100))

        # quit game button
        quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

        # text on buttons
        font = pygame.font.Font("font2.ttf", 25)
        font_title = pygame.font.Font("font2.ttf", 60)

        limit5_text = font.render('5 Minutes', False, BLACK)
        limit10_text = font.render('10 Minutes', False, BLACK)
        limit15_text = font.render('15 Minutes', False, BLACK)
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


def diff_select(timeLimit):
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    game_loop.game(timeLimit,2)
                elif 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    game_loop.game(timeLimit,1)
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    game_loop.game(timeLimit,3)
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(BLACK)
        my_group2.draw(screen)
        my_group2.update()
        my_group3.draw(screen)
        my_group3.update()
        my_group4.draw(screen)
        my_group4.update()
        my_group5.draw(screen)
        my_group5.update()
        clock.tick(6)

        # difficulty buttons
        difficulty_button = pygame.draw.rect(screen, BLACK, pygame.Rect(320, 100, 180, 50))
        difficulty_font = pygame.font.Font("font1.ttf", 30)
        difficulty_text = difficulty_font.render('CHOOSE DIFFICULTY LEVEL', False, WHITE)
        difficulty_rect = difficulty_text.get_rect(center=difficulty_button.center)
        screen.blit(difficulty_text, difficulty_rect)
        level1_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 250, 160, 100))
        level2_button = pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(320, 350, 160, 100))
        level3_button = pygame.draw.rect(screen, (141, 238, 238), pygame.Rect(320, 450, 160, 100))

        # quit game button
        quit_button = pygame.draw.rect(screen, RED, pygame.Rect(320, 550, 160, 100))

        # text on buttons
        font = pygame.font.Font("font2.ttf", 32)
        font_title = pygame.font.Font("font2.ttf", 60)

        level1_text = font.render('EASY', False, BLACK)
        level2_text = font.render('NORMAL', False, BLACK)
        level3_text = font.render('HARD', False, BLACK)
        level1_rect = level1_text.get_rect(center=level1_button.center)
        level2_rect = level2_text.get_rect(center=level2_button.center)
        level3_rect = level3_text.get_rect(center=level3_button.center)
        screen.blit(level1_text, level1_rect)
        screen.blit(level2_text, level2_rect)
        screen.blit(level3_text, level3_rect)
        quit_text = font.render('Quit', False, BLACK)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_rect)
        pygame.mouse.set_visible(True)
        pygame.display.flip()
