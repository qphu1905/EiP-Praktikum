import pygame
from Entities import Entities

class Platform(Entities):
    def __init__(self, image, rect, x_coord, y_coord):
        Entities.__init__(self)
        self.image = image
        self.rect = rect
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rect.x = x_coord
        self.rect.y = y_coord