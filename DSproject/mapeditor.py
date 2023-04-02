from settings import *
import pygame
import numpy as np
from block import Block


# -----------------------------------对象定义---------------------------------
class myMap:
    def __init__(self, screen, all_sprites):
        super().__init__()
        # modify maz

        self.mazeMatrix = self.MazeGenerator()
        self.mazerow = np.shape(self.mazeMatrix)[0]
        self.mazecol = np.shape(self.mazeMatrix)[1]
        self.MoveArea = [[1 for i in range(0, SCREEN_WIDTH)] for j in range(0, SCREEN_HEIGHT)]

        self.Room_unit_Row = 2
        self.Room_unit_Col = 2

        self.RoomRow = self.mazerow // self.Room_unit_Row
        self.RoomCol = self.mazecol // self.Room_unit_Col
        # define para
        self.screen = screen
        self.xl = SCREEN_WIDTH // self.mazecol
        self.yl = SCREEN_HEIGHT // self.mazerow

        self.roomxl = SCREEN_WIDTH // self.RoomCol
        self.roomyl = SCREEN_HEIGHT // self.RoomRow

        self.cell_row = range(0, SCREEN_HEIGHT, self.yl)
        self.cell_col = range(0, SCREEN_WIDTH, self.xl)

        self.all_sprites = all_sprites
        self.block = Block(self.all_sprites)

    # def drawWall(self):
    #     self.block.create_block_tile( self.mazeMatrix)
    #     self.block.block_sprites.draw(self.screen)
    #     for i in range(0, self.mazerow):
    #         for j in range(0, self.mazecol):
    #             if self.mazeMatrix[i][j] == 0:
    #                 for k in range(i * self.yl, (i + 1) * self.yl):
    #                     for p in range(j * self.xl, (j + 1) * self.xl):
    #                         self.MoveArea[k][p] = 0
    def drawRoom(self, x, y):
        room = self.toRoom(self.mazeMatrix, y, x)
        self.pr = room
        self.block.create_block_tile(room, self.roomyl, self.roomxl)
        self.block.block_sprites.draw(self.screen)
        for i in range(0, self.RoomRow):
            for j in range(0, self.RoomCol):
                if room[i][j] == 0:
                    for k in range(max(i * self.roomyl - 10, 0), min((i + 1) * self.roomyl + 10, SCREEN_HEIGHT - 1)):
                        for p in range(max(j * self.roomxl - 10, 0), min((j + 1) * self.roomxl + 10,
                                                                         SCREEN_WIDTH - 1)):
                            self.MoveArea[k][p] = 0

    def toRoom(self, maze, i, j):
        room = np.zeros((self.RoomRow, self.RoomCol))
        for k in range(0, self.RoomRow):
            for p in range(0, self.RoomCol):
                room[k][p] = maze[k + i * self.RoomRow][p + j * self.RoomCol]
        return room

    def initMoveArea(self):
        self.MoveArea = [[1 for i in range(0, SCREEN_WIDTH)] for j in range(0, SCREEN_HEIGHT)]

    def printRoom(self):
        print(self.pr)

    def getRoomRC(self):
        return [self.RoomRow, self.RoomCol]

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
        return self.mazeMatrix

    def getmazerow(self):
        return self.mazerow

    def getmazecol(self):
        return self.mazecol

    def getcell_col(self):
        return self.cell_col

    def getcell_row(self):
        return self.cell_row

    def MazeGenerator(self):
        # maze = (-1 * (np.array([
        #                        [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        #                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        #                        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        #                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        #                        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        #                        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        #                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        #                        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        #                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        #                        [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        #                        [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        #                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        #                        [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        #                        [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        #                        [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                        [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        #                        [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        #                        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]]) - 1)).tolist()
        maze = np.array([[0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 1, 0],
                         [0, 1, 0, 0, 1, 0],
                         [0, 1, 0, 0, 1, 0],
                         [0, 1, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0, 0]]).tolist()
        return maze
