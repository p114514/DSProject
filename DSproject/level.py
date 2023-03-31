import random

import pygame
from settings import *
from player import Player
from enemy import Enemy
from mapeditor import myMap
n = 10   #number of enemies

class Level:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.enempy_sprites = pygame.sprite.Group()
        self.play_sprites = pygame.sprite.Group()
        self.all_sprites=pygame.sprite.Group()
        self.map = myMap(self.display_surface, self.all_sprites)
        # setup
        self.RoomNO = 0
        self.map.drawWall()
        self.setup()

    def run(self, dt):
        if self.RoomNO==0:
           self.display_surface.fill('black')
           self.play_sprites.draw(self.display_surface)
           self.enempy_sprites.draw(self.display_surface)
           self.map.drawWall()
           #self.map.drawWall(RoomNO)====>drawdiffe room
        elif self.RoomNO>0:
            self.display_surface.fill('white')
            self.play_sprites.draw(self.display_surface)
            self.map.drawWall()
            # self.map.drawWall(RoomNO)====>drawdiffe room
        playerpos=self.player.getpos()
        if playerpos.x<0 or playerpos.x>SCREEN_WIDTH or playerpos.y<0 or playerpos.y>SCREEN_HEIGHT:
            self.shiftRoom(playerpos)
            self.RoomNO+=1


        # map‘s level is above the sprite
        self.all_sprites.update(dt)
        self.play_sprites.update(dt)
        self.enempy_sprites.update(dt)
        #enemy gets player's position
        for i in range(0, n):
         globals()['self.enemy' + str(i)].setPlayerPos(playerpos)
    def shiftRoom(self,playerpos):

        if playerpos.x<0:
            print(playerpos)
            self.player.setPos((SCREEN_WIDTH+playerpos.x,playerpos.y))
        elif playerpos.x>SCREEN_WIDTH:
            print(playerpos)
            self.player.setPos((playerpos.x-SCREEN_WIDTH, playerpos.y))
        elif playerpos.y<0:
            print(playerpos)
            self.player.setPos((playerpos.x ,SCREEN_HEIGHT+ playerpos.y))
        elif playerpos.y>SCREEN_HEIGHT:
            print(playerpos)
            self.player.setPos((playerpos.x,playerpos.y-SCREEN_HEIGHT))

    def setup(self):
        movepath = self.map.getMoveArea().copy()
        birthPos = self.map.getMovePos().copy()
        # Player_birth=random.choice(birthPos)
        # birthPos.remove(Player_birth)
        # print(Player_birth)
        Enemy_birth = []

        for i in range(0, n):
            Enemy_birth.append(random.choice(birthPos))
            if birthPos.count(Enemy_birth) > 0:
                birthPos.remove(Enemy_birth)
        print(Enemy_birth)

        self.player = Player((0, 0), movepath, self.play_sprites,self.map.getBlock())

        for i in range(0, n):
            globals()['self.enemy' + str(i)] = Enemy((0,0), self.player.getpos(),movepath, self.enempy_sprites,self.map.getBlock())
