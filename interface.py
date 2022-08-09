##########################################################################################
# Import statements
import pygame
from pygame import font

####################################################################################
# Colors and Corresponding RGB Values


RED = (255, 0, 0)
GREEN = (0, 255, 0),
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()


# limit5_button = pygame.draw.rect(screen, colors.RED, pygame.Rect(320, 250, 160, 100))

# limit5_text = pygame.font.render('5 Min Limit', False, colors.BLACK)


# limit5_rect = limit5_text.get_rect(center=limit5_button.center)


####################################################################################
# Menu Button Class
class MenuButton:
    # Constructor Method
    def __init__(self, surface, color, start_x, start_y, display_size, text, text_font, text_size):
        self.surface = surface
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.length = display_size * 0.2
        self.width = display_size * 0.125
        self.text = text
        self.text_style = pygame.font.SysFont(text_font, text_size)

    def draw_button(self):
        background = pygame.draw.rect(self.surface, self.color,
                                      pygame.Rect(self.start_x, self.start_y, self.length, self.width))
        text_font = self.text_style
        text = font.render(self.text, False, BLACK)
        button = text.get_rect(center=background.center)
        self.surface.blit(text, background)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        return self.start_x <= mouse[0] <= self.start_x + self.length and self.start_y <= mouse[
            1] <= self.start_y + self.width
