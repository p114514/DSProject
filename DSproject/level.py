import random

import pygame
from settings import *
from player import Player
from enemy import Enemy
from mapeditor import myMap

n = 10  # number of enemies


class Level:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.enemy_sprites = pygame.sprite.Group()
        self.temp = pygame.sprite.Group()
        self.play_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.map = myMap(self.display_surface, self.all_sprites)
        # setup
        self.curRoom = [0, 0]
        self.RR = self.map.getRoomRC()[0]
        self.RC = self.map.getRoomRC()[1]
        self.map.drawRoom(self.curRoom[0], self.curRoom[1])
        self.isShift = 0
        self.setup()
        # print(self.map.getMoveArea())

    def run(self, dt):
        if self.player.rect.x <= 0 or self.player.rect.x >= GAME_SCREEN_WIDTH or self.player.rect.y <= 0 or self.player.rect.y >= GAME_SCREEN_HEIGHT:
            self.shiftRoom()
        self.display_surface.fill('black')
        self.map.drawRoom(self.curRoom[0], self.curRoom[1])
        playerpos = self.player.getpos()

        ####移除不在该房间的enemy 用temp保存 下次回来时调用
        for sp in self.temp:
            self.enemy_sprites.add(sp)
        for sp in self.enemy_sprites:
            if sp.roomNO[0] != self.curRoom[0] or sp.roomNO[1]!=self.curRoom[1]:
                self.enemy_sprites.remove(sp)
                self.temp.add(sp)

        for sp in self.enemy_sprites:
            print(sp.pos_vector,sp.HP)
        self.enemy_sprites.draw(self.display_surface)
        self.play_sprites.draw(self.display_surface)
        #####draw Enemy



        ###generate new enemies
        if self.isShift == 1:
            self.map.initMoveArea()
            self.map.drawRoom(self.curRoom[0], self.curRoom[1])
            self.isShift = 0

        # map‘s level is above the sprite
        self.all_sprites.update(dt)
        self.play_sprites.update(dt)
        self.enemy_sprites.update(dt)
        # self.enemy_sprites.update(dt)
        # enemy gets player's position
        for sp in self.enemy_sprites:
            sp.setPlayerPos(playerpos)
        #####设置攻击对象
        self.player.setEnemy(self.enemy_sprites)
        #####kill enemy#####
        for sp in self.enemy_sprites:
            if sp.HP < 0:
                sp.kill()

    def shiftRoom(self):
        ##情况比较多 用树考虑比较好？
        # print(self.player.rect)
        if self.player.rect.x < 0:

            if self.curRoom[0] > 0:
                self.curRoom[0] -= 1
                self.player.rect.x = GAME_SCREEN_WIDTH - 1
                self.isShift = 1
            else:
                self.player.rect.x = 0
        elif self.player.rect.x > GAME_SCREEN_WIDTH:

            if self.curRoom[0] < self.RR - 1:
                self.curRoom[0] += 1
                self.player.rect.x = 0
                self.isShift = 1
            else:

                self.player.rect.x = GAME_SCREEN_WIDTH

        elif self.player.rect.y < 0:
            if self.curRoom[1] > 0:
                self.curRoom[1] -= 1
                self.player.rect.y = GAME_SCREEN_HEIGHT - 1
                self.isShift = 1
            else:
                self.player.rect.y = 0
        elif self.player.rect.y > GAME_SCREEN_HEIGHT:

            if self.curRoom[1] < self.RC - 1:
                self.curRoom[1] += 1
                self.player.rect.y = 0
                self.isShift = 1
            else:
                self.player.rect.y = GAME_SCREEN_HEIGHT

    def setup(self):
        movepath = self.map.getMoveArea()
        birthPos = []
        err = 30
        for i in range(err, GAME_SCREEN_HEIGHT - err):
            for j in range(err, GAME_SCREEN_WIDTH - err):
                if movepath[i][j] == 1 and (movepath[i + k][j + p] == 1 for k, p in [-err, err]):
                    birthPos.append((j, i))
        self.Player_birth = birthPos[random.randint(0, len(birthPos))]
        birthPos.remove(self.Player_birth)
        # print(Player_birth)
        self.player = Player(self.Player_birth, movepath, self.play_sprites, self.map.getBlock(), self.map.getTrap())
        self.player.setDisplaySur(self.display_surface)
        for i in range(0, n):
            roomNO=[random.randint(0,self.RR-1),random.randint(0, self.RC-1)]
            pos = self.map.getRoomBirthPos(roomNO)
            globals()['self.enemy' + str(i)] = Enemy(pos, self.player.getpos(), movepath,
                                                     self.enemy_sprites, self.map.getBlock(), self.map.getTrap())
            globals()['self.enemy' + str(i)].roomNO=roomNO

