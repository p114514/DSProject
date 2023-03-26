import pygame
from player import Player
from settings import *
import random

class Enemy(Player):
    def __init__(self, pos,group):
        super(Enemy,self).__init__(pos,group)
        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 100  # can modify later


        self.step=random.randint(500,1000)

    def update(self, dt):

        self.randMove(dt)



    def randMove(self, dt):  # needs to modify later
        if self.step<=0:
            l=pygame.math.Vector2(-1, 0)
            r = pygame.math.Vector2(1, 0)
            u = pygame.math.Vector2(0, 1)
            d = pygame.math.Vector2(0, -1)
            self.direction_vector=random.choice((l,r,u,d))
            self.step=random.randint(500,1000)
        else:
            self.move(dt)
            self.step-=1

