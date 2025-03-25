import pygame
import random

from pygame.pypm import FALSE

from Entities import Entities

class Platform(Entities):
    def __init__(self, x, y):
        Entities.__init__(self)
        self.image = pygame.Surface((random.randint(50,100), 12))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = random.randint(-1, 1) * random.randint(1,3)
        self.moving = True

    def move(self, SCREEN_WIDTH):
        if self.moving:
            self.rect.move_ip(self.speed, 0)
            if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH