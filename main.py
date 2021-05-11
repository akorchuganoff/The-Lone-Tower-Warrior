# mainloop
import pygame
import random
import math
import json
import schedule

from dead_screen import deadScreen
from PortalClass import Portal

player_walk = [pygame.image.load('Data/main hero/run/' +
                                 str(i + 1) + '.png') for i in range(5)]

player_idle = [pygame.image.load('Data/main hero/idle.png')]

player_attack = [pygame.image.load('Data/main hero/attack/' +
                                   str(i + 1) + '.png') for i in range(5)]

player_jump = [pygame.image.load('Data/main hero/jump/' +
                                 str(i + 1) + '.png') for i in range(5)]

player_death = [pygame.image.load('Data/main hero/death/' +
                                  str(i + 1) + '.png') for i in range(5)]

easy_enemy_walk = [pygame.image.load('Data/easy enemy/walk/' +
                                     str(i + 1) + '.png') for i in range(7)]

easy_enemy_idle = [pygame.image.load('Data/easy enemy/ide.png')]

easy_enemy_attack = [pygame.image.load('Data/easy enemy/attack/' +
                                       str(i + 1) + '.png') for i in range(7)]

giant_enemy_walk = [pygame.image.load('Data/giant enemy/walk/' +
                                      str(i + 1) + '.png') for i in range(7)]

giant_enemy_idle = [pygame.image.load('Data/giant enemy/idle.png')]

giant_enemy_attack = [pygame.image.load('Data/giant enemy/attack/' +
                                        str(i + 1) + '.png') for i in range(7)]

fire_boss_idle = [pygame.image.load('Data/fire boss/idle.png')]

fire_boss_attack = [pygame.image.load('Data/fire boss/attack/' +
                                      str(i + 1) + '.png') for i in range(3)] + \
                   [pygame.image.load('Data/fire boss/attack/' +
                                      str(i + 1) + '.png') for i in range(5)]

fire_boss_death = [pygame.image.load('Data/fire boss/death/' +
                                     str(i + 1) + '.png') for i in range(5)]

ogre_boss_idle = [pygame.image.load('Data/ogr boss/idle.png')]

ogre_boss_attack = [pygame.image.load('Data/ogr boss/attack/' +
                                      str(i + 1) + '.png') for i in range(7)]

ogre_boss_death = [pygame.image.load('Data/ogr boss/death/' +
                                     str(i + 1) + '.png') for i in range(7)]

ogre_boss_walk = [pygame.image.load('Data/ogr boss/walk/' +
                                    str(i + 1) + '.png') for i in range(7)]

summoner_boss_idle = [pygame.image.load('Data/summoner boss/idle.png')]

summoner_boss_attack = [pygame.image.load('Data/summoner boss/attack/' +
                                          str(i + 1) + '.png') for i in range(7)]

summoner_boss_death = [pygame.image.load('Data/summoner boss/death/' +
                                         str(i + 1) + '.png') for i in range(7)]

summoner_boss_walk = [pygame.image.load('Data/summoner boss/walk/' +
                                        str(i + 1) + '.png') for i in range(7)]

ground_sprite = pygame.image.load('Data/env/ground.png')
border_sprite = pygame.image.load('Data/env/tree.png')


def logo(screen, width, height):
    if i > 222:
        k = i - 222
        screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/authors/' + str(k) + '.gif'),
                    (300, 400))
    else:
        screen.blit(pygame.image.load('Data/the_best_logo_you_ever_seen/name/' + str(i) + '.gif'),
                    (300, 200))
    pygame.draw.rect(screen, pygame.Color('#ffd700'),
                     ((201, 601), ((800 * i // (303 + 222 + 1) - 2), 30 - 2)))


def menuScreen(screen, width, height, colorkey, cont=False):
    screen.fill(colorkey)
    if not cont:
        screen.blit(pygame.image.load('Data/menu/no continue2.gif'), (300, 100))
    else:
        screen.blit(pygame.image.load('Data/menu/continue.gif'), (300, 100))
    screen.blit(pygame.image.load('Data/menu/new game.gif'), (300, 250))
    screen.blit(pygame.image.load('Data/menu/exit.gif'), (300, 400))
    start_pos, continue_pos, exit_pos = (500, 300, 700, 380), (500, 160, 700, 240), (500, 470, 700, 540)
    return start_pos, continue_pos, exit_pos


def menuBoss(screen, curBoss):
    screen.blit(pygame.image.load('Data/menu/boss menu.png'), (0, 0))
    for i in range(3 - curBoss):
        screen.blit(pygame.image.load('Data/menu/locked1.png'), (200 + 350 * (2 - i), 340))
        screen.blit(pygame.image.load('Data/menu/locked.gif'), (185 + 350 * (2 - i), 260))
    if curBoss == 1:
        screen.blit(pygame.image.load('Data/menu/summoner.gif'), (150, 380))
    if curBoss == 2:
        screen.blit(pygame.image.load('Data/menu/wizard.gif'), (530, 378))
        screen.blit(pygame.image.load('Data/menu/summoner(killed).gif'), (150, 380))
    if curBoss == 3:
        screen.blit(pygame.image.load('Data/menu/ogre.gif'), (893, 374))
        screen.blit(pygame.image.load('Data/menu/wizard(killed).gif'), (530, 378))
        screen.blit(pygame.image.load('Data/menu/summoner(killed).gif'), (150, 380))
    if curBoss >= 4:
        screen.blit(pygame.image.load('Data/menu/ogre(killed).gif'), (893, 378))
        screen.blit(pygame.image.load('Data/menu/wizard(killed).gif'), (530, 378))
        screen.blit(pygame.image.load('Data/menu/summoner(killed).gif'), (150, 380))


def shopScreen1(screen):
    screen.blit(pygame.image.load('Data/shop/menu.png'), (0, 0))
    screen.blit(pygame.image.load('Data/shop/sword.png'), (125, 119))
    screen.blit(pygame.image.load('Data/shop/heart.png'), (500, 130))
    screen.blit(pygame.image.load('Data/shop/tower.png'), (925, 125))
    screen.blit(pygame.image.load('Data/shop/heart.png'), (125, 130 + 375))
    screen.blit(pygame.image.load('Data/shop/tower.png'), (175, 130 + 375))
    screen.blit(pygame.image.load('Data/shop/potion.png'), (475 + 48, 130 + 375))
    screen.blit(pygame.image.load('Data/shop/bow.png'), (125 + 375 * 2, 125 + 375))

    screen.blit(pygame.image.load('Data/shop/attack.gif'), (159, 68))
    screen.blit(pygame.image.load('Data/shop/health.gif'), (161 + 375, 69))
    screen.blit(pygame.image.load('Data/shop/tower.gif'), (170 + 375 * 2, 68))
    # heal tower
    screen.blit(pygame.image.load('Data/shop/heal.gif'), (120, 69 + 375))
    screen.blit(pygame.image.load('Data/shop/tower.gif'), (220, 68 + 375))
    #
    screen.blit(pygame.image.load('Data/shop/potion.gif'), (475 + 65, 68 + 375))
    screen.blit(pygame.image.load('Data/shop/arrows.gif'), (475 + 375 + 29, 66 + 375))

    font = pygame.font.Font(None, 50)
    balance_text_x1 = 100
    balance_text_x2 = 100 + 375
    balance_text_x3 = 100 + 375 * 2
    balance_text_y1 = 360
    balance_text_y2 = 360 + 375

    balance_text = font.render(f"Upgrage cost: {attack_upgrade_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x1, balance_text_y1))

    balance_text = font.render(f"Upgrage cost: {health_upgrade_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x2, balance_text_y1))

    balance_text = font.render(f"Upgrage cost: {tower_upgrade_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x3, balance_text_y1))

    balance_text = font.render(f"Heal cost: {heal_tower_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x1 + 25, balance_text_y2))

    balance_text = font.render(f"Upgrage cost: {potion_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x2, balance_text_y2))

    balance_text = font.render(f"Upgrage cost: {arrows_cost}", True, (200, 200, 200))
    screen.blit(balance_text, (balance_text_x3, balance_text_y2))


def end_game(screen):
    pass


class MainTower(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, group, all_sprites, tools):
        super().__init__(*group)
        self.image = pygame.image.load('Data/tower2.png')
        self.rect = pygame.Rect(int(x), int(y), int(self.image.get_width()), int(self.image.get_height()))
        self.width = self.rect.width
        self.height = self.rect.height
        self.fullhp = hp
        self.hp = hp
        self.MainTowerHPbar = HPbar(self, 500, 20, [all_sprites, tools])
        self.damage = 0

    def update(self):
        if collisionClock % 60 == 0:
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
        self.fullhp = hp
        self.hp = hp
        self.PlayerHPbar = HPbar(self, self.frames_idle[0].get_width(), 10, [all_sprites, tools, all_boss_sprites])
        self.width = self.frames_idle[0].get_width()
        self.height = self.frames_idle[0].get_height()
        self.damage = 4
        self.step = 0
        self.arrows = 20
        self.potions = 1

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
                    self.archeryTrigger = False
                    if self.arrows == 0:
                        return
                    pygame.mixer.Sound('Data/sounds/bow_jump.mp3').play()
                    self.archery(*self.archery_coords, self.archery_group)
                    self.arrows -= 1
                    return
                fsoundhit = False
                target1 = pygame.sprite.spritecollideany(self, enemies)
                target2 = pygame.sprite.spritecollideany(self, boss_group)
                if target1:
                    target1.hp -= self.damage
                    fsoundhit = True
                elif target2:
                    target2.hp -= self.damage
                    fsoundhit = True
                if fsoundhit:
                    pygame.mixer.Sound('Data/sounds/hit.mp3').play()
            return
        if pygame.sprite.spritecollideany(self, ground_layer):
            self.isGrounded = True
            if self.vx == 0 and collisionClock % 5 == 0:
                self.image = self.frames_idle[0]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
            elif collisionClock % 5 == 0:
                if collisionClock % 10 == 0:
                    pygame.mixer.Sound('Data/sounds/steps/stone' + str(self.step % 6 + 1) + '.mp3').play()
                    self.step += 1
                self.frames = self.frames_walk
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if last_move == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
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
                      player.rect.y + 30, arrow, dx, vx, round(self.damage * 0.6),
                      'enemies', [group, bullets], vy)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, group, sprite=False):
        super().__init__(*group)
        if sprite != False:
            self.image = ground_sprite
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        else:
            self.image = pygame.Surface([width, 5])
            self.rect = pygame.Rect(x, y, width, 5)
            self.image.fill((255, 255, 255))
            self.image.set_alpha(0)


class VerticalBorder(pygame.sprite.Sprite):
    def __init__(self, x, y, height, player, groups, sprite=False):
        super().__init__(*groups)
        self.player = player
        if sprite:
            self.image = border_sprite
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        else:
            self.image = pygame.Surface([40, height])
            self.rect = pygame.Rect(x, y, 40, height)
            self.image.fill((255, 255, 255))
            self.image.set_alpha(0)

    def update(self):
        global left_trigger
        global right_trigger
        if self.rect.x + self.rect.w // 4 <= self.player.rect.x <= self.rect.x + self.rect.w // 9 * 4:
            if self.player.rect.x >= self.rect.x + self.rect.w // 3:
                left_trigger = False
            else:
                right_trigger = False


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
            money.amount += 2
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
                pygame.mixer.Sound('Data/sounds/hit.mp3').play()
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
        text = font.render(self.name, True, (32, 28, 43))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 8 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))

    def death(self):
        global isAlive
        self.cur_frame = -1
        self.deathClock = 0
        self.deathTrigger = True
        self.frames = self.frames_death
        isAlive = False
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.load('Data/sounds/boss win.mp3')
        pygame.mixer.music.play(loops=0)

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
            if name == 'Summoner' and curBoss == 1:
                money.amount += 300
            elif name == 'Wizard' and curBoss == 2:
                money.amount += 500
            elif name == 'Ogre' and curBoss == 3:
                money.amount += 1000
            self.death()
            return
        if pygame.sprite.spritecollideany(self, player_group):
            if not self.attackTrigger:
                self.cur_frame = -1
                self.frames = self.frames_attack
            self.attackTrigger = True
        else:
            self.attackTrigger = False


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
                y = random.randint(self.rect.y + self.rect.height // 2 - n - 75,
                                   self.rect.y + self.rect.height // 2 - n + 75)
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
        if self.deathTrigger:
            return
        self.abilityClock += 1
        if self.abilityClock == 118:
            pygame.mixer.Sound('Data/sounds/summoner sound.mp3').play()
            self.abilityClock = 0
            self.abilityTrigger = True
        if self.abilityTrigger:
            self.frames = self.frames_attack
            if self.abilityClock % 4 == 3:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.rect.y = boss_ground.rect.y - self.frames[self.cur_frame].get_height() + self.vy
                if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.abilityClock == 28:
                enemy = Enemy(self.rect.x, boss_ground.rect.y - 100, player, [all_boss_sprites, enemies],
                              all_boss_sprites, tools, hp=10, attack=easy_enemy_attack,
                              walk=easy_enemy_walk, idle=easy_enemy_idle)
                self.abilityTrigger = False
                self.cur_frame = -1
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
                pygame.mixer.Sound('Data/sounds/hit.mp3').play()
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
                self.rect.x += 280 * speedPerFrame
            elif self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                self.rect.x -= 250 * speedPerFrame


class Ogre(Boss):
    def update(self):
        super().update()
        if self.deathTrigger:
            return
        self.abilityClock += 1
        if self.abilityClock % 90 == 0:
            pygame.mixer.Sound('Data/sounds/ogre sound.mp3').play()
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
                if self.player.rect.x + self.player.width // 2 < self.rect.x + self.rect.width // 2:
                    self.image = pygame.transform.flip(self.image, True, False)
            if self.abilityClock == 35:
                pygame.mixer.Sound('Data/sounds/ogre sound2.mp3').play()
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
                pygame.mixer.Sound('Data/sounds/hit.mp3').play()
                self.attackClock = 0
                self.attackTrigger = False
                self.player.hp -= 40
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
            if i not in all_boss_sprites and condition_trigger == 4 or \
                    i not in all_sprites and condition_trigger == 2:
                continue
            target = pygame.sprite.spritecollideany(self, i)
            if pygame.sprite.spritecollideany(self, i):
                if self.target == [player_group]:
                    s = pygame.mixer.Sound('Data/sounds/explode.mp3')
                    s.set_volume(0.5)
                    s.play()
                elif self.target == [boss_group, enemies]:
                    pygame.mixer.Sound('Data/sounds/bowhit2.mp3').play()
                target.hp -= self.damage
                self.kill()
        if pygame.sprite.spritecollideany(self, ground_layer):
            if self.target == [player_group]:
                s = pygame.mixer.Sound('Data/sounds/explode.mp3')
                s.set_volume(0.5)
                s.play()
            elif self.target == [boss_group, enemies]:
                pygame.mixer.Sound('Data/sounds/bowhit.mp3').play()
            self.kill()
        if self.rect.y + self.rect.width < -1000 or self.rect.y > 800:
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
        text = font.render(f"Your balance: {self.amount}", True, (32, 28, 43))
        text_x = 100
        text_y = 50
        screen.blit(text, (text_x, text_y))


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 4 * 3)


def newWave(typesOfEnemies):
    global waves
    waves += 1
    for i in range(min(waves, 4)):
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


def savegame():
    global player, mainTower, attack_upgrade_cost, health_upgrade_cost, tower_upgrade_cost, curBoss, waves, money
    with open('Data/save.json') as jsonfile:
        data = json.load(jsonfile)

    if condition_trigger != 2:
        return

    # money
    data['money_amount'] = money.amount
    # player
    data['arrows'] = player.arrows
    data['potion'] = player.potions
    data['hp'] = player.hp
    data['damage'] = player.damage
    # mainTower
    data['main_tower_hp'] = mainTower.hp
    data['main_tower_damage'] = mainTower.damage
    # shop
    data['attack_upgrade_cost'] = attack_upgrade_cost
    data['health_upgrade_cost'] = health_upgrade_cost
    data['tower_upgrade_cost'] = tower_upgrade_cost
    # other
    data['curBoss'] = curBoss
    data['waves'] = waves
    for key, value in data.items():
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')
    with open('Data/save.json', mode='w') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)


def upload_game():
    global player, mainTower, money
    with open('Data/save.json') as jsonfile:
        data = json.load(jsonfile)

    global player, mainTower, attack_upgrade_cost, health_upgrade_cost, tower_upgrade_cost, curBoss, waves, money, condition_trigger

    with open('Data/save.json') as jsonfile:
        data = json.load(jsonfile)

    # money
    money.amount = data['money_amount']
    # player
    player.arrows = data['arrows']
    player.potions = data['potion']
    player.hp = data['hp']
    player.damage = data['damage']
    # mainTower
    mainTower.hp = data['main_tower_hp']
    mainTower.damage = data['main_tower_damage']
    # shop
    attack_upgrade_cost = data['attack_upgrade_cost']
    health_upgrade_cost = data['health_upgrade_cost']
    tower_upgrade_cost = data['tower_upgrade_cost']
    # other
    curBoss = data['curBoss']
    waves = data['waves']


def new_game_session():
    with open('Data/save.json') as jsonfile:
        data = json.load(jsonfile)

    # money
    data['money_amount'] = 0
    # player
    data['arrows'] = 20
    data['potion'] = 1
    data['hp'] = 500
    data['damage'] = 4
    # mainTower
    data['main_tower_hp'] = 1000
    data['main_tower_damage'] = 0
    # shop
    data['attack_upgrade_cost'] = 10
    data['health_upgrade_cost'] = 10
    data['tower_upgrade_cost'] = 10
    # other
    data['curBoss'] = 1
    data['waves'] = 0

    with open('Data/save.json', mode='w') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)


if __name__ == '__main__':
    pygame.mixer.pre_init(48000, -16, 1, 1024)
    pygame.mixer.init()
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    # standard images
    image2 = pygame.image.load('Data/fon.png')
    pause = pygame.image.load('Data/pause.png')
    potions = pygame.image.load('Data/potions.png')
    arrows = pygame.image.load('Data/arrows.png')
    # main consts
    running = True
    player_position = [width // 2, height // 2]
    horizontall_speed = 200
    vertical_speed = 500
    typesOfEnemies = ['goblin', 'giant']
    # conditions and clocks
    clock = pygame.time.Clock()
    condition_trigger = 0
    first_time_trigger = True
    boss_trigger = False
    collisionClock = 0
    time = 10
    # is available continue button
    with open('Data/save.txt', mode='r') as file:
        f = file.readlines()
    if len(f) != 0:
        fcont = True
    else:
        fcont = False
    # camera?
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

    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('Data/sounds/menu music.mp3')
    pygame.mixer.music.play(loops=-1)
    # del old notes
    f = open("Data/coords save.txt", 'w')
    f.close()
    schedule.every(3).minutes.do(savegame)

    while running:
        schedule.run_pending()
        speedPerFrame = clock.tick(fps) / 1000
        if condition_trigger == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                    start_pos, continue_pos, exit_pos = menuScreen(screen, width, height, colorkey, cont=fcont)
                    if start_pos[0] <= x <= start_pos[2] and start_pos[1] <= y <= start_pos[3]:
                        collisionClock = 0
                        condition_trigger = 2
                        # start game
                        all_sprites = pygame.sprite.Group()
                        all_boss_sprites = pygame.sprite.Group()
                        boss_group = pygame.sprite.Group()
                        maintowergroup = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        tools = pygame.sprite.Group()
                        portal_group = pygame.sprite.Group()

                        money = Money([all_sprites, tools])
                        mainTower = MainTower(width * 2.5 // 8, height // 10, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 500,
                                        [all_sprites, player_group, all_boss_sprites], all_sprites, tools)
                        leftBD = VerticalBorder(-300, 100, 400, player, [all_sprites], sprite=True)
                        rightBD = VerticalBorder(1200, 100, 400, player, [all_sprites], sprite=True)
                        ground = Ground(-700, height // 4 * 3, width, [all_sprites, ground_layer], sprite=True)

                        waves = 0
                        curBoss = 1
                        portal = Portal([all_sprites, portal_group])
                        new_game_session()
                        # movement triggers
                        right_trigger = False
                        left_trigger = False
                        jump_trigger = False
                        shop_trigger = False
                        last_move = 'right'
                        # shop consts
                        attack_upgrade_cost = 10
                        health_upgrade_cost = 10
                        tower_upgrade_cost = 10
                        heal_tower_cost = 50
                        potion_cost = 50
                        arrows_cost = 20
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Data/sounds/castle music.mp3')
                        pygame.mixer.music.play(loops=-1)
                    elif fcont and continue_pos[0] <= x <= continue_pos[2] and \
                            continue_pos[1] <= y <= continue_pos[3]:
                        if first_time_trigger or boss_trigger:
                            first_time_trigger = False
                            boss_trigger = False
                            collisionClock = 0
                            condition_trigger = 2
                            # start game
                            all_sprites = pygame.sprite.Group()
                            all_boss_sprites = pygame.sprite.Group()
                            boss_group = pygame.sprite.Group()
                            maintowergroup = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            ground_layer = pygame.sprite.Group()
                            enemies = pygame.sprite.Group()
                            bullets = pygame.sprite.Group()
                            tools = pygame.sprite.Group()
                            portal_group = pygame.sprite.Group()

                            money = Money([all_sprites, tools])
                            mainTower = MainTower(width * 2.5 // 8, height // 10, 1000,
                                                  [all_sprites, maintowergroup], all_sprites, tools)
                            player = Player(player_position[0], player_position[1], 500,
                                            [all_sprites, player_group, all_boss_sprites], all_sprites, tools)
                            leftBD = VerticalBorder(-300, 100, 400, player, [all_sprites], sprite=True)
                            rightBD = VerticalBorder(1200, 100, 400, player, [all_sprites], sprite=True)
                            ground = Ground(-700, height // 4 * 3, width, [all_sprites, ground_layer], sprite=True)

                            waves = 0
                            curBoss = 1
                            portal = Portal([all_sprites, portal_group])
                            # movement triggers
                            right_trigger = False
                            left_trigger = False
                            jump_trigger = False
                            shop_trigger = False
                            last_move = 'right'
                            # shop consts
                            attack_upgrade_cost = 10
                            health_upgrade_cost = 10
                            tower_upgrade_cost = 10
                            heal_tower_cost = 50
                            potion_cost = 50
                            arrows_cost = 20
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.load('Data/sounds/castle music.mp3')
                            pygame.mixer.music.play(loops=-1)
                            upload_game()
                        else:
                            # it indicates whether to return (to the boss or to the castle)
                            condition_trigger = last_condition

                    elif exit_pos[0] <= x <= exit_pos[2] and exit_pos[1] <= y <= exit_pos[3]:
                        running = False
            menuScreen(screen, width, height, colorkey, cont=fcont)

        elif condition_trigger == 2:
            if not shop_trigger:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        # horizontal move
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            right_trigger = True
                            left_trigger = False
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            right_trigger = False
                            left_trigger = True
                        # vertical move
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            s = pygame.mixer.Sound('Data/sounds/bow_jump.mp3')
                            s.set_volume(0.5)
                            s.play()
                            jump_trigger = True
                        # shop
                        elif event.key == pygame.K_q:
                            shop_trigger = True
                        # use potion
                        elif event.key == pygame.K_e:
                            if player.potions > 0 and player.hp != player.fullhp:
                                player.potions -= 1
                                player.hp = min(player.fullhp, round(player.fullhp * 0.2) + player.hp)
                        # pause
                        elif event.key == pygame.K_ESCAPE:
                            condition_trigger = 0
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.load('Data/sounds/castle music.mp3')
                            pygame.mixer.music.play(loops=-1)
                            fcont = True
                            last_condition = 2
                            continue

                    elif event.type == pygame.KEYUP:
                        # horizontal move
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            right_trigger = False
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            left_trigger = False
                        # pause
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # pause
                        if event.button == 1 and \
                                event.pos[0] > 10 and \
                                event.pos[0] < 60 and \
                                event.pos[1] > 10 and \
                                event.pos[1] < 64:
                            condition_trigger = 0
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.load('Data/sounds/castle music.mp3')
                            pygame.mixer.music.play(loops=-1)
                            fcont = True
                            last_condition = 2
                            continue
                        # boss choose
                        elif event.button == 1 and \
                                event.pos[0] > portal.rect.x and \
                                event.pos[0] < portal.rect.x + portal.rect.width and \
                                event.pos[1] > portal.rect.y and \
                                event.pos[1] < portal.rect.y + portal.rect.height:
                            condition_trigger = 5
                            continue
                        # hit
                        elif event.button == 1 and not player.attackTrigger:
                            player.hit(event.pos)
                        # bow shot
                        elif event.button == 3 and not player.attackTrigger:
                            x1, y1 = event.pos
                            x2, y2 = player.rect.x + player.width // 2, player.rect.y + player.height // 2
                            player.hit(event.pos, coords=(x1, y1, x2, y2), group=all_sprites)
                if player.hp <= 0 or mainTower.hp <= 0:
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.load('Data/sounds/menu music.mp3')
                    pygame.mixer.music.play(loops=-1)
                    condition_trigger = 3
                # horizontal move
                if left_trigger:
                    player.vx = -1 * horizontall_speed * speedPerFrame
                    last_move = 'left'
                elif right_trigger:
                    player.vx = horizontall_speed * speedPerFrame
                    last_move = 'right'
                else:
                    player.vx = 0
                # vertical move
                if jump_trigger:
                    if player.isGrounded:
                        vertical_speed = -450
                        player.vy = vertical_speed * speedPerFrame
                    jump_trigger = False
                else:
                    if vertical_speed >= 300:
                        vertical_speed = 300
                    else:
                        vertical_speed += 20
                    player.vy = vertical_speed * speedPerFrame
                # enemies spawnww
                if int(time) % 15 == 0:
                    time += 1
                    newWave(typesOfEnemies)
                screen.fill((0, 0, 0))
                screen.blit(image2, (-350, -125))
                all_sprites.draw(screen)
                screen.blit(pause, (10, 10))
                font = pygame.font.Font(None, 40)
                text = font.render(str(player.arrows), True, (32, 28, 43))
                screen.blit(text, (70, 80))
                text = font.render(str(player.potions), True, (32, 28, 43))
                screen.blit(text, (70, 140))
                screen.blit(arrows, (10, 80))
                screen.blit(potions, (10, 140))
                all_sprites.update()

                camera.update(player)
                for sprite in all_sprites:
                    if sprite != money:
                        camera.apply(sprite)

            else:
                # shop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            shop_trigger = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = event.pos
                        if pos[0] in range(100, 250 + 75) and pos[1] in range(100, 250 + 100):
                            if money.amount >= attack_upgrade_cost:
                                money.amount -= attack_upgrade_cost
                                player.damage += 2
                                attack_upgrade_cost += 10
                        elif pos[0] in range(475, 250 + 475) and pos[1] in range(100, 250 + 100):
                            if money.amount >= health_upgrade_cost:
                                money.amount -= health_upgrade_cost
                                player.fullhp += 20
                                health_upgrade_cost += 10
                        elif pos[0] in range(850, 250 + 850) and pos[1] in range(100, 250 + 100):
                            if money.amount >= tower_upgrade_cost:
                                money.amount -= tower_upgrade_cost
                                mainTower.damage += 2
                                mainTower.fullhp += 30
                                tower_upgrade_cost += 10
                        elif pos[0] in range(100, 250 + 75) and pos[1] in range(475, 250 + 475):
                            if money.amount >= heal_tower_cost:
                                money.amount -= heal_tower_cost
                                mainTower.hp += mainTower.fullhp * 0.2
                                if mainTower.hp > mainTower.fullhp:
                                    mainTower.hp = mainTower.fullhp
                        elif pos[0] in range(475, 250 + 475) and pos[1] in range(475, 250 + 475):
                            if money.amount >= potion_cost:
                                money.amount -= potion_cost
                                player.potions += 1
                        elif pos[0] in range(850, 250 + 850) and pos[1] in range(475, 250 + 475):
                            if money.amount >= arrows_cost:
                                money.amount -= arrows_cost
                                player.arrows += 5
                shopScreen1(screen)
            savegame()

        elif condition_trigger == 3:
            deadScreen(screen, width, height)
            fcont = True
            for elem in all_sprites:
                elem.kill()
            for elem in all_boss_sprites:
                elem.kill()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    start_pos, continue_pos, exit_pos = menuScreen(screen, width, height, colorkey, cont=fcont)
                    if start_pos[0] <= x <= start_pos[2] and start_pos[1] <= y <= start_pos[3]:
                        collisionClock = 0
                        condition_trigger = 2
                        # start game
                        all_sprites = pygame.sprite.Group()
                        all_boss_sprites = pygame.sprite.Group()
                        boss_group = pygame.sprite.Group()
                        maintowergroup = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ground_layer = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        tools = pygame.sprite.Group()
                        portal_group = pygame.sprite.Group()

                        money = Money([all_sprites, tools])
                        mainTower = MainTower(width * 2.5 // 8, height // 10, 1000,
                                              [all_sprites, maintowergroup], all_sprites, tools)
                        player = Player(player_position[0], player_position[1], 500,
                                        [all_sprites, player_group, all_boss_sprites], all_sprites, tools)
                        leftBD = VerticalBorder(-300, 100, 400, player, [all_sprites], sprite=True)
                        rightBD = VerticalBorder(1200, 100, 400, player, [all_sprites], sprite=True)
                        ground = Ground(-700, height // 4 * 3, width, [all_sprites, ground_layer], sprite=True)

                        waves = 0
                        curBoss = 1
                        portal = Portal([all_sprites, portal_group])
                        new_game_session()
                        # movement triggers
                        right_trigger = False
                        left_trigger = False
                        jump_trigger = False
                        shop_trigger = False
                        last_move = 'right'
                        # shop consts
                        attack_upgrade_cost = 10
                        health_upgrade_cost = 10
                        tower_upgrade_cost = 10
                        heal_tower_cost = 50
                        potion_cost = 50
                        arrows_cost = 20
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Data/sounds/castle music.mp3')
                        pygame.mixer.music.play(loops=-1)
                    elif fcont and continue_pos[0] <= x <= continue_pos[2] and \
                            continue_pos[1] <= y <= continue_pos[3]:
                        if first_time_trigger or boss_trigger:
                            first_time_trigger = False
                            boss_trigger = False
                            collisionClock = 0
                            condition_trigger = 2
                            # start game
                            all_sprites = pygame.sprite.Group()
                            all_boss_sprites = pygame.sprite.Group()
                            boss_group = pygame.sprite.Group()
                            maintowergroup = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            ground_layer = pygame.sprite.Group()
                            enemies = pygame.sprite.Group()
                            bullets = pygame.sprite.Group()
                            tools = pygame.sprite.Group()
                            portal_group = pygame.sprite.Group()

                            money = Money([all_sprites, tools])
                            mainTower = MainTower(width * 2.5 // 8, height // 10, 1000,
                                                  [all_sprites, maintowergroup], all_sprites, tools)
                            player = Player(player_position[0], player_position[1], 500,
                                            [all_sprites, player_group, all_boss_sprites], all_sprites, tools)
                            leftBD = VerticalBorder(-300, 100, 400, player, [all_sprites], sprite=True)
                            rightBD = VerticalBorder(1200, 100, 400, player, [all_sprites], sprite=True)
                            ground = Ground(-700, height // 4 * 3, width, [all_sprites, ground_layer], sprite=True)

                            waves = 0
                            curBoss = 1
                            portal = Portal([all_sprites, portal_group])
                            # movement triggers
                            right_trigger = False
                            left_trigger = False
                            jump_trigger = False
                            shop_trigger = False
                            last_move = 'right'
                            # shop consts
                            attack_upgrade_cost = 10
                            health_upgrade_cost = 10
                            tower_upgrade_cost = 10
                            heal_tower_cost = 50
                            potion_cost = 50
                            arrows_cost = 20
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.load('Data/sounds/castle music.mp3')
                            pygame.mixer.music.play(loops=-1)
                            upload_game()
                        else:
                            # it indicates whether to return (to the boss or to the castle)
                            condition_trigger = last_condition

                    elif exit_pos[0] <= x <= exit_pos[2] and exit_pos[1] <= y <= exit_pos[3]:
                        running = False
            menuScreen(screen, width, height, colorkey, cont=fcont)

        elif condition_trigger == 4:
            boss_trigger = True
            if not f1:
                player.rect.y -= 200
                f1 = True
            if player.rect.x < 0:
                player.rect.x = 0
            if player.rect.x > 1150:
                player.rect.x = 1150
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        last_move = 'right'
                        right_trigger = True
                        left_trigger = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        last_move = 'left'
                        right_trigger = False
                        left_trigger = True
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        s = pygame.mixer.Sound('Data/sounds/bow_jump.mp3')
                        s.set_volume(0.5)
                        s.play()
                        jump_trigger = True
                    elif event.key == pygame.K_e:
                        if player.potions > 0 and player.hp != player.fullhp:
                            player.potions -= 1
                            player.hp = min(player.fullhp, round(player.hp * 1.2))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        right_trigger = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        left_trigger = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and \
                            event.pos[0] > 10 and \
                            event.pos[0] < 60 and \
                            event.pos[1] > 10 and \
                            event.pos[1] < 64:
                        condition_trigger = 0
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Data/sounds/castle music.mp3')
                        pygame.mixer.music.play(loops=-1)
                        fcont = True
                        last_condition = 4
                        continue
                    elif event.button == 1 and not player.attackTrigger:
                        player.hit(event.pos)
                    elif event.button == 3 and not player.attackTrigger:
                        x1, y1 = event.pos
                        x2, y2 = player.rect.x + player.width // 2, player.rect.y + player.height // 2
                        player.hit(event.pos, coords=(x1, y1, x2, y2), group=all_boss_sprites)
            if player.hp <= 0 or mainTower.hp <= 0:
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.load('Data/sounds/menu music.mp3')
                pygame.mixer.music.play(loops=-1)
                condition_trigger = 3
            if left_trigger:
                player.vx = -1 * horizontall_speed * speedPerFrame
            elif right_trigger:
                player.vx = horizontall_speed * speedPerFrame
            else:
                player.vx = 0
            if jump_trigger:
                if player.isGrounded:
                    vertical_speed = -500
                    player.vy = vertical_speed * speedPerFrame
                jump_trigger = False
            else:
                if vertical_speed >= 300:
                    vertical_speed = 300
                else:
                    vertical_speed += 20
                player.vy = vertical_speed * speedPerFrame
            # end of the boss battle
            if not isAlive:
                for elem in enemies:
                    elem.hpBar.kill()
                    elem.kill()
                endClock += 1
            if not isAlive and endClock == 180:
                for elem in ground_layer:
                    elem.kill()
                for elem in bullets:
                    elem.kill()
                f = open("Data/coords save.txt", 'r')
                lines = f.readlines()
                l1 = lines[0].rstrip('\n').split()
                l2 = lines[1].rstrip('\n').split()
                f.close()
                player.rect.y, player.rect.x = int(l2[0]), int(l2[1])
                ground = Ground(int(l1[0]), int(l1[1]), width, [all_sprites, ground_layer], sprite=True)
                condition_trigger = 2
                collisionClock = 0
                curBoss += 1
            screen.fill((0, 0, 0))
            boss.draw_boss_name()
            all_boss_sprites.draw(screen)
            screen.blit(pause, (10, 10))
            font = pygame.font.Font(None, 40)
            text = font.render(str(player.arrows), True, (255, 255, 255))
            screen.blit(text, (70, 80))
            text = font.render(str(player.potions), True, (255, 255, 255))
            screen.blit(text, (70, 140))
            screen.blit(arrows, (10, 80))
            screen.blit(potions, (10, 140))
            all_boss_sprites.update()

        elif condition_trigger == 5:
            # boss menu
            menuBoss(screen, curBoss)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        condition_trigger = 2
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = event.pos
                    f2 = False
                    if curBoss >= 1 and 100 < pos[0] < 400 and 300 < pos[1] < 500:
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.load('Data/sounds/summoner music.mp3')
                        pygame.mixer.music.play(loops=-1)
                        name = 'Summoner'
                        boss = Summoner(width - 200, height // 8 * 4, player,
                                        [all_boss_sprites, boss_group], all_boss_sprites,
                                        tools, name, 300, pygame.image.load('Data/fon2.jpg'),
                                        attack=summoner_boss_attack, walk=summoner_boss_walk,
                                        idle=summoner_boss_idle, death=summoner_boss_death)
                        boss_ground = Ground(0, height // 8 * 7, width, [all_boss_sprites, ground_layer])
                        f2 = True
                    elif curBoss >= 2 and 450 < pos[0] < 750 and 300 < pos[1] < 500:
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Data/sounds/wizard music.mp3')
                        pygame.mixer.music.play(loops=-1)
                        name = 'Wizard'
                        boss = FireBoss(width - 200, height // 8 * 4, player,
                                        [all_boss_sprites, boss_group], all_boss_sprites,
                                        tools, name, 200, pygame.image.load('Data/fon4.png'),
                                        attack=fire_boss_attack, idle=fire_boss_idle, death=fire_boss_death)
                        boss_ground = Ground(0, height // 4 * 3 - 50, width, [all_boss_sprites, ground_layer])
                        f2 = True
                    elif curBoss >= 3 and 800 < pos[0] < 1100 and 300 < pos[1] < 500:
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.load('Data/sounds/ogre music.mp3')
                        pygame.mixer.music.play(loops=-1)
                        name = 'Ogre'
                        boss = Ogre(width - 200, height // 8 * 4, player,
                                    [all_boss_sprites, boss_group], all_boss_sprites,
                                    tools, name, 500, pygame.image.load('Data/fon3.png'),
                                    attack=ogre_boss_attack, walk=ogre_boss_walk,
                                    idle=ogre_boss_idle, death=ogre_boss_death)
                        boss_ground = Ground(0, height // 8 * 7, width, [all_boss_sprites, ground_layer])
                        f2 = True
                    if f2:
                        leftBD = VerticalBorder(0, 800, 400, player, [all_boss_sprites], sprite=False)
                        rightBD = VerticalBorder(1160, 800, 400, player, [all_boss_sprites], sprite=False)
                        condition_trigger = 4
                        f1 = False
                        collisionClock = 0
                        f = open("Data/coords save.txt", 'w')
                        print(str(ground.rect.x), str(ground.rect.y), file=f)
                        print(str(player.rect.x), str(player.rect.y), file=f)
                        f.close()
                        ground.rect.y = height // 8 * 7
                        isAlive = True
                        endClock = 0
                        player_pos = (player.rect.x, player.rect.y)
                        for elem in enemies:
                            elem.hpBar.kill()
                            elem.kill()
                        for elem in bullets:
                            elem.kill()
        collisionClock += 1
        time += speedPerFrame
        pygame.display.flip()
    pygame.quit()
