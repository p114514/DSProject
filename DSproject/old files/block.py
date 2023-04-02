import pygame
from settings import *


class BlockTile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Block:
    def __init__(self, all_sprites):
        # surface groups
        self.all_sprites = all_sprites
        self.block_sprites = pygame.sprite.Group()

        # graphics
        self.block_surf = pygame.image.load(r'./block/block.png').convert_alpha()

    def create_block_tile(self, matrix):
        self.block_sprites.empty()
        resizeW = SCREEN_WIDTH // len(matrix)
        resizeH = SCREEN_HEIGHT // len(matrix[0])
        self.block_surf = pygame.transform.scale(self.block_surf, (resizeW, resizeH))

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    BlockTile((x * resizeW, y * resizeH), self.block_surf, self.block_sprites)

    def getBlockGroup(self):
        return self.block_sprites
