import pygame
from Entities import Entities

class Platform(Entities):
    def __init__(self, x_coord, y_coord):
        Entities.__init__(self)
        self.image = super().load_img('brickwall.png')[0]
        self.rect = super().load_img('brickwall.png')[1]
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rect.x = x_coord
        self.rect.y = y_coord

