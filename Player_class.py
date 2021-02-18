import pygame

ground_layer = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(group)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(x, y, width, height)
        self.vx = 0
        self.vy = 0

    def update(self):
        if pygame.sprite.spritecollideany(self, ground_layer):
            if self.vy <= 0:
                self.rect = self.rect.move(self.vx, self.vy)
            else:
                self.rect = self.rect.move(self.vx, 0)
        else:
            self.rect = self.rect.move(self.vx, self.vy)