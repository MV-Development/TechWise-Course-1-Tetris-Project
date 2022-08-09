########################################################################################################################
# Import statements
import pygame

########################################################################################################################
# Colors and Corresponding RGB Values

RED = (255, 0, 0)
GREEN = (0, 255, 0),
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


########################################################################################################################
# Menu Button Class
class MenuButton:
    # Constructor Method
    def __init__(self, surface, background_color, start_x, start_y, display_size, text, text_color, text_font,
                 text_size):
        self.surface = surface
        self.color = background_color
        self.start_x = start_x
        self.start_y = start_y
        self.length = display_size * 0.2
        self.width = display_size * 0.125
        self.text = text
        self.text_color = text_color
        self.text_style = pygame.font.SysFont(text_font, text_size)

    def draw_button(self):
        background = pygame.draw.rect(self.surface, self.color,
                                      pygame.Rect(self.start_x, self.start_y, self.length, self.width))
        text_font = self.text_style
        text = text_font.render(self.text, False, self.text_color)
        button = text.get_rect(center=background.center)
        self.surface.blit(text, background)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        return self.start_x <= mouse[0] <= self.start_x + self.length and self.start_y <= mouse[
            1] <= self.start_y + self.width
