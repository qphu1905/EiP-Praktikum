import pygame
import os
class Entities(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def load_img(self, filename):
        """Load image and return image object, rectangle of image."""
        filepath = os.path.join('asset', filename)
        try:
            image = pygame.image.load(filepath)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
                pygame.Surface.set_colorkey(image, "pink")
            return image, image.get_rect()
        except FileNotFoundError:
            print(f'File {filepath} found')