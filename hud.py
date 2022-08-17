import pygame.time


# CREATING HUD TO DISPLAY TIME AND SCORE

def create_hud(screen, start_time, time_limit):
    passed_time = 0
    game_clock = pygame.time.Clock()
    player_score = 0
    font = pygame.font.Font(None, 30)
    font_color = pygame.Color('white')
    passed_time = pygame.time.get_ticks() - start_time
    min_str = str(passed_time // 60000).zfill(2)
    sec_str = str((passed_time % 60000) // 1000).zfill(2)
    mill_str = str(passed_time % 1000).zfill(3)
    score_str = ('{min}:{sec}:{mil}'.format(min=min_str, sec=sec_str, mil=mill_str))
    if int(min_str) >= time_limit:
        min_str = -1
    text = font.render(str(score_str), True, font_color)
    screen.fill((0, 0, 0), (0, 0, 800, 100))
    screen.blit(text, (50, 50))
    game_clock.tick(25)
    score_display = font.render("CURRENT SCORE: ", True, font_color)  # ADD SCORE FUNCTION
    screen.blit(score_display, (300, 50))
    return min_str
