import random

import pygame
import os
from Player import Player
from Platform import Platform

def load_img(filename):
    """Load image and return image object, rectangle of image."""
    filepath = os.path.join('asset', filename)
    try:
        image = pygame.image.load(filepath)
        width = image.get_width()
        height = image.get_height()
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image, image.get_rect(center=(width/2, height/2))
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
                p = Platform(platform_image, platform_rect)
                platforms.append(p)
                for group in sprite_groups:
                    p.add(group)
            x += resolution
        y += resolution
    return platforms


def generate_platform(platform_entities, sprite_entities, SCREEN_HEIGHT, SCREEN_WIDTH):
    while len(platform_entities) < 8:
        width = random.randrange(50,100)
        p = Platform(random.randint(10,SCREEN_WIDTH-10),
                     random.randint(0, SCREEN_HEIGHT-10))
        p.rect.center = (random.randrange(0, SCREEN_WIDTH - width),
                         random.randrange(-50, 0))
        p.add(sprite_entities)
        p.add(platform_entities)

def main():

    #pygame setup
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    #Create sprite group for all object, and sprite group for platform
    sprite_entities = pygame.sprite.Group()
    platform_entities = pygame.sprite.Group()

    #Load player image
    player_loaded_image = load_img('ninja_resized.png')
    player_image = player_loaded_image[0]
    player_rect = player_loaded_image[1]

    #Create player sprite object
    player = Player(player_image, player_rect, 480, 320, 100 )
    #Add player sprite object to sprite group for all object
    player.add(sprite_entities)

    #Create Platform object ground
    #ground Platform is created seperated due to different color,
    #non-randomized position, and moving parameter set to False
    ground = Platform(0,0)
    #Create surface for ground object that is half as wide as screen size and 16 pixel high
    ground.image = pygame.Surface((SCREEN_WIDTH / 2, 16))
    ground.image.fill('red')
    ground.rect = ground.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 8))
    #Disable ability for the ground to move
    ground.moving = False
    #Add ground to all sprites group, and platform sprites group
    ground.add(sprite_entities)
    ground.add(platform_entities)

    #Create initial platforms, disallow moving for initial platforms
    #4 or 5 platforms may be created to randomize start
    for i in range(random.randint(4,5)):
        p = Platform(random.randint(10,SCREEN_WIDTH-10),
                     random.randint(0, SCREEN_HEIGHT-10))
        p.moving = False
        p.add(sprite_entities)
        p.add(platform_entities)

    #MAIN GAME LOOP
    while running:
        for event in pygame.event.get():
            #Check quit event
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit
            #Check for jumping event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.jump()

        #LOGICAL UPDATE
        #Iterate through all Platform entities, call move method to move platforms
        for p in platform_entities:
            p.move(SCREEN_WIDTH)

        #Move player when input is detected
        player.move()
        #Perform collision check between player and platforms
        player.update(player, platform_entities)

        #Generate platforms above the player, outside screen area
        generate_platform(platform_entities, sprite_entities, SCREEN_HEIGHT, SCREEN_WIDTH)

        #Scroll screen when player reached specific part of screen
        if player.rect.top <= SCREEN_HEIGHT / 3:
            player.pos.y += abs(player.velocity.y)
            #Check if platform are below screen, delete if so
            for p in platform_entities:
                p.rect.top += abs(player.velocity.y)
                if p.rect.top >= SCREEN_HEIGHT:
                    p.kill()
        #Check if player fell below screen
        elif player.rect.bottom >= SCREEN_HEIGHT:
            print("You DIED")
            raise SystemExit

        #Allow player to go from one side of the screen to the other
        if player.pos.x > SCREEN_WIDTH:
            player.pos.x = 0
            player.pos.y -= 10
        if player.pos.x < 0:
            player.pos.x = SCREEN_WIDTH
            player.pos.y -= 10
        screen.fill('black')

        #Render graphic here
        #Draw all sprites in general sprite group
        sprite_entities.draw(screen)
        #Flip display
        pygame.display.flip()
        #Limit FPS: 60
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()