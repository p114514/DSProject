from settings import *
import pygame
import numpy as np
from block import Block

from support import import_folder


########不能用精灵 太卡了
# -----------------------------------对象定义---------------------------------
class myMap:
    def __init__(self, screen, all_sprites):
        super().__init__()
        # modify maz

        self.mazelist = self.MazeGenerator()
        self.mazerow = np.shape(self.mazelist)[0]
        self.mazecol = np.shape(self.mazelist)[1]
        self.MoveArea = [[1 for i in range(0, SCREEN_WIDTH)] for j in range(0, SCREEN_HEIGHT)]
        # define para
        self.screen = screen
        self.xl = SCREEN_WIDTH // self.mazecol
        self.yl = SCREEN_HEIGHT // self.mazerow
        self.cell_row = range(0, SCREEN_HEIGHT, self.yl)
        self.cell_col = range(0, SCREEN_WIDTH, self.xl)

        self.all_sprites = all_sprites
        self.block = Block(self.all_sprites)

    def drawWall(self):
        self.block.create_block_tile(self.MazeGenerator())
        self.block.block_sprites.draw(self.screen)
        for i in range(0, self.mazerow):
            for j in range(0, self.mazecol):
                if self.mazelist[i][j] == 0:
                    for k in range(i * self.yl, (i + 1) * self.yl):
                        for p in range(j * self.xl, (j + 1) * self.xl):
                            self.MoveArea[k][p] = 0

    def getBlock(self):

        return self.block.getBlockGroup()
    def getMoveArea(self):
        return self.MoveArea

    def getMovePos(self):
        movepos = []
        for i in range(0, SCREEN_HEIGHT):
            for j in range(0, SCREEN_WIDTH):
                if self.MoveArea[i][j] == 1:
                    movepos.append((i, j))
        return movepos

    def getmaze(self):
        return self.mazelist

    def getmazerow(self):
        return self.mazerow

    def getmazecol(self):
        return self.mazecol

    def getcell_col(self):
        return self.cell_col

    def getcell_row(self):
        return self.cell_row

    def MazeGenerator(self):
        maze = (-1 * (np.array([[0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                               [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
                               [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                               [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
                               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
                               [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1],
                               [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                               [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                               [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                               [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                               [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                               [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                               [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]]) - 1)).tolist()
        return maze
