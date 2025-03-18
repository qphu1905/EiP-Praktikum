import pygame
from Entities import Entities

class Player(Entities):
    gravity = 10
    def __init__(self, image, rect, hitpoints, y_speed, x_coord, y_coord):
        Entities.__init__(self)
        self.image = image
        self.rect = rect
        self.hitpoint = hitpoints
        self.x_speed = 10
        self.y_speed = y_speed
        self.x_coord = x_coord
        self.y_coord = y_coord


    def moveleft(self, delta_time):
        self.x_coord -= self.x_speed * delta_time
        self.rect.Rect.move(-self.x_speed * delta_time, 0)


    def moveright(self, delta_time):
        self.x_coord += self.x_speed * delta_time
        self.rect.Rect.move(self.x_speed * delta_time, 0)


    def jump(self, delta_time):
        self.y_coord -= self.y_speed * delta_time
        self.rect.Rect.move(0, -self.y_speed * delta_time)
        self.y_speed += self.gravity * delta_time


    def collision(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.x_speed > 0:
                    self.rect.right = p.rect.left
                if self.x_speed < 0:
                    self.rect.left = p.rect.right
                if self.y_speed > 0:
                    self.rect.bottom = p.rect.top
                if self.y_speed < 0:
                    self.rect.top = p.rect.bottom
