########################################################################################################################
# Import statements
import pygame
import block_game

# CREATING HUD TO DISPLAY TIME AND SCORE

SIZE = block_game.SIZE

SCREEN = block_game.screen


def create_hud(screen, start_time):
    passed_time = 0
    game_clock = pygame.time.Clock()
    player_score = 0
    font = pygame.font.Font(None, int(SIZE * 0.0375))
    font_color = pygame.Color('white')
    passed_time = pygame.time.get_ticks() - start_time
    min_str = str(passed_time // 60000).zfill(2)
    sec_str = str((passed_time % 60000) // 1000).zfill(2)
    mill_str = str(passed_time % 1000).zfill(3)
    score_str = ('{min}:{sec}:{mil}'.format(min=min_str, sec=sec_str, mil=mill_str))
    text = font.render(str(score_str), True, font_color)
    screen.fill((0, 0, 0), (0, 0, 800, 100))
    screen.blit(text, (50, 50))
    game_clock.tick(25)
    score_display = font.render("CURRENT SCORE: ", True, font_color)  # ADD SCORE FUNCTION
    screen.blit(score_display, (int(SIZE * 0.375), int(SIZE * 0.0625)))


def limit5(screen, start_time):
    passed_time = 0
    game_clock = pygame.time.Clock()
    player_score = 0
    font = pygame.font.Font(None, int(SIZE * (30 / 800)))
    font_color = pygame.Color('white')
    passed_time = pygame.time.get_ticks() - start_time
    min_str = str(passed_time // 60000).zfill(2)
    sec_str = str((passed_time % 60000) // 1000).zfill(2)
    mill_str = str(passed_time % 1000).zfill(3)
    score_str = ('{min}:{sec}:{mil}'.format(min=min_str, sec=sec_str, mil=mill_str))
    if min_str >= "05":
        score_str = "ASSY"
    text = font.render(str(score_str), True, font_color)
    screen.fill((0, 0, 0), (0, 0, 800, 100))
    screen.blit(text, (50, 50))
    game_clock.tick(25)
    game_mode_display = font.render("5 Minute Time Limit", False, font_color)
    screen.blit(game_mode_display, (250, 50))
    score_display = font.render(f"CURRENT SCORE: ", True, font_color)  # ADD SCORE FUNCTION
    screen.blit(score_display, (500, 50))
    return score_str
