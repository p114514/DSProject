import math

import pygame
from Interface_component import *
from settings import *
from support import *
from Weapon import Weapon
from  Magic import *
from mapeditor import myMap

from math import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, movepath, group, obstacle_sprite, trap_sprite):
        super().__init__(group)

        self.weapon_sprites = pygame.sprite.Group()
        self.WeaponList = []

        self.magic_sprites= pygame.sprite.Group()
        self.MagicList = ["Circle",'Shoot']
        self.handMagic = self.MagicList[1]


        # Status of player
        self.HP = 100


        self.ATK = 100

        self.DEF = 50
        self.MP = 100

        # sprite image initialization
        self.import_assets()
        self.status = 'right'
        self.weapon_status='left'
        self.weapon_pos = {'right': [16,0], 'left': [-16,0], 'up': [0,-16], 'down':[0,16]}

        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        # movement
        self.direction_vector = pygame.math.Vector2(0, 0)
        self.pos_vector = pygame.math.Vector2(self.rect.center)

        self.normal_speed = 100
        self.reduced_speed = 90
        self.speed = self.normal_speed  # can modify later
        self.movepath = movepath

        ###sprites from map
        self.obstacle = obstacle_sprite
        self.traps = trap_sprite
        self.enemy_sprite = pygame.sprite.Group()

        self.invincible = False
        self.getDMG = False
        self.getPushDir = pygame.math.Vector2(0, 0)
        self.last_hit_time = 0

    def input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed *= 2
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
            self.weapon_status='up'
        elif self.direction_vector.y == 1:
            self.status = 'right'
            self.weapon_status='down'
        elif self.direction_vector.x == 1:
            self.status = 'left'
            self.weapon_status='right'
        else:
            self.status = 'right'
            self.weapon_status='left'

        ####武器、魔法待实现
        if keys[pygame.K_1]:
            handWeapon = Weapon(self.weapon_sprites)
            handWeapon.setWeapon(self.weapon_status, (self.rect.x + self.weapon_pos[self.weapon_status][0],
                                                  self.rect.y + self.weapon_pos[self.weapon_status][1]))
            self.weapon_sprites.draw(self.display_surface)

            self.attack(handWeapon, self.enemy_sprite)
        if keys[pygame.K_2]:
            self.doMagic()



    def take_damage(self, damage):
        if not self.invincible:
            self.HP -= damage
            self.invincible = True
            self.last_hit_time = pygame.time.get_ticks()





    def take_damage(self, damage, fromWhich):
        if not self.invincible:
            self.HP -= damage
            self.invincible = True
            ###mark for get damage
            self.getDMG = True
            self.last_hit_time = pygame.time.get_ticks()
            self.getPushDir = -pygame.math.Vector2(fromWhich.rect.x - self.rect.x, fromWhich.rect.y - self.rect.y)

            hit1_sound.set_volume(Sound.hit_volume)
            hit1_sound.play()



    def invincibility(self):
        if pygame.time.get_ticks() - self.last_hit_time > 100:
            self.invincible = False
            self.getDMG = False

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.stepontrap()
        self.invincibility()

        if not self.weapon_sprites.empty():
          for sp in self.weapon_sprites:
            sp.setWeapon(self.weapon_status, (self.rect.x +self.weapon_pos[self.weapon_status][0], self.rect.y+self.weapon_pos[self.weapon_status][1]))
        self.magic_sprites.draw(self.display_surface)
        self.magic_sprites.update(dt)
        self.MP += dt * 10

        if self.MP > 100: self.MP = 100

    def move(self, dt):  # needs to modify later

        if self.getDMG == 1:
            self.direction_vector = self.getPushDir

        if self.direction_vector.magnitude() > 0:
            self.direction_vector = self.direction_vector.normalize()
        predictx = self.rect.x + self.direction_vector.x * self.speed * dt
        predicty = self.rect.y + self.direction_vector.y * self.speed * dt
        # print(self.rect,(predictx,predicty))
        if predictx < 0 or predictx >= GAME_SCREEN_WIDTH - 1:

            # print(self.direction_vector.y)

            self.rect.x += self.direction_vector.x * self.speed * dt
            self.collision("horizontal")
            self.pos_vector = pygame.math.Vector2(self.rect.center)

        elif predicty < 0 or predicty >= GAME_SCREEN_HEIGHT - 1:

            # print(self.direction_vector.x)

            self.rect.y += self.direction_vector.y * self.speed * dt
            self.collision("vertical")
            self.pos_vector = pygame.math.Vector2(self.rect.center)
        else:
            self.rect.x += self.direction_vector.x * self.speed * dt
            self.collision("horizontal")
            self.rect.y += self.direction_vector.y * self.speed * dt
            self.collision("vertical")
            self.pos_vector = pygame.math.Vector2(self.rect.center)

    def collision(self, direction):
        if direction == "horizontal":
            for sp in self.obstacle:
                if sp.rect.colliderect(self.rect):
                    if self.direction_vector.x > 0:
                        self.rect.right = sp.rect.left
                    if self.direction_vector.x < 0:
                        self.rect.left = sp.rect.right
        if direction == "vertical":
            for sp in self.obstacle:
                if sp.rect.colliderect(self.rect):
                    if self.direction_vector.y > 0:
                        self.rect.bottom = sp.rect.top
                    if self.direction_vector.y < 0:
                        self.rect.top = sp.rect.bottom

        for sp in self.enemy_sprite:
            if sp.rect.colliderect(self.rect):
                self.take_damage(sp.ATK - self.DEF, sp)
                sp.take_damage(0, self)

    def stepontrap(self):
        flag = False
        for trap_sprite in self.traps:
            if self.rect.colliderect(trap_sprite):
                flag = True

        if flag:
            self.speed = self.reduced_speed
        else:
            self.speed = self.normal_speed

    def setEnemy(self, enemy):
        self.enemy_sprite = enemy

    def attack(self, AttackMethod, enemyGroup):
        for sp in enemyGroup:
            if sp.rect.colliderect(AttackMethod.rect):
                sp.take_damage(self.ATK - sp.DEF, AttackMethod)

    # 利用碰撞检测实现attack
    def doMagic(self):
        if self.handMagic == "Circle":
            if self.MP >= 1:
                self.MP -= 1
                xval = self.rect.x + cos(pygame.time.get_ticks()) * 50
                yval = self.rect.y + sin(pygame.time.get_ticks()) * 50
                pos = (xval, yval)
                tempS = pygame.sprite.Group()
                tempW = Weapon(tempS)
                tempW.setWeapon('right', pos)
                tempW.image = pygame.transform.rotate(tempW.image, -math.degrees(pygame.time.get_ticks()))
                tempS.draw(self.display_surface)
                self.attack(tempW, self.enemy_sprite)

        elif self.handMagic == "Shoot":
                print("ok")
                if self.MP >= 10:
                    self.MP -= 10
                magic=Magic(self.magic_sprites)
                magic.setMagic(self.weapon_status,(self.rect.x +self.weapon_pos[self.weapon_status][0], self.rect.y+self.weapon_pos[self.weapon_status][1]),self.enemy_sprite,self.obstacle)





    def getpos(self):
        return self.pos_vector

    def setPos(self, pos):
        self.rect.center = pos

    def setDisplaySur(self, sur):
        self.display_surface = sur

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
        if self.getDMG == True:
            value = sin(pygame.time.get_ticks())
            if value >= 0:
                value = 255
            else:
                value = 0
            self.image.set_alpha(value)

        else:
            self.image.set_alpha(255)
