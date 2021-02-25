import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([100, 100])
        self.rect = pygame.Rect(150, 350, 100, 100)
        self.image.fill((255, 255, 255))

    def update(self):
        pass

# portal = Portal([all_sprites, portal_group])