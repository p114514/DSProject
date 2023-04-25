import pygame
from settings import *
from support import *


class Magic(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.speed = 100
        self.ATK=100
        self.frame_index = 0
        self.pics = {'right': r'./weapon/0.png', 'left': r'./weapon/1.png', 'up': r'./weapon/2.png',
                     'down': r'./weapon/3.png'}
        self.dir={'right':[1,0],'left':[-1,0],'up':[0,-1],'down':[0,1]}
        self.step=50


    def setMagic(self, status, pos,enemy,oracle):
        self.status = status
        self.image = pygame.image.load(self.pics[self.status])
        self.rect = self.image.get_rect(topleft=pos)
        self.enemy_sprites=enemy
        self.oracle_sprites=oracle
        self.dirV = [self.dir[self.status][0], self.dir[self.status][1]]

    def update(self, dt):
        self.move(dt)

    def move(self,dt):
        if self.step>0:
         self.rect.x+=self.dirV[0]*self.speed*dt
         self.rect.y+=self.dirV[1]*self.speed*dt
         self.step-=1
        else:
         self.kill()
        for sp in self.enemy_sprites:
            if sp.rect.colliderect(self.rect):
               sp.take_damage(self.ATK - sp.DEF, self)
               self.kill()
        for sp in self.oracle_sprites:
            if self.rect.colliderect(sp.rect):
                self.kill()




