import pygame

def menuScreen(screen, width, height):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)

    start_text = font.render("Start", True, (200, 200, 200))
    start_text_x = width // 8 - start_text.get_width()//2
    start_text_y = height // 8 - start_text.get_height() // 2
    start_text_w = start_text.get_width()
    start_text_h = start_text.get_height()
    screen.blit(start_text, (start_text_x, start_text_y))

    continue_text = font.render("Continue", True, (200, 200, 200))
    continue_text_x = width // 8 - continue_text.get_width() // 2
    continue_text_y = height // 8 * 2 - continue_text.get_height() // 2
    continue_text_w = continue_text.get_width()
    continue_text_h = continue_text.get_height()
    screen.blit(continue_text, (continue_text_x, continue_text_y))

    stats_text = font.render("Stats", True, (200, 200, 200))
    stats_text_x = width // 8 - start_text.get_width()//2
    stats_text_y = height // 8 * 3 - stats_text.get_height() // 2
    stats_text_w = stats_text.get_width()
    stats_text_h = stats_text.get_height()
    screen.blit(stats_text, (stats_text_x, stats_text_y))

    button_text_w = max(start_text.get_width()//2, continue_text.get_width()//2, stats_text.get_width()//2) + 20

    pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                     [width//8 - button_text_w, start_text_y - start_text_h // 2, button_text_w * 2,
                      start_text_h*2],
                     width=5)
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                     [width//8 - button_text_w, continue_text_y - continue_text_h // 2, button_text_w * 2,
                      continue_text_h * 2],
                     width=5)
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                     [width//8 - button_text_w, stats_text_y - stats_text_h // 2, button_text_w * 2,
                      stats_text_h * 2],
                     width=5)

    start_pos = (width//8 - button_text_w, start_text_y - start_text_h // 2, width//8 + button_text_w, start_text_y + start_text_h // 2 * 3)
    continue_pos = (width//8 - button_text_w, continue_text_y - continue_text_h // 2, width//8 + button_text_w, continue_text_y + continue_text_h // 2*3)
    stats_pos = (width//8 - button_text_w, stats_text_y - stats_text_h // 2, width//8 + button_text_w, stats_text_y + stats_text_h // 2*3)

    return start_pos, continue_pos, stats_pos


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        menuScreen(screen, width, height)

        clock.tick(30)
        pygame.display.flip()
    pygame.quit()