import pygame

def deadScreen(screen, width, height):
    screen.fill((32, 28, 43))
    pygame.draw.rect(screen, pygame.Color('#ffd700'), [width // 4, height // 4, width // 2, height // 2], width=5)
    pygame.draw.rect(screen, pygame.Color('#ffd700'), [width // 4, height // 4, width // 2, height // 4], width=5)
    pygame.draw.rect(screen, pygame.Color('#ffd700'), [width // 4, height // 2, width // 4, height // 4], width=5)
    screen.blit(pygame.image.load('Data/menu/menu.gif'), (400, 500))
    screen.blit(pygame.image.load('Data/menu/game over.gif'), (510, 300))
    screen.blit(pygame.image.load('Data/menu/exit2.gif'), (700, 500))