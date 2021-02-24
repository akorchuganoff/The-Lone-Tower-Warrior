import pygame
from math import sqrt

def logo(screen, width, height):
    pygame.draw.circle(screen, pygame.Color((255, 255, 255)), (width//2, height//2), radius=200, width=5)
    pygame.draw.line(screen, pygame.Color((255, 255, 255)), (width//2 - sqrt(2)*200/2, height//2 - sqrt(2)*200/2), (width//2 + sqrt(2)*200/2, height//2 + sqrt(2)*200/2), width=5)
    pygame.draw.line(screen, pygame.Color((255, 255, 255)),
                     (width // 2 + sqrt(2) * 200 / 2, height // 2 - sqrt(2) * 200 / 2),
                     (width // 2 - sqrt(2) * 200 / 2, height // 2 + sqrt(2) * 200 / 2), width=5)

    font = pygame.font.Font(None, 50)
    text = font.render("Korchuganov and Davyidenko prods", True, (200, 200, 200))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 8 * 7 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
