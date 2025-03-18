import pygame
from Entities import Entities

class Player(Entities):
    def __init__(self, image, rect, x_coord, y_coord, hitpoints = 100, speed = 100):
        Entities.__init__(self)
        self.image = image
        self.rect = rect
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.hitpoint = hitpoints
        self.speed = speed
        self.x_speed = 0
        self.y_speed = 0

    def moveleft(self, delta_time):
        self.x_speed = -self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def moveright(self, delta_time):
        self.x_speed = self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def jump(self, delta_time):
        self.y_coord -= self.y_speed * delta_time
        self.rect.y -= self.y_speed * delta_time


    def collision(self, platforms):
        for p in platforms:
            if pygame.Rect.colliderect(self.rect, p.rect):
                print('COllided')
                if self.x_speed > 0:
                    self.rect.right = p.rect.left
                if self.x_speed < 0:
                    self.rect.left = p.rect.right

