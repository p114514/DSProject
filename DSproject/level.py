import pygame
from settings import *
from player import Player
from enemy import  Enemy
from mapeditor import myMap
class Level:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.map = myMap(self.display_surface)
        # setup
        self.setup()

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.map.drawWall()
        #map‘s level is above the sprite
        self.all_sprites.update(dt)

    def setup(self):

        movepath = self.map.getmaze().copy()

        maze=self.map.getmaze().copy()
        mazerow=self.map.getmazerow()
        mazecol=self.map.getmazecol()
        cellcol=self.map.getcell_col()
        cellrow=self.map.getcell_row()
        flag=1
        for i in range(0, mazerow):
            for j in range(0, mazecol):
                if maze[i][j] == 1 and flag==1:
                   self.player = Player((cellrow[i], cellcol[j]),movepath, self.all_sprites)
                   maze[i][j]=0
                   flag=0
        flag=1
        for i in range(0, mazerow):
            for j in range(0, mazecol):
                if maze[i][j] == 1 and flag==1:
                   self.enemy = Enemy((cellrow[i], cellcol[j]), movepath,self.all_sprites)
                   maze[i][j]=0
                   flag=0


