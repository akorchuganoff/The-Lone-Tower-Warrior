#mainloop
import pygame
from dead_screen import deadScreen

def draw(screen, width, height):
    #ground
    pygame.draw.rect(screen, pygame.Color('Gray'), ((0, height // 4 * 3), (width, height//4)), width=0)
    #tower
    pygame.draw.rect(screen, pygame.Color((100, 100, 100)), ((width//9*4, height//8*3), (width//9, height // 8 * 3)), width=0)




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
    player = pygame.sprite.Group()
    ground_layer = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    tools = pygame.sprite.Group()


    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, hp, group):
            super().__init__(*group)
            self.image = pygame.Surface([width, height])
            self.image.fill((255, 0, 0))
            self.rect = pygame.Rect(x, y, width, height)
            self.vx = 0
            self.vy = 0
            self.hp = hp

        def update(self):
            if pygame.sprite.spritecollideany(self, ground_layer):
                if self.vy <= 0:
                    self.rect = self.rect.move(self.vx, self.vy)
                else:
                    self.rect = self.rect.move(self.vx, 0)
            else:
                self.rect = self.rect.move(self.vx, self.vy)

            if pygame.sprite.spritecollideany(self, enemies):
                self.hp -= 1
                # self.hp -= clock.tick(30)/1000

    class Ground(pygame.sprite.Sprite):
        def __init__(self, width, height, *group):
            super().__init__(*group)
            self.image = pygame.Surface([width, 5])
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(0, height//5*4, width, 5)

        def update(self):
            pass


    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x,y, width, height, group):
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

    class HPbar(pygame.sprite.Sprite):
        def __init__(self, player, width, height, groups):
            super().__init__(*groups)
            self.image = pygame.Surface([102, 12])
            self.rect = pygame.Rect(width//4*3, height//16, 102, 12)
            self.hp = player.hp

        def update(self):
            self.hp = player.hp
            self.image.fill((255, 255, 255))
            pygame.draw.rect(self.image, pygame.Color((255, 0, 0)), [(1, 1), (int(player.hp), 12)], width=0)


    # input this blok in restart cheacking
    player = Player(player_position[0], player_position[1], 20, 50, 0, [all_sprites, player])
    ground = Ground(width, height, [all_sprites, ground_layer])
    enemy_1 = Enemy(50, 50, 30, 30, [all_sprites, enemies])
    MainHPbar = HPbar(player, width, height, [all_sprites, tools])
    # end of block

    # movement triggers
    right_trigger = False
    left_trigger = False
    jump_trigger = False
    condition_trigger = 2

    while running:
        if condition_trigger == 2:
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

            if player.hp <= 0:
                condition_trigger = 3

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

            # check
            print(MainHPbar.hp)
            # check end

            clock.tick(30)
            screen.fill((0, 0, 0))

            # Make a right order. It is the layer drawing!!!
            # Landskapes
            draw(screen, width, height)

            # Main act
            all_sprites.draw(screen)
            all_sprites.update()

        if condition_trigger == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    rx, ry, rw, rh, qx, qy, qw, qh = deadScreen(screen, width, height)
                    print()
                    # restart cheacking
                    if rx <= pos[0] <= rx + rw and ry <= pos[1] <= ry + rh:
                        condition_trigger = 2

                        all_sprites = pygame.sprite.Group()
                        player = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        tools = pygame.sprite.Group()

                        # input beggin block here
                        player = Player(player_position[0], player_position[1], 20, 50, 50, [all_sprites, player])
                        ground = Ground(width, height, [all_sprites, ground_layer])
                        enemy_1 = Enemy(50, 50, 30, 30, [all_sprites, enemies])
                        MainHPbar = HPbar(player, width, height, [all_sprites, tools])
                        # end of block

                    # quit
                    if qx <= pos[0] <= qx + qw and qy <= pos[1] <= qy + qh:
                        running = False

            deadScreen(screen, width, height)
            clock.tick(30)



        pygame.display.flip()
    pygame.quit()