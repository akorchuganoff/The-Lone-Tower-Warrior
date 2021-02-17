#mainloop
import pygame

def draw(screen, width, height, player_position):
    #ground
    pygame.draw.rect(screen, pygame.Color('Gray'), ((0, height // 4 * 3), (width, height//4)), width=0)
    #tower
    pygame.draw.rect(screen, pygame.Color((100, 100, 100)), ((width//9*4, height//8*3), (width//9, height // 8 * 3)), width=0)
    #player
    pygame.draw.rect(screen, pygame.Color((255, 0, 0)),
                     ((player_position[0], player_position[1]), (20, 50)), width=0)

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    running = True

    player_position = [width//2, height//2]
    speed = 100

    # movement triggers
    right_trigger = False
    left_trigger = False

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
            player_position[0] -= speed * clock.tick(30) / 1000
        elif right_trigger:
            player_position[0] += speed * clock.tick(30) / 1000
        # horizontal move end

        clock.tick(30)
        screen.fill((0, 0, 0))
        draw(screen, width, height, player_position)
        pygame.display.flip()
    pygame.quit()