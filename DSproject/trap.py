import pygame
from settings import *


class TrapTile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Trap:
    def __init__(self, all_sprites):
        # surface groups
        self.all_sprites = all_sprites
        self.trap_sprites = pygame.sprite.Group()

        # graphics
        self.trap_surf = pygame.image.load(r'./trap/143.png').convert_alpha()

    def create_trap_tile(self, matrix, ry, rx):
        self.trap_sprites.empty()
        resizeW = rx
        resizeH = ry
        self.trap_surf = pygame.transform.scale(self.trap_surf, (resizeW, resizeH))

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[y][x] == 8:
                    TrapTile((x * resizeW, y * resizeH), self.trap_surf, self.trap_sprites)

    def getTrapGroup(self):
        return self.trap_sprites
