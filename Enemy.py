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
        self.rect.x = x_coord
        self.rect.y = y_coord
        pygame.Surface.set_colorkey(image, (0,0,0,))
        self.action_speed = action_speed



    def collision(self, player_hitboxes):
        for hitbox in player_hitboxes:
            if pygame.Rect.colliderect(self.rect, hitbox.rect):
                self.hitpoints -= hitbox.damage






