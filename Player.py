import pygame
from usefull_functions import center_distance
from Entities import Entities

class Player(Entities):
    def __init__(self, image, rect, x_coord, y_coord, hitpoints = 6, speed = 300):
        Entities.__init__(self)
        self.image = image
        self.rect = rect
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.hitpoints = hitpoints
        self.speed = speed
        self.x_speed = 0
        self.y_speed = 0
        self.hit_recently = False
        self.time_since_last_hit=0

    def gravity(self, delta_time):
        if self.y_speed < 17:
            self.y_speed += 40 * delta_time
            self.rect.y += self.y_speed
            self.y_coord = self.rect.y
            self.x_coord = self.rect.x
    '''def air_resistance(self, delta_time):
        

        self.x_speed -= x * delta_time'''



    def moveleft(self, delta_time):
        self.x_speed = -self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def moveright(self, delta_time):
        self.x_speed = self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def jump_normal(self):
        self.y_speed = -12

    def collision(self, platforms, enemy_hitboxes, delta_time):
        for p in platforms:
            if pygame.Rect.colliderect(self.rect, p.rect):
                print('COllided')
                if p.rect.collidepoint(self.rect.midright):
                    self.rect.right = p.rect.left
                if p.rect.collidepoint(self.rect.midleft):
                    self.rect.left = p.rect.right
                if p.rect.collidepoint(self.rect.midbottom):
                    self.rect.bottom = p.rect.top
                    self.y_speed = 0
                if p.rect.collidepoint(self.rect.midtop):
                    self.rect.top = p.rect.bottom
                    self.y_speed = 0
        if self.hit_recently:
                self.time_since_last_hit += 1
                if self.time_since_last_hit == 30:
                    self.hit_recently = False
        else:
            for hitbox in enemy_hitboxes:
                if pygame.Rect.colliderect(self.rect, hitbox.rect):
                    self.hitpoints -= hitbox.damage
                    self.hit_recently=True
                    self.time_since_last_hit = 0








