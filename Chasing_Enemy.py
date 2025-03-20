import pygame
from Entities import Entities
from Enemy import Enemy
from math import *
from usefull_functions import center_distance

class Chasing_Enemy(Enemy):
    def __init__(self, image, rect, hitpoints, damage, speed, x_coord, y_coord, action_speed):
        Enemy.__init__(self, image, rect, hitpoints, damage, speed, x_coord, y_coord, action_speed)


   

    def chase(self, player_rect, dt):
        distance = center_distance(player_rect, self.rect)
        if distance[2]<1000:
            if distance[1][0]>10:
                self.x_coord += distance[0][0] * self.speed * dt
                self.rect.x = self.x_coord
            if distance[1][0]<90 and distance[1][1]>10:
                self.rect.y = self.y_coord
                self.y_coord -= distance[0][1] * self.speed * dt

