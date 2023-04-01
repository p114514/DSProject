import random

import pygame
from settings import *
from player import Player
from enemy import Enemy
from mapeditor import myMap
n = 5  #number of enemies

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
        self.curRoom=[0,0]
        self.RR=self.map.getRoomRC()[0]
        self.RC = self.map.getRoomRC()[1]
        self.map.drawRoom(self.curRoom[0],self.curRoom[1])
        self.isShift=0
        self.setup()
        #print(self.map.getMoveArea())
    def run(self, dt):
        if self.player.rect.x <= 0 or self.player.rect.x >= SCREEN_WIDTH or self.player.rect.y <= 0 or self.player.rect.y >= SCREEN_HEIGHT:
            self.shiftRoom()
        self.display_surface.fill('black')

        self.map.drawRoom(self.curRoom[0], self.curRoom[1])



        playerpos = self.player.getpos()
        self.play_sprites.draw(self.display_surface)
        self.enempy_sprites.draw(self.display_surface)
        ###generate new enemies
        if self.isShift==1:

            self.enempy_sprites.remove(self.enempy_sprites)
            self.map.initMoveArea()
            self.map.drawRoom(self.curRoom[0], self.curRoom[1])
            Enemy_birth=[]
            abirthPos=[]
            movepath = self.map.MoveArea
            for i in range(0, SCREEN_HEIGHT):
                for j in range(0, SCREEN_WIDTH):
                    if movepath[i][j] == 1:
                        abirthPos .append((i, j))
            print(abirthPos[0])
            #print(len(birthPos))
            for i in range(0, n):
                a=abirthPos[random.randint(0, len(abirthPos))]
                if movepath[a[0]][a[1]]==1:
                   Enemy_birth.append(a)
                   print(movepath[Enemy_birth[0][0]][Enemy_birth[0][1]])


            for i in range(0, n):
                globals()['self.enemy' + str(i)] = Enemy(Enemy_birth[i], self.player.getpos(), movepath,
                                                         self.enempy_sprites, self.map.getBlock())
            self.isShift=0

        # map‘s level is above the sprite
        self.all_sprites.update(dt)
        self.play_sprites.update(dt)
        self.enempy_sprites.update(dt)
        #enemy gets player's position
        for i in range(0, n):
         globals()['self.enemy' + str(i)].setPlayerPos(playerpos)
    def shiftRoom(self):
        ##情况比较多 用树考虑比较好？
        #print(self.player.rect)
        if self.player.rect.x<0:

            if self.curRoom[0] > 0:

               self.curRoom[0]-=1

               self.player.rect.x = SCREEN_WIDTH - 1
               self.isShift=1
            else:
               self.player.rect.x=0
        elif self.player.rect.x>SCREEN_WIDTH:

            if self.curRoom[0] < self.RR-1:

               self.curRoom[0]+=1

               self.player.rect.x = 0
               self.isShift = 1
            else:
               self.player.rect.x=SCREEN_WIDTH
        elif self.player.rect.y<0:

            if self.curRoom[1] > 0:
               self.curRoom[1] -= 1

               self.player.rect.y = SCREEN_HEIGHT - 1
               self.isShift = 1
            else:
               self.player.rect.y=0
        elif self.player.rect.y>SCREEN_HEIGHT:

            if self.curRoom[1] < self.RC-1:
               self.curRoom[1]+=1

               self.player.rect.y = 0
               self.isShift = 1
            else:
               self.player.rect.y=SCREEN_HEIGHT


    def setup(self):
        movepath = self.map.getMoveArea()

        birthPos = []

        for i in range(0, SCREEN_HEIGHT):
            for j in range(0, SCREEN_WIDTH):
                if movepath[i][j] == 1:
                    birthPos.append((i, j))
        self.Player_birth=birthPos[random.randint(0,len(birthPos))]

        print(movepath[self.Player_birth[0]][self.Player_birth[1]])
        birthPos.remove(self.Player_birth)
        # print(Player_birth)
        Enemy_birth = []

        for i in range(0, n):
            Enemy_birth.append(random.choice(birthPos))
            if birthPos.count(Enemy_birth) > 0:
                birthPos.remove(Enemy_birth)

        self.player = Player(self.Player_birth, movepath, self.play_sprites,self.map.getBlock())
        for i in range(0, n):
            globals()['self.enemy' + str(i)] = Enemy(Enemy_birth[i], self.player.getpos(),movepath, self.enempy_sprites,self.map.getBlock())
