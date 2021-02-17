#mainloop
import pygame

def draw(screen, width, height, player_position):
    #ground
    pygame.draw.rect(screen, pygame.Color('Gray'), ((0, height // 4 * 3), (width, height//4)), width=0)
    #tower
    pygame.draw.rect(screen, pygame.Color((100, 100, 100)), ((width//9*4, height//8*3), (width//9, height // 8 * 3)), width=0)
    # #player
    # pygame.draw.rect(screen, pygame.Color((255, 0, 0)),
    #                  ((player_position[0], player_position[1]), (20, 50)), width=0)

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True

    player_position = [width//2, height//2]
    horizontall_speed = 200
    vertical_speed = 500

    all_sprites = pygame.sprite.Group()
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

    class Ground(pygame.sprite.Sprite):
        def __init__(self, width, height, *group):
            super().__init__(*group)
            self.image = pygame.Surface([width, 5])
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(0, height//5*4, width, 5)


        def update(self):
            pass

    player = Player(player_position[0], player_position[1], 20, 50, all_sprites)
    ground = Ground(width, height, [all_sprites, ground_layer])

    # movement triggers
    right_trigger = False
    left_trigger = False
    jump_trigger = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # horizontal move begin
                if event.key == pygame.K_RIGHT:
                    right_trigger = True
                    left_trigger = False
                elif event.key == pygame.K_LEFT:
                    right_trigger = False
                    left_trigger = True
                # horizontal move end
                # vertical move
                elif event.key == pygame.K_UP:
                    jump_trigger = True

            if event.type == pygame.KEYUP:
                # horizontal move begin
                if event.key == pygame.K_RIGHT:
                    right_trigger = False
                elif event.key == pygame.K_LEFT:
                    left_trigger = False
                # horizontal move end

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # horizontal move begin
        if left_trigger:
            player.vx = -1 * horizontall_speed * clock.tick(30) / 1000
        elif right_trigger:
            player.vx = horizontall_speed * clock.tick(30) / 1000
        else:
            player.vx = 0
        # horizontal move end

        # vertical move begin
        if jump_trigger:
            vertical_speed = -300
            player.vy = vertical_speed * clock.tick(30) / 1000
            jump_trigger = False
        else:
            if vertical_speed >= 300:
                vertical_speed = 300
            else:
                vertical_speed += 20
            player.vy = vertical_speed * clock.tick(30) / 1000
        # vertical move end

        clock.tick(30)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        # draw(screen, width, height)
        pygame.display.flip()
    pygame.quit()