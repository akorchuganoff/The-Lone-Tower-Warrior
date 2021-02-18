import pygame

clock = pygame.time.Clock()
ground_layer = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(*group)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(x, y, width, height)
        self.vx = 0
        self.vy = 300 * clock.tick(30) / 1000

    def update(self):
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.rect = self.rect.move(self.vx, 0)
        else:
            self.rect = self.rect.move(self.vx, self.vy)