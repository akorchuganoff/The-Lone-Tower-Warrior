# mainloop
import pygame
import random

from dead_screen import deadScreen
from logo_screen import logo
from menu_screen import menuScreen
from shop_screen import shopScreen
from PortalClass import Portal

# TODO: make a portal
# TODO: camera

class MainTower(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, hp, group, all_sprites, tools):
        super().__init__(*group)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(x, y, width, height)
        self.hp = hp
        self.width = width
        self.height = height
        self.MainTowerHPbar = HPbar(self, 500, 20, [all_sprites, tools])
        self.damage = 0

    def update(self):
        global collisionClock

        if collisionClock >= 5:
            for enemy in pygame.sprite.spritecollide(self, enemies, False):
                enemy.hp -= self.damage
                if enemy.hp <= 0:
                    enemy.hpBar.kill()
                    enemy.kill()
                    money.amount += 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, hp, group, all_sprites, tools):
        super().__init__(*group)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(x, y, width, height)
        self.vx = 0
        self.vy = 0
        self.isGrounded = False
        self.hp = hp
        self.PlayerHPbar = HPbar(self, 100, 10, [all_sprites, tools])
        self.width = width
        self.height = height

    def hit(self):
        global money
        for enemy in pygame.sprite.spritecollide(self, enemies, False):
            enemy.hp -= 1
            if enemy.hp <= 0:
                enemy.hpBar.kill()
                enemy.kill()
                money.amount += 1


    def update(self):
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.isGrounded = True
            if self.vy <= 0:
                self.rect = self.rect.move(self.vx, self.vy)
            else:
                self.rect = self.rect.move(self.vx, 0)

        else:
            self.isGrounded = False
            self.rect = self.rect.move(self.vx, self.vy)



class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, group):
        super().__init__(*group)
        self.image = pygame.Surface([width, 5])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x, y, width, 5)

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y, width, height, player, group, all_sprites, tools):
        global speedPerFrame

        super().__init__(*group)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(x-width, y-height, width*2, height*2)
        self.vx = 0
        self.vy = 300 * speedPerFrame
        self.player = player

        self.hp = 10
        self.hpBar = HPbar(self, width, 10, [all_sprites, tools])
        self.width = width
        self.height = height

    def EnemyAI(self):
        global speedPerFrame

        if self.player.rect.x + self.player.width//2 > self.rect.x:
            self.vx = 100 * speedPerFrame
        elif self.player.rect.x + self.player.width//2 < self.rect.x:
            self.vx = -100 * speedPerFrame
        else:
            self.vx = 0
        self.rect = self.rect.move(self.vx, 0)

    def update(self):
        global collisionClock
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.EnemyAI()
        else:
            self.rect = self.rect.move(self.vx, self.vy)

        if collisionClock >= 5:
            if pygame.sprite.spritecollideany(self, player_group):
                player.hp -= 1
            if pygame.sprite.spritecollideany(self, maintowergroup):
                mainTower.hp -= 1


class HPbar(pygame.sprite.Sprite):
    def __init__(self, player, width, height, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(player.rect.x - width // 2, player.rect.y - height, width, height)
        self.player = player
        self.hp_beg = player.hp
        self.hp = player.hp
        self.width = width
        self.height = height

    def update(self):
        self.rect = pygame.Rect(self.player.rect.x - self.width // 2 + self.player.width // 2, self.player.rect.y - self.height*2, self.width, self.height)
        self.hp = self.player.hp
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, pygame.Color((255, 0, 0)), [(1, 1), (self.width*int(self.hp)/self.hp_beg, height-2)], width=0)


class Money(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([500, 35])
        self.rect = pygame.Rect(50, 50, 100, 15)
        self.font = pygame.font.Font(None, 30)
        self.amount = 0

    def update(self):

        text = self.font.render(f"Your balance: {self.amount}", True, (200, 200, 200))
        text_x = 0
        text_y = 0
        text_w = text.get_width()
        text_h = text.get_height()
        self.image.fill((0, 0, 0))
        self.image.blit(text, (text_x, text_y))


def newWave(typesOfEnemies):
    global waves
    waves+= 1
    for i in range(waves):
        enemy = typesOfEnemies[random.randrange(0, len(typesOfEnemies), 1)]
        if enemy == 'goblin':
            enemy = Enemy(random.randrange(0, width-50), 600, 30, 30, player, [all_sprites, enemies], all_sprites, tools)
        elif enemy == 'giant':
            enemy = Enemy(random.randrange(0, width-50), 600, 50, 50, mainTower, [all_sprites, enemies], all_sprites, tools)


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
    shop_group = pygame.sprite.Group()
    maintowergroup = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    ground_layer = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    tools = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()

    # input this blok in restart cheacking
    money = Money([all_sprites, tools])
    mainTower = MainTower(width//8*3, height//4, width//4, height//2, 1000, [all_sprites, maintowergroup], all_sprites, tools)
    player = Player(player_position[0], player_position[1], 20, 50, 100, [all_sprites, player_group], all_sprites, tools)
    ground = Ground(0, height//5*4, width, [all_sprites, ground_layer])
    groundToPortal_1 = Ground(0, height//16*11  , width//8, [all_sprites, ground_layer])
    groundToPortal_2 = Ground(width//8, height // 8 * 5, width // 8*2, [all_sprites, ground_layer])
    shop = shopScreen(width, height, [shop_group], money)
    portal = Portal([all_sprites, portal_group])
    waves = 0
    typesOfEnemies = ['goblin', 'giant']
    # end of block

    # movement triggers
    right_trigger = False
    left_trigger = False
    jump_trigger = False
    condition_trigger = 2
    shop_trigger = False

    collisionClock = 0

    time = 0
    speedPerFrame = 0

    while running:
        speedPerFrame = clock.tick(30) / 1000
        if condition_trigger == -1:
            if time >= 4:
                condition_trigger = 0
            else:
                logo(screen, width, height)

        if condition_trigger == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    start_pos, continue_pos, stats_pos = menuScreen(screen, width, height)
                    if start_pos[0]<=x<=start_pos[2] and start_pos[1]<=y<=start_pos[3]:
                        print('start')
                        condition_trigger = 2

                        # start game
                        all_sprites = pygame.sprite.Group()
                        maintowergroup = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        tools = pygame.sprite.Group()

                        money = Money([all_sprites, tools])
                        mainTower = MainTower(width // 8 * 3, height // 4, width // 4, height // 2, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 20, 50, 100,
                                        [all_sprites, player_group], all_sprites, tools)
                        ground = Ground(width, height, [all_sprites, ground_layer])
                        shop = shopScreen(width, height, [shop_group], money)
                        waves = 0
                        typesOfEnemies = ['goblin', 'giant']

                    elif continue_pos[0]<=x<=continue_pos[2] and continue_pos[1]<=y<=continue_pos[3]:
                        print('continue')
                    elif stats_pos[0]<=x<=stats_pos[2] and stats_pos[1]<=y<=stats_pos[3]:
                        print('stats')

            menuScreen(screen, width, height)

        elif condition_trigger == 2:
            if not shop_trigger:
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
                        # vertical move end

                        # shop
                        elif event.key == pygame.K_q:
                            shop_trigger = True


                    if event.type == pygame.KEYUP:
                        # horizontal move begin
                        if event.key == pygame.K_RIGHT:
                            right_trigger = False
                        elif event.key == pygame.K_LEFT:
                            left_trigger = False
                        # horizontal move end

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player.hit()

                if player.hp <= 0 or mainTower.hp <= 0:
                    condition_trigger = 3

                # horizontal move begin
                if left_trigger:
                    player.vx = -1 * horizontall_speed * speedPerFrame
                elif right_trigger:
                    player.vx = horizontall_speed * speedPerFrame
                else:
                    player.vx = 0
                # horizontal move end

                # vertical move begin
                if jump_trigger:
                    if player.isGrounded:
                        vertical_speed = -300
                        player.vy = vertical_speed * speedPerFrame
                    jump_trigger = False
                else:
                    if vertical_speed >= 300:
                        vertical_speed = 300
                    else:
                        vertical_speed += 20
                    player.vy = vertical_speed * speedPerFrame
                # vertical move end

                # enemies spawn
                if int(time) %5 == 0:
                    time += 1
                    newWave(typesOfEnemies)

                screen.fill((0, 0, 0))
                # Main act
                all_sprites.draw(screen)
                all_sprites.update()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            shop_trigger = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        xr, yr, xl, yl = shop.update()
                        print(x, y)
                        print(xr, yr, xl, yl)
                        if xr<=x-width//8<=xl and yr<=y-height//8<=yl:
                            if shop.money.amount >= shop.price:
                                shop.buy(mainTower)
                                print('buy')

                            else:
                                pass

                shop_group.draw(screen)
                shop_group.update()

        elif condition_trigger == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    rx, ry, rw, rh, qx, qy, qw, qh = deadScreen(screen, width, height)
                    # restart checking
                    if rx <= pos[0] <= rx + rw and ry <= pos[1] <= ry + rh:
                        condition_trigger = 2

                        for elem in all_sprites:
                            elem.kill()

                        # start game
                        all_sprites = pygame.sprite.Group()
                        maintowergroup = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        tools = pygame.sprite.Group()

                        money = Money([all_sprites, tools])
                        mainTower = MainTower(width // 8 * 3, height // 4, width // 4, height // 2, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 20, 50, 100,
                                        [all_sprites, player_group], all_sprites, tools)
                        ground = Ground(width, height, [all_sprites, ground_layer])
                        shop = shopScreen(width, height, [shop_group], money)
                        waves = 0
                        typesOfEnemies = ['goblin', 'giant']

                    # quit
                    if qx <= pos[0] <= qx + qw and qy <= pos[1] <= qy + qh:
                        running = False

            deadScreen(screen, width, height)

        collisionClock += 1
        time += speedPerFrame
        if collisionClock >= 6:
            collisionClock = 0

        print("\rFPS:", clock.get_fps(), end='')
        pygame.display.flip()
    pygame.quit()