import pygame
import os
from Player import Player
from Platform import Platform

def load_img(filename):
    """Load image and return image object, rectangle of image."""
    filepath = os.path.join('asset', filename)
    try:
        image = pygame.image.load(filepath)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image, image.get_rect()
    except FileNotFoundError:
        print(f'File {filepath} found')


#def load_sound() if sound is added


def load_map(level, resolution: int, sprite_entities):
    platforms = []
    y = 0
    for row in level:
        x = 0
        for column in row:
            if column == 'p':
                platform_loaded_image = load_img('brickwall.png')
                platform_image = platform_loaded_image[0]
                platform_rect = platform_loaded_image[1]
                p = Platform(platform_image, platform_rect, x, y)
                platforms.append(p)
                p.add(sprite_entities)
            x += resolution
        y += resolution
    return platforms

def main():
    #pygame setup
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 640

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    sprite_entities = pygame.sprite.Group()
    player_loaded_image = load_img('ninja_resized.png')
    player_image = player_loaded_image[0]
    player_rect = player_loaded_image[1]
    player = Player(player_image, player_rect, 480, 320, 100 )
    player.add(sprite_entities)

    level = ['p             p',
             'p             p',
             'p             p',
             'p             p',
             'p             p',
             'p             p',
             'p             p',
             'p             p',
             'p             p',
             'ppppppppppppppp',]
    platforms = load_map(level, 64, sprite_entities)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit

        #Logical update here
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.jump(dt)
        if keys[pygame.K_a]:
            player.moveleft(dt)
        if keys[pygame.K_d]:
            player.moveright(dt)

        player.collision(platforms)

        screen.fill('black')

        #Render graphic here
        sprite_entities.draw(screen)
        pygame.display.flip()   #Flip display
        clock.tick(60)          #Limit FPS: 60

    pygame.quit()


if __name__ == '__main__':
    main()