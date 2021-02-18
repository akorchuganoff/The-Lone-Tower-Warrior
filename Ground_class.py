import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height, *group):
        super().__init__(*group)
        self.image = pygame.Surface([width, 5])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(0, height // 5 * 4, width, 5)

    def update(self):
        pass