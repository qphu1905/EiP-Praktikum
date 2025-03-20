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


def load_map(level, resolution: int, sprite_groups: list):
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
                for group in sprite_groups:
                    p.add(group)
            x += resolution
        y += resolution
    return platforms

def main():
    #Game Parameter
    ACC = 1
    FRIC = -0.12

    #pygame setup
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    sprite_entities = pygame.sprite.Group()
    platform_entities = pygame.sprite.Group()
    player_loaded_image = load_img('ninja_resized.png')
    player_image = player_loaded_image[0]
    player_rect = player_loaded_image[1]
    player = Player(player_image, player_rect, 480, 320, 100 )
    player.add(sprite_entities)

    level = ['     ppp                      ',
             '                              ',
             '                     ppp      ',
             '              ppp             ',
             '                              ',
             '             ppp              ',
             '                              ',
             '     ppp                      ',
             '                              ',
             '                  ppp         ',
             '       ppp                    ',
             '                              ',
             '    ppp           ppp         ',
             '                              ',
             '        ppp              ppp  ',
             '                              ',
             '                ppp           ',
             '     ppp                      ',
             '                              ',
             'pppppppppppppppppppppppppppppp']

    platforms = load_map(level, 32, [sprite_entities, platform_entities])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.jump()

        #Logical update here
        dt = clock.tick(60) / 1000

        player.move(ACC, FRIC)
        player.update(player, platform_entities)

        if player.rect.top <= SCREEN_HEIGHT / 3:
            player.pos.y += abs(player.velocity.y)
            for p in platform_entities:
                p.rect.y += abs(player.velocity.y)
        elif player.rect.bottom >= SCREEN_HEIGHT / 4:
            player.pos.y -= abs(player.velocity.y)
            for p in platform_entities:
                p.rect.y -= abs(player.velocity.y)
        screen.fill('black')

        #Render graphic here
        sprite_entities.draw(screen)
        pygame.display.flip()   #Flip display
        clock.tick(60)          #Limit FPS: 60

    pygame.quit()


if __name__ == '__main__':
    main()