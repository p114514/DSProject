import random

import pygame
from settings import *
from player import Player
from enemy import Enemy
from mapeditor import myMap


class Level:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.map = myMap(self.display_surface, self.all_sprites)
        # setup

        self.map.drawWall()
        self.setup()

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.map.drawWall()
        # map‘s level is above the sprite
        self.all_sprites.update(dt)

    def setup(self):
        movepath = self.map.getMoveArea().copy()
        birthPos = self.map.getMovePos().copy()
        # Player_birth=random.choice(birthPos)
        # birthPos.remove(Player_birth)
        # print(Player_birth)
        Enemy_birth = []
        n = 10
        for i in range(0, n):
            Enemy_birth.append(random.choice(birthPos))
            if birthPos.count(Enemy_birth) > 0:
                birthPos.remove(Enemy_birth)
        print(Enemy_birth)

        self.player = Player((0, 0), movepath, self.all_sprites,self.map.getBlock())
        for i in range(0, n):
            locals()['self.enemy' + str(i)] = Enemy(Enemy_birth[i], movepath, self.all_sprites,self.map.getBlock())
