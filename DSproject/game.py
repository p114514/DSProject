import pygame, sys
from settings import *
from level import Level
from mapeditor import myMap
from calendar import c


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('My name is Van')

        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(114514)

            dt = self.clock.tick() / 1000

            self.level.run(dt)

            pygame.display.update()
