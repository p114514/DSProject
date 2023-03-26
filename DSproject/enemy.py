import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 200  # can modify later
        self.direction_vector.x = random.choice((-1, 1))
        self.direction_vector.y = random.choice((-1, 1))



    def update(self, dt):

        self.randomMove(dt)

    def randomMove(self, dt):  # needs to modify later




        if self.rect.centerx >= SCREEN_WIDTH or self.rect.centerx <= 0:
            self.direction_vector.x *=-1
            self.direction_vector.y *= random.choice((-1, 1))
        if self.rect.centery >= SCREEN_HEIGHT or self.rect.centery <= 0:
            self.direction_vector.y *= -1
            self.direction_vector.x *= random.choice((-1, 1))
        if self.direction_vector.magnitude() > 0:
            self.direction_vector = self.direction_vector.normalize()


        # horizontal
        self.pos_vector.x += self.direction_vector.x * self.speed * dt
        self.rect.centerx = self.pos_vector.x

        # vertical
        self.pos_vector.y += self.direction_vector.y * self.speed * dt
        self.rect.centery = self.pos_vector.y