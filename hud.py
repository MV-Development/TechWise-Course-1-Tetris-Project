import pygame.time

#CREATING HUD TO DISPLAY TIME AND SCORE

def create_hud(screen):
    passed_time = 0
    gameClock = pygame.time.Clock()
    playerScore = 0
    font = pygame.font.Font(None, 20)
    font_color = pygame.Color('white')
    start_time = pygame.time.get_ticks()
    passed_time = pygame.time.get_ticks() - start_time
    text = font.render(str(passed_time / 1000), True, font_color)
    screen.blit(text, (50, 50))
    pygame.display.flip()
    gameClock.tick(1000)
    scoreDisplay = font.render("CURRENT SCORE: ",True, font_color) #ADD SCORE FUNCTION
    screen.blit(scoreDisplay,(600,50))