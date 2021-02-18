#mainloop
import pygame
from Player_class import Player

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
        def __init__(self, x, y, width, height, group):
            super().__init__(*group)
            self.image = pygame.Surface([width, height])
            self.image.fill((255, 0, 0))
            self.rect = pygame.Rect(x, y, width, height)
            self.vx = 0
            self.vy = 0
            self.hp = 0

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


    player = Player(player_position[0], player_position[1], 20, 50, [all_sprites, player])
    ground = Ground(width, height, [all_sprites, ground_layer])
    enemy_1 = Enemy(50, 50, 30, 30, [all_sprites, enemies])
    MainHPbar = HPbar(player, width, height, [all_sprites, tools])

    # movement triggers
    right_trigger = False
    left_trigger = False
    jump_trigger = False
    condition_trigger = 1

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

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("You lose!!!", True, (100, 100, 100))
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, pygame.Color((255, 255, 255)), [width//4, height//4, width//2, height//2], width=5)

            restart_text = font.render("Restart", True, (100, 100, 100))
            restart_text_x = width // 8*3 - restart_text.get_width() // 2
            restart_text_y = height // 8*5 - restart_text.get_height() // 2
            restart_text_w = restart_text.get_width()
            restart_text_h = restart_text.get_height()
            screen.blit(restart_text, (restart_text_x, restart_text_y))

            quit_text = font.render("Quit", True, (100, 100, 100))
            quit_text_x = width // 8 * 5 - quit_text.get_width() // 2
            quit_text_y = height // 8 * 5 - quit_text.get_height() // 2
            quit_text_w = quit_text.get_width()
            quit_text_h = quit_text.get_height()
            screen.blit(quit_text, (quit_text_x, quit_text_y))
            # button_text_w = max(quit_text_w // 2, restart_text_w//2)
            button_text_w = 60
            pygame.draw.rect(screen, pygame.Color((255, 255, 255)), [restart_text_x - button_text_w, restart_text_y - restart_text_h//2, button_text_w*4, restart_text_h*2],
                             width=5)
            pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                             [quit_text_x - button_text_w*1.4, quit_text_y - quit_text_h // 2,
                              button_text_w*4, quit_text_h * 2],
                             width=5)
            print(button_text_w)



        pygame.display.flip()
    pygame.quit()