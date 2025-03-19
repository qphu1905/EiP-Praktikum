import pygame
from Entities import Entities
from Enemy import Enemy
from math import *

class Chasing_Enemy(Enemy):
    def __init__(self, image, rect, hitpoints, damage, speed, x_coord, y_coord, action_speed):
        Enemy.__init__(self, image, rect, hitpoints, damage, speed, x_coord, y_coord, action_speed)


   

    def chase(self, player_x, player_y, dt):
        def distance_to_player(player_x, player_y) -> list[tuple[int, int] | int]:
            x_distance = int(player_x - self.x_coord)
            if x_distance > 0:
                x_sign = 1
            else:
                x_sign = -1
            y_distance = int(player_y - self.y_coord)
            if y_distance > 0:                                            # if a is ABOVE b, y_sign is 1,if a is BELOW b, y_sign is -1!!
                y_sign = -1
            else:
                y_sign = 1
            distance_total = int(ceil(sqrt(x_distance ** 2 + y_distance ** 2)))
            return [(x_sign, y_sign), (x_distance, y_distance), distance_total]
        distance = distance_to_player(player_x, player_y)
        if distance[2]<1000:
            if not 5>distance[1][0]>-5:
                self.x_coord += distance[0][0] * self.speed * dt
                self.rect.x = self.x_coord
            if not 5>distance[1][1]>-5:
                self.rect.y = self.y_coord
                self.y_coord -= distance[0][1] * self.speed * dt

