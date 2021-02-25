import pygame

def deadScreen(screen, width, height):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("You lose!!!", True, (100, 100, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)), [width // 4, height // 4, width // 2, height // 2], width=5)

    restart_text = font.render("Menu", True, (100, 100, 100))
    restart_text_x = width // 8 * 3 - restart_text.get_width() // 2
    restart_text_y = height // 8 * 5 - restart_text.get_height() // 2
    restart_text_w = restart_text.get_width()
    restart_text_h = restart_text.get_height()
    screen.blit(restart_text, (restart_text_x, restart_text_y))

    quit_text = font.render("Quit", True, (100, 100, 100))
    quit_text_x = width // 8 * 5 - quit_text.get_width() // 2
    quit_text_y = height // 8 * 5 - quit_text.get_height() // 2
    quit_text_w = quit_text.get_width()
    quit_text_h = quit_text.get_height()
    screen.blit(quit_text, (quit_text_x, quit_text_y))
    # button_text_w = max(quit_text_w // 2, restart_text_w//2)
    button_text_w = 60
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                     [restart_text_x - button_text_w, restart_text_y - restart_text_h // 2, button_text_w * 4,
                      restart_text_h * 2],
                     width=5)
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                     [quit_text_x - button_text_w * 1.4, quit_text_y - quit_text_h // 2,
                      button_text_w * 4, quit_text_h * 2],
                     width=5)

    return restart_text_x - button_text_w, restart_text_y - restart_text_h // 2, button_text_w * 4,\
           restart_text_h * 2, quit_text_x - button_text_w * 1.4, quit_text_y - quit_text_h // 2,\
           button_text_w * 4, quit_text_h * 2