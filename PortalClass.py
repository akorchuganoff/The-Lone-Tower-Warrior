import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([200, 200])
        self.rect = pygame.Rect(1000, 0, 200, 200)
        self.image.fill((255, 255, 255))

    def update(self):
        pass

# portal = Portal([all_sprites, portal_group])