import pygame
import os


def load_img(filename):
    '''Load image and return image object, rectangle of image.'''
    filepath = os.path.join('asset', filename)
    try:
        image = pygame.image.load(filepath)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f'File {filepath} found')
    return image, image.get_rect()


#def load_sound() if sound is added


def main():
    #pygame setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        if pygame.event.get(pygame.QUIT):
            running = False
            raise SystemExit

        #Logical update here

        screen.fill('black')

        #Render graphic here

        pygame.display.flip()   #Flip display
        clock.tick(60)          #Limit FPS: 60
    pygame.quit()


if __name__ == '__main__':
    main()