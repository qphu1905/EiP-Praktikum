import pygame
from Entities import Entities

class Player(Entities):
    def __init__(self, image, rect, x_coord, y_coord, hitpoints = 100, speed = 100):
        Entities.__init__(self)
        self.image = image
        self.rect = rect

        self.pos = pygame.Vector2(x_coord, y_coord)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
        self.acc = 1
        self.fric = -0.12
        self.onground = False

    def move(self):
        self.acceleration = pygame.Vector2(0,0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.acceleration.x = -self.acc
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.acceleration.x = self.acc
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.acceleration.y += 1

        self.acceleration.x += self.velocity.x * self.fric
        self.velocity += self.acceleration
        self.pos += self.velocity + 0.5 * self.acceleration
        self.rect.center = self.pos


    def jump(self):
        if self.onground:
            self.velocity.y = -15
            self.onground = False


    def update(self, player, platform_entities):
        hits = pygame.sprite.spritecollide(player, platform_entities, False)
        if hits:
            self.pos.y = hits[0].rect.top - (self.rect.h / 2)
            self.velocity.y = 0
            self.onground = True