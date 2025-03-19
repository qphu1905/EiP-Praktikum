import pygame
from Entities import Entities
from Enemy import Enemy
from math import *
from Chasing_Enemy import Chasing_Enemy

class Ghost(Chasing_Enemy):
    def __init__(self, image, rect, x_coord, y_coord):
        Chasing_Enemy.__init__(self, image, rect, 2, 1, 70, x_coord, y_coord, 0)



