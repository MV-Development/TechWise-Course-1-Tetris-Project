import pygame.time

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