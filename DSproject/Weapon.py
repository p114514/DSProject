import pygame
from settings import *
from support import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.ATK = 100
        self.frame_index = 0
        self.pics = {'right': r'./weapon/0.png', 'left': r'./weapon/1.png', 'up': r'./weapon/2.png',
                     'down': r'./weapon/3.png'}

    def setWeapon(self, status, pos):
        self.status = status
        self.image = pygame.image.load(self.pics[self.status])
        self.rect = self.image.get_rect(topleft=pos)


