# mainloop
import pygame
import random

from dead_screen import deadScreen
from logo_screen import logo
from menu_screen import menuScreen
from shop_screen import shopScreen
from PortalClass import Portal

# TODO:

easy_enemy_walk = [pygame.image.load('Data/easy enemy/walk/1.png'), pygame.image.load('Data/easy enemy/walk/2.png'),
                   pygame.image.load('Data/easy enemy/walk/3.png'), pygame.image.load('Data/easy enemy/walk/4.png'),
                   pygame.image.load('Data/easy enemy/walk/5.png'), pygame.image.load('Data/easy enemy/walk/6.png'),
                   pygame.image.load('Data/easy enemy/walk/7.png')]

easy_enemy_idle = [pygame.image.load('Data/easy enemy/ide.png')]

easy_enemy_attack = [pygame.image.load('Data/easy enemy/attack/1.png'),
                     pygame.image.load('Data/easy enemy/attack/2.png'),
                     pygame.image.load('Data/easy enemy/attack/3.png'),
                     pygame.image.load('Data/easy enemy/attack/4.png'),
                     pygame.image.load('Data/easy enemy/attack/5.png'),
                     pygame.image.load('Data/easy enemy/attack/6.png'),
                     pygame.image.load('Data/easy enemy/attack/7.png')]


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
        if collisionClock % 5 == 0:
            for enemy in pygame.sprite.spritecollide(self, enemies, False):
                enemy.hp -= self.damage


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
        self.PlayerHPbar = HPbar(self, 100, 10, [all_sprites, tools, all_boss_sprites])
        self.width = width
        self.height = height

    def hit(self):
        for enemy in pygame.sprite.spritecollide(self, enemies, False):
            enemy.hp -= 1
        for enemy in pygame.sprite.spritecollide(self, boss_group, False):
            enemy.hp -= 1

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
    def __init__(self, x, y, width, height, player, group, all_sprites, tools, hp=10):
        super().__init__(*group)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(x, y, width, height)
        self.vx = 0
        self.vy = 300 * speedPerFrame
        self.player = player
        self.hp = hp
        self.hpBar = HPbar(self, width, hp, [all_sprites, tools])
        self.width = width
        self.height = height

    def EnemyAI(self):
        if self.player.rect.x + self.player.width // 2 > self.rect.x:
            self.vx = 100 * speedPerFrame
        elif self.player.rect.x + self.player.width // 2 < self.rect.x:
            self.vx = -100 * speedPerFrame
        else:
            self.vx = 0
        self.rect = self.rect.move(self.vx, 0)

    def update(self):
        if self.hp <= 0:
            money.amount += 1
            self.hpBar.kill()
            self.kill()
            return
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.EnemyAI()
        else:
            self.rect = self.rect.move(self.vx, self.vy)
        if collisionClock % 5 == 0:
            if pygame.sprite.spritecollideany(self, player_group):
                player.hp -= 1
            if pygame.sprite.spritecollideany(self, maintowergroup):
                mainTower.hp -= 1


class Easy_enemy(Enemy):
    def __init__(self, x, y, width, height, player, group, all_sprites, tools, hp=10):
        super().__init__(x, y, width, height, player, group, all_sprites, tools, hp=10)
        self.frames_walk = easy_enemy_walk
        self.frames_idle = easy_enemy_idle
        self.frames_attack = easy_enemy_attack
        self.frames = self.frames_idle
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = pygame.Rect(0, 0, self.frames_idle[0].get_width(),
                                self.frames_idle[0].get_height())
        self.rect = self.rect.move(x, y)

        self.width = self.frames_idle[0].get_width()
        self.hpBar.kill()
        self.hpBar = HPbar(self, self.frames_walk[0].get_width(), hp, [all_sprites, tools])
        print(self.rect, self.frames[0].get_width())

        self.count = 0
        self.attackTrigger = False

    def EnemyAI(self):
        super().EnemyAI()

        if 0 <= self.rect.x - self.player.rect.x+self.rect.w <= 10 or 0 <= self.rect.x - self.player.rect.x + self.player.rect.w <= 10:
            self.attackTrigger = True
        else:
            self.attackTrigger = False

    def update(self):
        super().update()

        self.count += 1
        if self.count % 4 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        if not self.attackTrigger:
            if self.cur_frame == 0:
                if -1 <= self.vx <= 1:
                    self.frames = self.frames_idle
                else:
                    self.frames = self.frames_walk
        else:
            self.frames = self.frames_attack


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        self.frames = sheet
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = pygame.Rect(0, 0, sheet[0].get_width(),
                                sheet[0].get_height())
        self.rect = self.rect.move(x, y)
        self.count = 0

    def update(self):
        self.count += 1
        if self.count % 3 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


class Boss(Enemy):
    def __init__(self, x, y, width, height, player, group, all_boss_sprites, tools, name, hp):
        super().__init__(x, y, width, height, player, group, all_boss_sprites, tools, hp)
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.hpBar.kill()
        self.hpBar = Boss_HPbar(self, [all_boss_sprites, tools])

    def draw_boss_name(self):
        font = pygame.font.Font(None, 50)
        text = font.render(self.name, True, (200, 200, 200))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 8 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))

    def update(self):
        if self.hp <= 0:
            money.amount += 100
            self.hpBar.kill()
            self.kill()
            return
        if not pygame.sprite.spritecollideany(self, ground_layer):
            self.rect.y += 300 * speedPerFrame


class FireBoss(Boss):
    def update(self):
        if self.hp <= 0:
            money.amount += 100
            self.hpBar.kill()
            self.kill()
            return
        if not pygame.sprite.spritecollideany(self, ground_layer):
            self.rect.y += 300 * speedPerFrame
        if collisionClock % 75 == 59:
            if player.rect.x < self.rect.x + self.rect.width // 2:
                d = - 1
            else:
                d = 1
            Bullet(self.rect.x + self.width // 2,
                   self.rect.y + self.height // 2, 20, 'pink',
                   d, 400, 10, 'player', [bullets, all_boss_sprites])
        if collisionClock % 5 == 0:
            if pygame.sprite.spritecollideany(self, player_group):
                player.hp -= 1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, direction, speed, damage, player, group):
        super().__init__(*group)
        self.image = pygame.Surface([radius * 2, radius * 2])
        pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        # direction = +- 1
        self.direct = direction
        self.speed = speed
        self.damage = damage
        if player == 'player':
            self.target = player_group
        elif player == 'enemy':
            self.target = enemies
        elif player == 'boss':
            self.target = boss_group

    def update(self):
        self.rect.x += self.direct * self.speed * speedPerFrame
        target = pygame.sprite.spritecollideany(self, self.target)
        if pygame.sprite.spritecollideany(self, self.target):
            target.hp -= self.damage
            self.kill()


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
        self.rect = pygame.Rect(self.player.rect.x - self.width // 2 + self.player.width // 2,
                                self.player.rect.y - self.height * 2, self.width, self.height)
        self.hp = self.player.hp
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, pygame.Color((255, 0, 0)),
                         [(1, 1), (self.width * int(self.hp) / self.hp_beg, height - 2)], width=0)


class Boss_HPbar(HPbar):
    def __init__(self, player, groups):
        super().__init__(player, 1000, 20, groups)
        self.rect = pygame.Rect(100, 150, 1000, 20)

    def update(self):
        self.hp = self.player.hp
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, pygame.Color((255, 0, 0)),
                         [(1, 1), (self.width * int(self.hp) / self.hp_beg, height - 2)], width=0)


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
    waves += 1
    for i in range(waves):
        enemy = typesOfEnemies[random.randrange(0, len(typesOfEnemies), 1)]
        x = random.randrange(ground.rect.x, ground.rect.x + ground.rect.width - 50, 1)
        if enemy == 'goblin':
            enemy = Easy_enemy(x, ground.rect.y - 100, 30, 30, player, [all_sprites, enemies], all_sprites, tools)
        elif enemy == 'giant':
            enemy = Enemy(x, ground.rect.y - 100, 50, 50, mainTower, [all_sprites, enemies], all_sprites, tools)

        print(x, ground.rect.x, )


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 4 * 3)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    player_position = [width // 2, height // 2]
    horizontall_speed = 200
    vertical_speed = 500

    typesOfEnemies = ['goblin', 'giant']

    condition_trigger = -1
    collisionClock = 0
    time = 0

    camera = Camera()

    while running:
        speedPerFrame = clock.tick(30) / 1000
        if condition_trigger == -1:
            if time >= 1:
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
                    if start_pos[0] <= x <= start_pos[2] and start_pos[1] <= y <= start_pos[3]:
                        print('start')
                        condition_trigger = 2

                        # start game
                        all_sprites = pygame.sprite.Group()
                        all_boss_sprites = pygame.sprite.Group()
                        boss_group = pygame.sprite.Group()
                        shop_group = pygame.sprite.Group()
                        maintowergroup = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        tools = pygame.sprite.Group()
                        portal_group = pygame.sprite.Group()

                        money = Money([all_sprites, tools])
                        mainTower = MainTower(width // 8 * 3, height // 4, width // 4, height // 2, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 20, 50, 100,
                                        [all_sprites, player_group, all_boss_sprites], all_sprites, tools)
                        ground = Ground(0, height // 4 * 3, width, [all_sprites, ground_layer])
                        shop = shopScreen(width, height, [shop_group], money)
                        waves = 0
                        # portal way
                        portal = Portal([all_sprites, portal_group])

                        # movement triggers
                        right_trigger = False
                        left_trigger = False
                        jump_trigger = False
                        shop_trigger = False
                        last_move = 'right'
                    elif continue_pos[0] <= x <= continue_pos[2] and continue_pos[1] <= y <= continue_pos[3]:
                        print('continue')
                    elif stats_pos[0] <= x <= stats_pos[2] and stats_pos[1] <= y <= stats_pos[3]:
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
                            last_move = 'right'
                            right_trigger = True
                            left_trigger = False
                        elif event.key == pygame.K_LEFT:
                            last_move = 'left'
                            right_trigger = False
                            left_trigger = True
                        # horizontal move end

                        # vertical move
                        elif event.key == pygame.K_UP:
                            jump_trigger = True
                        # vertical move end

                        elif event.key == pygame.K_y:
                            if last_move == 'right':
                                d = 1
                            else:
                                d = -1
                            Bullet(player.rect.x + player.width // 2,
                                   player.rect.y + player.height // 2, 10, 'red',
                                   d, 200, 5, 'enemy', [all_sprites, bullets, all_boss_sprites])
                        elif event.key == pygame.K_q:
                            shop_trigger = True
                    elif event.type == pygame.KEYUP:
                        # horizontal move begin
                        if event.key == pygame.K_RIGHT:
                            right_trigger = False
                        elif event.key == pygame.K_LEFT:
                            left_trigger = False
                        # horizontal move end

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[0] > portal.rect.x and event.pos[0] < portal.rect.x + portal.rect.width and\
                            event.pos[1] > portal.rect.y and event.pos[1] < portal.rect.y + portal.rect.height:
                            name = 'FireBoss'
                            boss = FireBoss(width - 200, height // 8 * 4, 100, 100, player,
                                            [all_boss_sprites, boss_group], all_boss_sprites, tools, name, 300)
                            boss_ground = Ground(0, height // 4 * 3, width, [all_boss_sprites, ground_layer])
                            condition_trigger = 4
                            f1 = False
                            continue
                        else:
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
                if int(time) % 5 == 0:
                    time += 1
                    newWave(typesOfEnemies)
                # Main act
                screen.fill((0, 0, 0))
                all_sprites.draw(screen)
                all_sprites.update()

                camera.update(player)
                for sprite in all_sprites :
                    if sprite != money:
                        camera.apply(sprite)

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
                        if xr <= x - width // 8 <= xl and yr <= y - height // 8 <= yl:
                            if shop.money.amount >= shop.price:
                                shop.buy(mainTower)
                                print('buy')
                            else:
                                pass
                shop_group.draw(screen)
                shop_group.update()

        elif condition_trigger == 3:
            for elem in all_sprites:
                elem.kill()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    rx, ry, rw, rh, qx, qy, qw, qh = deadScreen(screen, width, height)
                    # restart checking
                    if rx <= pos[0] <= rx + rw and ry <= pos[1] <= ry + rh:
                        condition_trigger = 0

                    # quit
                    if qx <= pos[0] <= qx + qw and qy <= pos[1] <= qy + qh:
                        running = False
            deadScreen(screen, width, height)

        elif condition_trigger == 4:
            if not f1:
                player.rect.y -= 200
                f1 = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # horizontal move begin
                    if event.key == pygame.K_RIGHT:
                        last_move = 'right'
                        right_trigger = True
                        left_trigger = False
                    elif event.key == pygame.K_LEFT:
                        last_move = 'left'
                        right_trigger = False
                        left_trigger = True
                    # horizontal move end
                    # vertical move
                    elif event.key == pygame.K_UP:
                        jump_trigger = True
                    # vertical move end
                    elif event.key == pygame.K_y:
                        if last_move == 'right':
                            d = 1
                        else:
                            d = -1
                        Bullet(player.rect.x + player.width // 2,
                                player.rect.y + player.height // 2, 10, 'red',
                                d, 200, 5, 'boss', [all_sprites, bullets, all_boss_sprites])
                    elif event.key == pygame.K_z:
                        player.rect.x = mainTower.rect.x + mainTower.rect.width // 2
                        for elem in boss_group:
                            elem.hpBar.kill()
                            elem.kill()
                        for elem in bullets:
                            elem.kill()
                        for elem in all_boss_sprites:
                            if elem != player and elem != player.PlayerHPbar:
                                elem.kill()
                        condition_trigger = 2
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        right_trigger = False
                    elif event.key == pygame.K_LEFT:
                        left_trigger = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    player.hit()

            if boss.hp <= 0:
                player.rect.x = mainTower.rect.x + mainTower.rect.width // 2
                for elem in boss_group:
                    elem.hpBar.kill()
                    elem.kill()
                for elem in bullets:
                    elem.kill()
                for elem in all_boss_sprites:
                    if elem != player and elem != player.PlayerHPbar:
                        elem.kill()
            if player.hp <= 0 or mainTower.hp <= 0:
                condition_trigger = 3
                # condition_trigger = 2

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
            # Main act
            screen.fill((0, 0, 0))
            boss.draw_boss_name()
            all_boss_sprites.draw(screen)
            all_boss_sprites.update()

        collisionClock += 1
        time += speedPerFrame

        print("\rFPS:", clock.get_fps(), end='')
        pygame.display.flip()
    pygame.quit()