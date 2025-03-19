import pygame
from Entities import Entities

class Enemy(Entities):
    def __init__(self, image, rect, hitpoints, damage, speed, x_coord, y_coord, action_speed):
        Entities.__init__(self)
        self.hitpoints = hitpoints
        self.damage = damage
        self.image = image
        self.rect = rect
        self.speed = speed
        self.y_speed = 0
        self.x_speed = 0
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.action_speed = action_speed




    def collision(self, platforms):
        for p in platforms:
            if pygame.Rect.colliderect(self.rect, p.rect):
                if self.x_speed > 0:
                    self.rect.right = p.rect.left
                if self.x_speed < 0:
                    self.rect.left = p.rect.right