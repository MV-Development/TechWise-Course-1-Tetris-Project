##########################################################################################
# Import statements
import pygame

####################################################################################
# Colors and Corresponding RGB Values

RED = (255, 0, 0)
GREEN = (0, 255, 0),
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont('franklingothicmedium', 28)


# limit5_button = pygame.draw.rect(screen, colors.RED, pygame.Rect(320, 250, 160, 100))

# limit5_text = pygame.font.render('5 Min Limit', False, colors.BLACK)


# limit5_rect = limit5_text.get_rect(center=limit5_button.center)


####################################################################################
# Menu Button Class
class MenuButton:
    # Constructor Method
    def __init__(self, surface, color, start_x, start_y, display_size, text):
        self.surface = surface
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.length = display_size * 0.2
        self.width = display_size * 0.125
        self.text = text

    def draw_button(self):
        background = pygame.draw.rect(self.surface, RED,
                                      pygame.Rect(self.start_x, self.start_y, self.length, self.width))
        text = font.render(self.text, False, BLACK)
        button = text.get_rect(center=background.center)
        self.surface.blit(text, background)
