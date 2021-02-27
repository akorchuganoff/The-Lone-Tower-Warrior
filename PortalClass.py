import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Data/portal1.png')
        self.rect = pygame.Rect(1000, 0, self.image.get_width(), self.image.get_height())

    def update(self):
        pass

# portal = Portal([all_sprites, portal_group])