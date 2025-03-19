import pygame

from Entities import Entities

class Player(Entities):
    def __init__(self, image, rect, x_coord, y_coord, hitpoints = 100, speed = 300):
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

    def gravity(self, delta_time):
        if self.y_speed < 20:
            self.y_speed += 40 * delta_time
            self.rect.y += self.y_speed
            self.y_coord = self.rect.y
            self.x_coord = self.rect.x



    def moveleft(self, delta_time):
        self.x_speed = -self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def moveright(self, delta_time):
        self.x_speed = self.speed * delta_time
        self.x_coord += self.x_speed
        self.rect.x += self.x_speed


    def jump_normal(self, delta_time):
        self.y_speed = -12


    def collision(self, platforms):
        for p in platforms:
            if pygame.Rect.colliderect(self.rect, p.rect):
                print('COllided')
                if p.rect.collidepoint(self.rect.midright):
                    self.rect.right = p.rect.left
                if p.rect.collidepoint(self.rect.midleft):
                    self.rect.left = p.rect.right
                if p.rect.collidepoint(self.rect.midbottom):
                    self.rect.bottom = p.rect.top
                    self.y_coord = p.rect.top
                    self.y_speed = 0

                if p.rect.collidepoint(self.rect.midtop):
                    self.rect.top = p.rect.bottom

