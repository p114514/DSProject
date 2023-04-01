import pygame
from settings import *
from support import *

from mapeditor import myMap

import math


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, movepath, group,obstacle_sprite):
        super().__init__(group)
        self.movepath = movepath
        # sprite image initialization
        self.import_assets()
        self.status = 'right'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)
        self.speed = 200  # can modify later
        # self.noMove = []
        self.obstacle=obstacle_sprite
        #print(self.obstacle)
        # print(self.movepath)

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

        if self.direction_vector.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        elif self.direction_vector.y == -1:
            self.status = 'back'
        elif self.direction_vector.x == 1:
            self.status = 'left'
        else:
            self.status = 'right'

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)

    def move(self, dt):  # needs to modify later

        if self.direction_vector.magnitude() > 0:
            self.direction_vector = self.direction_vector.normalize()
        predictx= self.rect.x+self.direction_vector.x * self.speed * dt
        predicty =  self.rect.y+self.direction_vector.y * self.speed * dt
        #print(self.rect,(predictx,predicty))

        if predictx<0 or predictx>=SCREEN_WIDTH-1:

            #print(self.direction_vector.y)

            self.rect.x += self.direction_vector.x * self.speed * dt
            self.collision("horizontal")
            self.pos_vector = pygame.math.Vector2(self.rect.center)
        elif predicty < 0 or predicty >= SCREEN_HEIGHT-1:

            #print(self.direction_vector.x)

            self.rect.y += self.direction_vector.y * self.speed * dt
            self.collision("vertical")
            self.pos_vector = pygame.math.Vector2(self.rect.center)
        else:
            self.rect.x += self.direction_vector.x * self.speed * dt
            self.collision("horizontal")
            self.rect.y += self.direction_vector.y * self.speed * dt
            self.collision("vertical")
            self.pos_vector=pygame.math.Vector2(self.rect.center)




    def collision(self,direction):
        if direction=="horizontal":
         for sp in self.obstacle:
            if sp.rect.colliderect(self.rect):
                if self.direction_vector.x>0:
                    self.rect.right=sp.rect.left
                if self.direction_vector.x<0:
                    self.rect.left = sp.rect.right
        if direction == "vertical":
            for sp in self.obstacle:
                if sp.rect.colliderect(self.rect):
                    if self.direction_vector.y > 0:
                        self.rect.bottom = sp.rect.top
                    if self.direction_vector.y < 0:
                        self.rect.top = sp.rect.bottom

    def getpos(self):
        return self.pos_vector
    def setPos(self,pos):
        self.rect.center=pos
    def import_assets(self):
        self.animations = {'right': [], 'left': [], 'back': [], 'right_idle': [], 'left_idle': [], 'back_idle': []}

        for animation in self.animations.keys():
            full_path = r'./player/' + animation

            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
