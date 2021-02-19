import pygame


class shopScreen(pygame.sprite.Sprite):
    def __init__(self, width, height, group, money):
        super().__init__(*group)
        self.image = pygame.Surface([width // 4 * 3, height // 4 * 3])
        self.image.fill((255, 255, 255))
        # self.image.set_alpha(10)
        # self.image.set_alpha(255)
        self.rect = pygame.Rect(width // 8, height // 8, width // 4 * 3, height // 4 * 3)
        self.price = 1
        self.width = width // 4 * 3
        self.height = height // 4 * 3

        self.font = pygame.font.Font(None, 50)
        self.money = money
        print(self.money)



    def buy(self, mainTower):
        self.money.amount -= self.price
        self.price *= 2
        mainTower.damage += 1
        print(mainTower.damage)

    def update(self):

        self.font = pygame.font.Font(None, 100)
        shop_text = self.font.render("Shop", True, (0, 0, 0))
        shop_text_x = self.width // 2 - shop_text.get_width()//2
        shop_text_y = self.height // 4 - shop_text.get_height()//2
        self.image.fill((255, 255, 255))
        self.image.blit(shop_text, (shop_text_x, shop_text_y))

        self.font = pygame.font.Font(None, 50)
        upgrade_text = self.font.render(f"Upgrade: {self.price}", True, (0, 0, 0))
        upgrade_text_x = self.width // 2 - upgrade_text.get_width() // 2
        upgrade_text_y = self.height // 4 * 2 - upgrade_text.get_height() // 2
        self.image.blit(upgrade_text, (upgrade_text_x, upgrade_text_y))

        pygame.draw.rect(self.image, pygame.Color((0, 0, 0)), ((upgrade_text_x-10, upgrade_text_y-10), (upgrade_text.get_width()+20, upgrade_text.get_height()+20)), width=5)

        self.font = pygame.font.Font(None, 50)
        balance_text = self.font.render(f"Your balance: {self.money.amount}", True, (0, 0, 0))
        balance_text_x = self.width // 2 - balance_text.get_width() // 2
        balance_text_y = self.height // 4*3 - balance_text.get_height() // 2
        self.image.blit(balance_text, (balance_text_x, balance_text_y))

        return upgrade_text_x-10, upgrade_text_y-10, upgrade_text_x-10+upgrade_text.get_width()+20, upgrade_text_y-10+upgrade_text.get_height()+20



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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True

    money_group = pygame.sprite.Group()
    shop_group = pygame.sprite.Group()



    money = Money([money_group])
    shop = shopScreen(1, width, height, [shop_group], money)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 0))
        shop_group.draw(screen)
        shop_group.update()


        clock.tick(30)
        pygame.display.flip()
    pygame.quit()