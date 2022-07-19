import pygame.time

<<<<<<< HEAD
#CREATING HUD TO DISPLAY TIME AND SCORE
def create_hud():
    gameClock = pygame.time.Clock()
    timeStart = pygame.time.get_ticks()
    font = pygame.font.Font(None, 20)
    color = pygame.Color('white')
    display = font.render(str(round(timeStart / 1000, 2)), True, color)
    screen.blit(display, (50, 50))
    pg.display.flip()
    clock.tick(1000)
=======

def create_hud(screen):
    passed_time = 0
    gameClock = pygame.time.Clock()
    playerScore = 0
    font = pygame.font.Font(None, 20)
    font_color = pygame.Color('white')
    text = font.render(str(passed_time / 1000), True, font_color)
    screen.blit(text, (50, 50))
    pygame.display.flip()
>>>>>>> origin/main
