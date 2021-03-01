# mainloop
import pygame
import random
import math

from dead_screen import deadScreen
from shop_screen import shopScreen
from PortalClass import Portal

# TODO:

player_walk = [pygame.image.load('Data/main hero/run/1.png'),
               pygame.image.load('Data/main hero/run/2.png'),
               pygame.image.load('Data/main hero/run/3.png'),
               pygame.image.load('Data/main hero/run/4.png'),
               pygame.image.load('Data/main hero/run/5.png')]

player_idle = [pygame.image.load('Data/main hero/idle.png')]

player_attack = [pygame.image.load('Data/main hero/attack/1.png'),
                pygame.image.load('Data/main hero/attack/2.png'),
                pygame.image.load('Data/main hero/attack/3.png'),
                pygame.image.load('Data/main hero/attack/4.png'),
                pygame.image.load('Data/main hero/attack/5.png')]

player_jump = [pygame.image.load('Data/main hero/jump/1.png'),
                pygame.image.load('Data/main hero/jump/2.png'),
                pygame.image.load('Data/main hero/jump/3.png'),
                pygame.image.load('Data/main hero/jump/4.png'),
                pygame.image.load('Data/main hero/jump/5.png')]

player_death = [pygame.image.load('Data/main hero/death/1.png'),
                pygame.image.load('Data/main hero/death/2.png'),
                pygame.image.load('Data/main hero/death/3.png'),
                pygame.image.load('Data/main hero/death/4.png'),
                pygame.image.load('Data/main hero/death/5.png')]

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

giant_enemy_walk = [pygame.image.load('Data/giant enemy/walk/1.png'), pygame.image.load('Data/giant enemy/walk/2.png'),
                   pygame.image.load('Data/giant enemy/walk/3.png'), pygame.image.load('Data/giant enemy/walk/4.png'),
                   pygame.image.load('Data/giant enemy/walk/5.png'), pygame.image.load('Data/giant enemy/walk/6.png'),
                   pygame.image.load('Data/giant enemy/walk/7.png')]

giant_enemy_idle = [pygame.image.load('Data/giant enemy/idle.png')]

giant_enemy_attack = [pygame.image.load('Data/giant enemy/attack/1.png'),
                     pygame.image.load('Data/giant enemy/attack/2.png'),
                     pygame.image.load('Data/giant enemy/attack/3.png'),
                     pygame.image.load('Data/giant enemy/attack/4.png'),
                     pygame.image.load('Data/giant enemy/attack/5.png'),
                     pygame.image.load('Data/giant enemy/attack/6.png'),
                     pygame.image.load('Data/giant enemy/attack/7.png')]

fire_boss_idle = [pygame.image.load('Data/fire boss/idle.png')]

fire_boss_attack = [pygame.image.load('Data/fire boss/idle.png'),
                    pygame.image.load('Data/fire boss/idle.png'),
                    pygame.image.load('Data/fire boss/idle.png'),
                    pygame.image.load('Data/fire boss/attack/1.png'),
                    pygame.image.load('Data/fire boss/attack/2.png'),
                    pygame.image.load('Data/fire boss/attack/3.png'),
                    pygame.image.load('Data/fire boss/attack/4.png'),
                    pygame.image.load('Data/fire boss/attack/5.png')]

fire_boss_death = [pygame.image.load('Data/fire boss/death/1.png'),
                    pygame.image.load('Data/fire boss/death/2.png'),
                    pygame.image.load('Data/fire boss/death/3.png'),
                    pygame.image.load('Data/fire boss/death/4.png'),
                    pygame.image.load('Data/fire boss/death/5.png')]

ogre_boss_idle = [pygame.image.load('Data/ogr boss/idle.png')]

ogre_boss_attack = [pygame.image.load('Data/ogr boss/attack/1.png'),
                    pygame.image.load('Data/ogr boss/attack/2.png'),
                    pygame.image.load('Data/ogr boss/attack/3.png'),
                    pygame.image.load('Data/ogr boss/attack/4.png'),
                    pygame.image.load('Data/ogr boss/attack/5.png'),
                    pygame.image.load('Data/ogr boss/attack/6.png'),
                    pygame.image.load('Data/ogr boss/attack/7.png')]

ogre_boss_death = [pygame.image.load('Data/ogr boss/death/1.png'),
                    pygame.image.load('Data/ogr boss/death/2.png'),
                    pygame.image.load('Data/ogr boss/death/3.png'),
                    pygame.image.load('Data/ogr boss/death/4.png'),
                    pygame.image.load('Data/ogr boss/death/5.png'),
                    pygame.image.load('Data/ogr boss/death/6.png'),
                    pygame.image.load('Data/ogr boss/death/7.png')]

ogre_boss_walk = [pygame.image.load('Data/ogr boss/walk/1.png'), pygame.image.load('Data/ogr boss/walk/2.png'),
                   pygame.image.load('Data/ogr boss/walk/3.png'), pygame.image.load('Data/ogr boss/walk/4.png'),
                   pygame.image.load('Data/ogr boss/walk/5.png'), pygame.image.load('Data/ogr boss/walk/6.png'),
                   pygame.image.load('Data/ogr boss/walk/7.png')]

ground_sprite = pygame.image.load('Data/env/ground.png')



def logo(screen, width, height):
    if i > 222:
        k = i - 222
        screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/authors/' + str(k) + '.gif'),
                    (300, 400))
    else:
        screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/name/' + str(i) + '.gif'),
                    (300, 200))
    pygame.draw.rect(screen, pygame.Color('#ffd700'),
                     ((201, 601), ((800 * i / (303 + 222 + 1) - 2), 30 - 2)), width=0)


def menuScreen(screen, width, height, colorkey):
    screen.fill(colorkey)
    screen.blit(pygame.image.load('Data/menu/no continue2.gif'), (300, 100))
    screen.blit(pygame.image.load('Data/menu/new game.gif'), (300, 250))
    screen.blit(pygame.image.load('Data/menu/exit.gif'), (300, 400))
    start_pos, continue_pos, exit_pos = (500, 300, 700, 380), (500, 160, 700, 240), (500, 470, 700, 540)
    return start_pos, continue_pos, exit_pos


class MainTower(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, group, all_sprites, tools):
        super().__init__(*group)
        self.image = pygame.image.load('Data/tower2.png')
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.width = self.rect.width
        self.height = self.rect.height
        self.hp = hp
        self.MainTowerHPbar = HPbar(self, 500, 20, [all_sprites, tools])
        self.damage = 0

    def update(self):
        if collisionClock % 5 == 0:
            for enemy in pygame.sprite.spritecollide(self, enemies, False):
                enemy.hp -= self.damage


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, group, all_sprites, tools):
        super().__init__(*group)
        self.frames_walk = player_walk
        self.frames_attack = player_attack
        self.frames_idle = player_idle
        self.frames_death = player_death
        self.frames_jump = player_jump
        self.frames = self.frames_idle
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = pygame.Rect(x, y, self.frames_idle[0].get_width(),
                                self.frames_idle[0].get_height())
        self.vx = 0
        self.vy = 0
        self.isGrounded = False
        self.attackTrigger = False
        self.archeryTrigger = False
        self.hp = hp
        self.PlayerHPbar = HPbar(self, self.frames_idle[0].get_width(), 10, [all_sprites, tools, all_boss_sprites])
        self.width = self.frames_idle[0].get_width()
        self.height = self.frames_idle[0].get_height()

    def hit(self, pos, coords=(), group=False):
        global last_move
        if not self.isGrounded:
            return
        self.attackTrigger = True
        self.cur_frame = -1
        self.frames = self.frames_attack
        self.attackClock = 0
        if self.rect.x + self.rect.width // 2 <= pos[0]:
            last_move = 'right'
        else:
            last_move = 'left'
        if len(coords) > 0:
            self.archeryTrigger = True
            self.archery_coords = coords
            self.archery_group = group

    def update(self):
        if self.attackTrigger:
            self.attackClock += 1
            if self.attackClock % 3 == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.attackClock == len(self.frames) * 3:
                self.attackTrigger = False
                if self.archeryTrigger:
                    self.archery(*self.archery_coords, self.archery_group)
                    self.archeryTrigger = False
                    return
                for enemy in pygame.sprite.spritecollide(self, enemies, False):
                    enemy.hp -= 10
                for enemy in pygame.sprite.spritecollide(self, boss_group, False):
                    enemy.hp -= 10
            return
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.isGrounded = True
            # animation
            if self.vx == 0 and collisionClock % 5 == 0:
                self.image = self.frames_idle[0]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)

            elif collisionClock % 5 == 0:
                self.frames = self.frames_walk
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
            # end animation
            if self.vy <= 0:
                self.rect = self.rect.move(self.vx, self.vy)
            else:
                self.rect = self.rect.move(self.vx, 0)
        else:
            self.isGrounded = False
            self.frames = self.frames_jump
            if collisionClock % 3 == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.rect.move(self.vx, self.vy)

    def archery(self, x1, y1, x2, y2, group):
        if x1 >= x2:
            dx = 1
        else:
            dx = -1
        if y1 >= y2:
            dy = 1
        else:
            dy = -1
        if y1 - y2 != 0:
            vy2 = int(500 ** 2 / (((x1 - x2) / (y1 - y2)) ** 2 + 1))
        else:
            vy2 = 0
        vx2 = 500 ** 2 - vy2
        vy = vy2 ** 0.5 * dy
        vx = vx2 ** 0.5
        if vx != 0:
            angle = math.degrees(math.atan(-vy / vx))
        else:
            angle = 90
        arrow = pygame.transform.rotate(pygame.image.load('Data/arrow2.png'), angle)
        return Bullet(player.rect.x + player.width // 2,
                      player.rect.y + 30, arrow, dx, vx, 5,
                      'enemies', [group, bullets], vy)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, group):
        super().__init__(*group)
        self.image = ground_sprite
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player, group, all_sprites, tools, hp=10,
                 attack=None, idle=None, walk=None, death=None):
        super().__init__(*group)
        self.player = player
        self.hp = hp
        self.attackTrigger = False
        self.attackClock = 0

        self.frames_walk = walk
        self.frames_idle = idle
        self.frames_attack = attack
        self.frames_death = death
        self.frames = self.frames_idle
        self.rect = pygame.Rect(x, y, self.frames_idle[0].get_width(),
                                self.frames_idle[0].get_height())
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.y = ground.rect.y - self.frames[self.cur_frame].get_height()
        if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
            self.image = pygame.transform.flip(self.image, True, False)
        self.hpBar = HPbar(self, self.frames_idle[0].get_width(), 10, [all_sprites, tools])

    def update(self):
        if self.hp <= 0:
            money.amount += 1
            self.hpBar.kill()
            self.kill()
            return
        if self.rect.x + self.rect.width // 2 in \
                range(self.player.rect.x,
                      self.player.rect.x + self.player.rect.width):
            if not self.attackTrigger:
                self.cur_frame = -1
                self.frames = self.frames_attack
            self.attackTrigger = True
        else:
            self.attackTrigger = False
        if self.attackTrigger:
            self.attackClock += 1
            self.frames = self.frames_attack
            if collisionClock % 4 == 3:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.rect.y = ground.rect.y - self.frames[self.cur_frame].get_height()
                if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.attackClock == 4 * len(self.frames):
                self.attackClock = 0
                self.attackTrigger = False
                self.player.hp -= 5
                self.cur_frame = -1
            return
        if collisionClock % 3 == 2:
            self.frames = self.frames_walk
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.rect.y = ground.rect.y - self.frames[self.cur_frame].get_height()
            if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.image = pygame.transform.flip(self.image, True, False)
            if self.player.rect.x + self.player.width // 2 > self.rect.x + self.rect.width // 2:
                self.rect.x += 340 * speedPerFrame
            elif self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.rect.x -= 300 * speedPerFrame


class Boss(Enemy):
    def __init__(self, x, y, player, group, all_boss_sprites, tools, name, hp, fon,
                 attack=None, idle=None, walk=None, death=None):
        self.frames_idle = idle
        super().__init__(x, y, player, group, all_boss_sprites, tools, hp, attack=attack, idle=idle,
                         walk=walk, death=death)
        self.name = name
        self.hpBar.kill()
        self.hpBar = Boss_HPbar(self, [all_boss_sprites, tools])

        self.vy = 0
        self.attackClock = 0
        self.abilityClock = 0
        self.abilityTrigger = False
        self.attackTrigger = False
        self.deathTrigger = False
        self.fon = fon

    def draw_boss_name(self):
        screen.blit(self.fon, (-100, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(self.name, True, (200, 200, 200))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 8 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))

    def death(self):
        self.cur_frame = -1
        self.deathClock = 0
        self.deathTrigger = True
        self.frames = self.frames_death

    def update(self):
        if self.deathTrigger:
            if self.deathClock % 7 == 1:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
            if self.deathClock == len(self.frames) * 7:
                self.hpBar.kill()
                self.kill()
            self.deathClock += 1
            return
        if self.hp <= 0:
            money.amount += 100
            self.death()
            return
        if pygame.sprite.spritecollideany(self, player_group):
            if not self.attackTrigger:
                self.cur_frame = -1
                self.frames = self.frames_attack
            self.attackTrigger = True
        else:
            self.attackTrigger = False

    def walk(self):
        self.cur_frame = -1
        self.frames = self.frames_walk


class FireBoss(Boss):
    def update(self):
        super().update()
        if self.deathTrigger:
            return
        self.attackTrigger = True
        self.frames = self.frames_attack
        if collisionClock % 4 == 3:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.rect.y = boss_ground.rect.y - self.frames[self.cur_frame].get_height()
            if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.image = pygame.transform.flip(self.image, True, False)
        if collisionClock % 64 == 31:
            if player.rect.x < self.rect.x + self.rect.width // 2:
                d = - 1
            else:
                d = 1
            for i in range(5):
                n = abs(self.rect.x + self.rect.width // 2)
                x = random.randint(n - 50, n + 50)
                n = abs(n - self.player.rect.x - self.player.rect.width // 2)
                y = random.randint(self.rect.y + self.rect.height // 2 - n - 75, self.rect.y + self.rect.height // 2 - n + 75)
                Bullet(x, y,
                       pygame.image.load('Data/fireball/fireball50_35.png'),
                       d, 400, 10, 'player', [bullets, all_boss_sprites], 400)
        if collisionClock % 64 == 63:
            if player.rect.x < self.rect.x + self.rect.width // 2:
                d = - 1
            else:
                d = 1
            Bullet(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2,
                   pygame.image.load('Data/fireball/fireball50_35.png'),
                   d, 400, 10, 'player', [bullets, all_boss_sprites])
        if collisionClock % 5 == 0:
            if pygame.sprite.spritecollideany(self, player_group):
                player.hp -= 1


class Summoner(Boss):
    def update(self):
        super().update()
        if collisionClock % 75 == 59:
            enemy = Enemy(self.rect.x, self.rect.y, boss_ground.rect.y - 100, player, [all_sprites, enemies],
                          all_sprites, tools, hp=10, attack=easy_enemy_attack,
                          walk=easy_enemy_walk, idle=easy_enemy_idle)
        if collisionClock % 5 == 0:
            if pygame.sprite.spritecollideany(self, player_group):
                player.hp -= 1
        if self.player.rect.x + self.player.width // 2 > self.rect.x + self.rect.width // 2:
            self.rect.x += 40 * speedPerFrame
        elif self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
            self.rect.x -= 10 * speedPerFrame


class Ogre(Boss):
    def update(self):
        super().update()
        if self.deathTrigger:
            return
        self.abilityClock += 1
        if self.abilityClock == 270:
            self.abilityClock = 0
            self.cur_frame = -1
            self.abilityTrigger = True
        if self.abilityTrigger:
            self.frames = [*self.frames_attack, self.frames_attack[-1]]
            if self.abilityClock <= 20:
                self.vy -= 250 * speedPerFrame
            elif self.abilityClock > 20:
                self.vy += 250 * 20 / 15 * speedPerFrame
            if self.abilityClock % 4 == 3:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.rect.y = boss_ground.rect.y - self.frames[self.cur_frame].get_height() + self.vy
                if width // 2 < self.rect.x + self.rect.width // 2:
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.abilityClock == 35:
                self.vy = 0
                self.abilityTrigger = False
                self.cur_frame = -1
                if player.isGrounded:
                    player.hp -= min(175, int(300 / abs(player.rect.x - self.rect.x) ** 0.2))
            return
        if self.attackTrigger:
            self.attackClock += 1
            self.frames = self.frames_attack
            if collisionClock % 4 == 3:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.rect.y = boss_ground.rect.y - self.frames[self.cur_frame].get_height()
                if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.attackClock == 4 * len(self.frames):
                self.attackClock = 0
                self.attackTrigger = False
                self.player.hp -= 30
                self.cur_frame = -1
            return
        if collisionClock % 4 == 3:
            self.frames = self.frames_walk
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.rect.y = boss_ground.rect.y - self.frames[self.cur_frame].get_height()
            if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.image = pygame.transform.flip(self.image, True, False)
            if self.player.rect.x + self.player.width // 2 > self.rect.x + self.rect.width // 2:
                self.rect.x += 180 * speedPerFrame
            elif self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.rect.x -= 150 * speedPerFrame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image, direction, xspeed, damage, player, group, yspeed=0):
        super().__init__(*group)
        self.image = image
        self.direct = direction
        if self.direct == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # direction = +- 1
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.damage = damage
        if player == 'player':
            self.target = [player_group]
        elif player == 'enemies':
            self.target = [boss_group, enemies]

    def update(self):
        self.rect.x += self.direct * self.xspeed * speedPerFrame
        self.rect.y += self.yspeed * speedPerFrame
        for i in self.target:
            if i not in all_boss_sprites and condition_trigger == 4 or\
                    i not in all_sprites and condition_trigger == 2:
                continue
            target = pygame.sprite.spritecollideany(self, i)
            if pygame.sprite.spritecollideany(self, i):
                target.hp -= self.damage
                self.kill()
        if pygame.sprite.spritecollideany(self, ground_layer) or self.rect.y + self.rect.width < -1000 or\
                self.rect.y > 800:
            self.kill()


class HPbar(pygame.sprite.Sprite):
    def __init__(self, player, width, height, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(player.rect.x - width // 2, player.rect.y - height * 2, width, height)
        self.player = player
        self.hp_beg = player.hp
        self.hp = player.hp
        self.width = width
        self.height = height

    def update(self):
        self.rect = pygame.Rect(self.player.rect.x - self.rect.width // 2 + self.player.rect.width // 2,
                                self.player.rect.y - self.rect.height * 2, self.rect.width, self.rect.height)
        self.hp = self.player.hp
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, pygame.Color((255, 0, 0)),
                         [(1, 1), (self.width * int(self.hp) / self.hp_beg, height - 2)], width=0)


class Boss_HPbar(HPbar):
    def __init__(self, player, groups):
        super().__init__(player, 1000, 20, groups)
        self.rect = pygame.Rect(100, 150, 1000, 20)
        self.height = 20

    def update(self):
        self.hp = self.player.hp
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, pygame.Color((255, 0, 0)),
                         [(1, 1), (self.width * int(self.hp) / self.hp_beg, height - 2)], width=0)


class Money(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        self.image = pygame.Surface([0, 0])
        self.rect = pygame.Rect(50, 50, 0, 0)
        self.amount = 0

    def update(self):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Your balance: {self.amount}", True, (200, 200, 200))
        text_x = 50
        text_y = 50
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))


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


def newWave(typesOfEnemies):
    global waves
    waves += 1
    for i in range(waves):
        enemy = typesOfEnemies[random.randrange(0, len(typesOfEnemies), 1)]
        x = random.randrange(ground.rect.x, ground.rect.x + ground.rect.width - 50, 1)
        if enemy == 'goblin':
            enemy = Enemy(x, ground.rect.y - 100, player, [all_sprites, enemies],
                               all_sprites, tools, hp=10, attack=easy_enemy_attack,
                               walk=easy_enemy_walk, idle=easy_enemy_idle)
        elif enemy == 'giant':
            enemy = Enemy(x, ground.rect.y - 100, mainTower, [all_sprites, enemies],
                                all_sprites, tools, hp=25, attack=giant_enemy_attack,
                                walk=giant_enemy_walk, idle=giant_enemy_idle)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    image2 = pygame.image.load('Data/fon.png')
    # const
    running = True
    player_position = [width // 2, height // 2]
    horizontall_speed = 200
    vertical_speed = 500
    typesOfEnemies = ['goblin', 'giant']
    condition_trigger = -1
    collisionClock = 0
    time = 0
    camera = Camera()
    # New logo
    i = 0
    image = pygame.image.load('Data/the_best_logo_you_ever_seen/name/0.gif')
    colorkey = image.get_at((0, 0))
    screen.fill(colorkey)
    screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/authors/0.gif'), (300, 400))
    screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/name/0.gif'), (300, 200))
    pygame.draw.rect(screen, (0, 0, 0), ((200, 600), (800, 30)), 1)
    fps = 60

    while running:
        speedPerFrame = clock.tick(fps) / 1000
        if condition_trigger == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            condition_trigger = 0
            fps = 30
            i += 1
            if i == 600:
                fps = 30
                condition_trigger = 0
            elif i < 303 + 222 + 1:
                logo(screen, width, height)

        if condition_trigger == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    start_pos, continue_pos, exit_pos = menuScreen(screen, width, height, colorkey)
                    if start_pos[0] <= x <= start_pos[2] and start_pos[1] <= y <= start_pos[3]:
                        print('start')
                        collisionClock = 0
                        time = 1
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
                        mainTower = MainTower(width // 8 * 2.5, height // 10, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 500,
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
                    elif exit_pos[0] <= x <= exit_pos[2] and exit_pos[1] <= y <= exit_pos[3]:
                        running = False
            menuScreen(screen, width, height, colorkey)

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
                        elif event.key == pygame.K_q:
                            shop_trigger = True
                    elif event.type == pygame.KEYUP:
                        # horizontal move begin
                        if event.key == pygame.K_RIGHT:
                            right_trigger = False
                        elif event.key == pygame.K_LEFT:
                            left_trigger = False
                        # horizontal move end

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and\
                                event.pos[0] > portal.rect.x and\
                                event.pos[0] < portal.rect.x + portal.rect.width and\
                                event.pos[1] > portal.rect.y and\
                                event.pos[1] < portal.rect.y + portal.rect.height:
                            # Я знаю что это отвратительно и бессовестно, но что поделать
                            if True:
                                name = 'Wizard'
                                boss = FireBoss(width - 200, height // 8 * 4, player,
                                                [all_boss_sprites, boss_group], all_boss_sprites,
                                                tools, name, 100, pygame.image.load('Data/fon4.png'),
                                                attack=fire_boss_attack, idle=fire_boss_idle, death=fire_boss_death)
                                boss_ground = Ground(0, height // 4 * 3 - 50, width, [all_boss_sprites, ground_layer])
                                condition_trigger = 4
                                f1 = False
                                collisionClock = 0
                                ground.kill()
                                continue
                            name = 'Ogre'
                            boss = Ogre(width - 200, height // 8 * 4, player,
                                            [all_boss_sprites, boss_group], all_boss_sprites,
                                            tools, name, 300, pygame.image.load('Data/fon3.png'),
                                            attack=ogre_boss_attack, walk=ogre_boss_walk,
                                            idle=ogre_boss_idle, death=ogre_boss_death)
                            boss_ground = Ground(0, height // 8 * 7, width, [all_boss_sprites, ground_layer])
                            condition_trigger = 4
                            f1 = False
                            collisionClock = 0
                            ground.kill()
                            continue
                            # Конец этого ужаса
                        elif event.button == 1 and not player.attackTrigger:
                            player.hit(event.pos)
                        elif event.button == 3 and not player.attackTrigger:
                            x1, y1 = event.pos
                            x2, y2 = player.rect.x + player.width // 2, player.rect.y + player.height // 2
                            player.hit(event.pos, coords=(x1, y1, x2, y2), group=all_sprites)
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
                if int(time) % 6 == 0:
                    time += 1
                    newWave(typesOfEnemies)
                # Main act
                screen.fill((0, 0, 0))
                screen.blit(image2, (-350, -125))
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
                            ground = Ground(0, height // 4 * 3, width, [all_sprites, ground_layer])
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        right_trigger = False
                    elif event.key == pygame.K_LEFT:
                        left_trigger = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not player.attackTrigger:
                        player.hit(event.pos)
                    elif event.button == 3 and not player.attackTrigger:
                        x1, y1 = event.pos
                        x2, y2 = player.rect.x + player.width // 2, player.rect.y + player.height // 2
                        player.hit(event.pos, coords=(x1, y1, x2, y2), group=all_boss_sprites)
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
            # Main act
            screen.fill((0, 0, 0))
            boss.draw_boss_name()
            all_boss_sprites.draw(screen)
            all_boss_sprites.update()

        collisionClock += 1
        time += speedPerFrame

        pygame.display.flip()
    pygame.quit()