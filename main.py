import pygame
import os
from Player import Player
from Platform import Platform
from math import *
from Ghost import Ghost

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
    ghost_loaded_image = load_img('Ghost_black.jpg')
    ghost_image = ghost_loaded_image[0]
    ghost_rect = ghost_loaded_image[1]
    ghost_1 = Ghost(ghost_image, ghost_rect, 700, 320)
    ghost_1.add(sprite_entities)
    chasing_enemys = [ghost_1]
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
        if keys[pygame.K_SPACE] and player.y_speed==0:
            player.jump_normal(dt)
        if keys[pygame.K_a]:
            player.moveleft(dt)
        if keys[pygame.K_d]:
            player.moveright(dt)

        player.gravity(dt)
        player.collision(platforms)
        for Enemy in chasing_enemys:
                Enemy.chase(player.x_coord, player.y_coord, dt)
        screen.fill('black')
        #Render graphic here
        sprite_entities.draw(screen)
        pygame.display.flip()   #Flip display
        clock.tick(60)          #Limit FPS: 60
        print(player.x_coord, player.y_coord)
    pygame.quit()


if __name__ == '__main__':
    main()