import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 200  # can modify later

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction_vector.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction_vector.y = 1
        else:
            self.direction_vector.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction_vector.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction_vector.x = -1
        else:
            self.direction_vector.x = 0

    def update(self, dt):
        self.input()
        self.move(dt)

    def move(self, dt):  # needs to modify later
        if self.direction_vector.magnitude() > 0:
            self.direction_vector = self.direction_vector.normalize()

        # horizontal
        self.pos_vector.x += self.direction_vector.x * self.speed * dt
        self.rect.centerx = self.pos_vector.x

        # vertical
        self.pos_vector.y += self.direction_vector.y * self.speed * dt
        self.rect.centery = self.pos_vector.y
