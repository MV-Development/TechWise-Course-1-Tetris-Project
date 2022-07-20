import pygame.time


# CREATING HUD TO DISPLAY TIME AND SCORE

def create_hud(screen, start_time):
    passed_time = 0
    game_clock = pygame.time.Clock()
    player_score = 0
    font = pygame.font.Font(None, 20)
    font_color = pygame.Color('white')
    passed_time = pygame.time.get_ticks() - start_time
    sec_str = str((passed_time%60000)/1000).zfill(2)
    text = font.render(str(sec_str), True, font_color)
    screen.fill((0,0,0), (0, 0, 800, 100))
    screen.blit(text, (50, 50))
    game_clock.tick(25)
    scoreDisplay = font.render("CURRENT SCORE: ", True, font_color)  # ADD SCORE FUNCTION
    screen.blit(scoreDisplay, (600, 50))
