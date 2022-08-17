def diff_select(timeLimit):
    while True:
        for event in pygame.event.get():
            # on event click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse = pygame.mouse.get_pos()
                if 320 <= mouse[0] <= 480 and 250 <= mouse[1] <= 350:
                    game_loop.game(timeLimit, 1)
                elif 320 <= mouse[0] <= 480 and 350 <= mouse[1] <= 450:
                    game_loop.game(timeLimit, 2)
                elif 320 <= mouse[0] <= 480 and 450 <= mouse[1] <= 550:
                    game_loop.game(timeLimit, 3)
                elif 320 <= mouse[0] <= 480 and 550 <= mouse[1] <= 650:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(BLACK)
        my_group2.draw(screen)
        my_group2.update()
        my_group3.draw(screen)
        my_group3.update()
        my_group4.draw(screen)
        my_group4.update()
        my_group5.draw(screen)
        my_group5.update()
        clock.tick(6)

        # difficulty buttons
        text_maker1('CHOOSE DIFFICULTY LEVEL', 30, WHITE, BLACK, 320, 100, 180, 50)
        text_maker2('EASY', 32, BLACK, (141, 238, 238), 320, 250, 160, 100)
        text_maker2('NORMAL', 32, BLACK, (30, 144, 255), 320, 350, 160, 100)
        text_maker2('HARD', 32, BLACK, (141, 238, 238), 320, 450, 160, 100)
        text_maker2('Quit', 32, BLACK, RED, 320, 550, 160, 100)

        pygame.mouse.set_visible(True)
        pygame.display.flip()
