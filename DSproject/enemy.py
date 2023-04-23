import pygame
from player import Player
from settings import *
import random
from math import *

from support import import_folder


class Enemy(Player):
    def __init__(self, pos, playerpos, movepath, group, obscatle_sprite, trap_sprite):

        super(Enemy, self).__init__(pos, movepath, group, obscatle_sprite, trap_sprite)
        # import assets and surface setup
        self.import_assets()
        self.status = 'right'
        self.frame_index = 0
        self.image = self.animations[self.status][self.frame_index]

        # general setup
        self.rect = self.image.get_rect(center=pos)
        self.movepath = movepath
        # movement
        self.playerpos = playerpos
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 120  # can modify later
        self.step = 50

        self.roomNO=[0,0]

    def update(self, dt):
        self.randMove(dt)
        self.animate(dt)

        self.invincibility()

    def setPlayerPos(self, playerpos):
        self.playerpos = playerpos

    def randMove(self, dt):  # needs to modify later
        # if self.Astep>0 and (self.pos_vector-self.playerpos).magnitude()<100:
        #     self.direction_vector=self.dir_list[self.temp-self.Astep]
        #     self.move(dt)
        #     self.Astep-=1
        # else:
        #     self.dir_list=A(self.playerpos).copy
        #     self.Astep=len(self.dir_list)
        #     self.temp=len(self.dir_list)

        if (self.pos_vector - self.playerpos).magnitude() < 500:
            if (self.playerpos - self.pos_vector) != pygame.math.Vector2(0, 0):
                self.direction_vector = (self.playerpos - self.pos_vector).normalize()
                # print(self.direction_vector)
                self.move(dt)
        else:
            left_unit_vector = pygame.math.Vector2(-1, 0)
            right_unit_vector = pygame.math.Vector2(1, 0)
            up_unit_vector = pygame.math.Vector2(0, 1)
            down_unit_vector = pygame.math.Vector2(0, -1)
            self.left = self.pos_vector + pygame.math.Vector2(-1, 0) * self.speed * dt
            self.right = self.pos_vector + pygame.math.Vector2(1, 0) * self.speed * dt
            self.up = self.pos_vector + pygame.math.Vector2(0, 1) * self.speed * dt
            self.down = self.pos_vector + pygame.math.Vector2(0, -1) * self.speed * dt
            if self.right.x > GAME_SCREEN_WIDTH:
                self.direction_vector = random.choice((left_unit_vector, up_unit_vector, down_unit_vector))
            if self.left.x < 0:
                self.direction_vector = random.choice((right_unit_vector, up_unit_vector, down_unit_vector))
            if self.up.y > GAME_SCREEN_HEIGHT:
                self.direction_vector = random.choice((left_unit_vector, right_unit_vector, down_unit_vector))
            if self.down.y < 0:
                self.direction_vector = random.choice((left_unit_vector, right_unit_vector, up_unit_vector))
            if self.step <= 0:
                self.direction_vector = random.choice(
                    (left_unit_vector, right_unit_vector, up_unit_vector, down_unit_vector))
                self.step = 100
            else:
                self.move(dt)
                self.step -= 1

        if self.direction_vector.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        elif self.direction_vector.y == -1:
            self.status = 'back'
        elif self.direction_vector.x == 1:
            self.status = 'left'
        else:
            self.status = 'right'

    def import_assets(self):
        self.animations = {'right': [], 'left': [], 'back': [], 'right_idle': [], 'left_idle': [], 'back_idle': []}
        for animation in self.animations.keys():
            full_path = r'./enemy/' + animation
            self.animations[animation] = import_folder(full_path)


