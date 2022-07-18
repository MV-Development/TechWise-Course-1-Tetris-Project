import pygame.time


def create_hud(screen):
    passed_time = 0
    gameClock = pygame.time.Clock()
    playerScore = 0
    font = pygame.font.Font(None, 20)
    font_color = pygame.Color('white')
    text = font.render(str(passed_time / 1000), True, font_color)
    screen.blit(text, (50, 50))
    pygame.display.flip()