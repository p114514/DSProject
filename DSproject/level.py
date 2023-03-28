import random

import pygame
from settings import *
from player import Player
from enemy import  Enemy
from mapeditor import myMap
class Level:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.map = myMap(self.display_surface)
        # setup

        self.map.drawWall()
        self.setup()

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.map.drawWall()
        #map‘s level is above the sprite
        self.all_sprites.update(dt)

    def setup(self):

        movepath = self.map.getMoveArea().copy()
        birthPos  =self.map.getMovePos().copy()
        print(self.map.getMoveArea()[319][179])
        Player_birth=random.choice(birthPos)
        birthPos.remove(Player_birth)
        print(Player_birth)
        Enemy_birth=random.choice(birthPos)
        birthPos.remove(Enemy_birth)
        print(Enemy_birth)
        self.player = Player((0,0),movepath, self.all_sprites)
       # self.enemy = Enemy(Enemy_birth, movepath,self.all_sprites)



