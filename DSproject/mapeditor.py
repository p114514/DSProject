from settings import *
import pygame
import  numpy as np


########不能用精灵 太卡了
# -----------------------------------对象定义---------------------------------
class myMap():
    def __init__(self,screen):
        super().__init__()
        #modify maze
        self.mazerow=4;
        self.mazecol=4;
        self.mazelist=np.array([[1,1,1,1],
                                [1,1,1,0],
                                [1,0,0,1],
                                [1,1,1,1]])
        self.MoveArea = [[1 for i in range(0,SCREEN_WIDTH)]for j in range(0,SCREEN_HEIGHT)]
        #define para
        self.screen=screen
        self.xl=SCREEN_WIDTH// self.mazecol
        self.yl=SCREEN_HEIGHT//self.mazerow
        self.cell_row=range(0,SCREEN_HEIGHT,self.yl)
        self.cell_col = range(0, SCREEN_WIDTH,self.xl)
    def drawWall(self):
        for i in range(0,self.mazerow):
            for j in range(0,self.mazecol):
                if self.mazelist[i][j]==0:
                  pygame.draw.rect(self.screen,(255,255,255),(self.cell_col[j],self.cell_row[i],self.xl,self.yl))
                  for k in range(i *self.yl,(i+1)* self.yl):
                      for p in range(j *self.xl,(j+1)* self.xl):
                         self.MoveArea[k][p]=0






    def getMoveArea(self):
        return self.MoveArea
    def getMovePos(self):
        movepos=[]
        for i in range(0,SCREEN_HEIGHT):
            for j in range(0,SCREEN_WIDTH):
                if self.MoveArea[i][j]==1:
                    movepos.append((i,j))
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






