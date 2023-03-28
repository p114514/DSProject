import pygame
from player import Player
from settings import *
import random
import  math
class Enemy(Player):
    def __init__(self, pos,movepath,group):

        super(Enemy,self).__init__(pos,movepath,group)
        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)
        self.movepath=movepath
        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 400  # can modify later
        self.step=500

    def update(self, dt):

        self.randMove(dt)

    def randMove(self, dt):  # needs to modify later
        l = pygame.math.Vector2(-1, 0)
        r = pygame.math.Vector2(1, 0)
        u = pygame.math.Vector2(0, 1)
        d = pygame.math.Vector2(0, -1)
        self.left=self.pos_vector+pygame.math.Vector2(-1, 0)* self.speed * dt
        self.right = self.pos_vector + pygame.math.Vector2(1, 0)* self.speed * dt
        self.up = self.pos_vector + pygame.math.Vector2(0, 1)* self.speed * dt
        self.down = self.pos_vector + pygame.math.Vector2(0, -1)* self.speed * dt
        if self.right.x>SCREEN_WIDTH:
            self.direction_vector = random.choice((l, u, d))
        if self.left.x<0 :
            self.direction_vector=random.choice((r,u,d))
        if self.up.y>SCREEN_HEIGHT:
            self.direction_vector = random.choice((l, r, d))
        if self.down.y<0 :
            self.direction_vector=random.choice((l,r,u))
        if self.step<=0:
            self.direction_vector=random.choice((l,r,u,d))
            self.step=500
        else:
            self.move(dt)
            self.step-=1
