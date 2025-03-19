import pygame
import os

from Player import Player
from Platform import Platform
from math import *
from Ghost import Ghost




#def load_sound() if sound is added


def load_map(level, resolution: int, sprite_entities):
    platforms = []
    y = 0
    for row in level:
        x = 0
        for column in row:
            if column == 'p':
                p = Platform(x, y)
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
    Ghost_1 = Ghost(480, 320)
    player = Player(480, 320, 100 )
    player.add(sprite_entities)
    Ghost_1.add(sprite_entities)
    print(sprite_entities)
    Chasing_Enemys = []
    Chasing_Enemys.append(Ghost_1)
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
        for Enemy in Chasing_Enemys:
                Enemy.chase(player.x_coord, player.y_coord, dt)
        screen.fill('black')
        #Render graphic here

        sprite_entities.draw(screen)
        pygame.display.flip()   #Flip display
        clock.tick(60)          #Limit FPS: 60


    pygame.quit()


if __name__ == '__main__':
    main()