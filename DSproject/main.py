from game import Game
import os
import random
import sys
from settings import *
import pygame
from pygame import font
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
import pygame, sys
from settings import *
from level import Level
from mapeditor import myMap
from calendar import c


class Color:
    # 自定义颜色
    ACHIEVEMENT = (220, 160, 87)
    VERSION = (220, 160, 87)

    # 固定颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)  # 中性灰
    TRANSPARENT = (255, 255, 255, 0)  # 白色的完全透明


class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        """
        text: 文本内容，如'大学生模拟器'，注意是字符串形式
        text_color: 字体颜色，如Color.WHITE、COLOR.BLACK
        font_type: 字体文件(.ttc)，如'msyh.ttc'，注意是字符串形式
        font_size: 字体大小，如20、10
        """
        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size

        font = pygame.font.Font(os.path.join('font', (self.font_type)), self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()

        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (upperleft_x, upperleft_y))


class Image:
    def __init__(self, img_name: str, ratio=0.4):
        """
        img_name: 图片文件名，如'background.jpg'、'ink.png',注意为字符串
        ratio: 图片缩放比例，与主屏幕相适应，默认值为0.4
        """
        self.img_name = img_name
        self.ratio = ratio

        self.image_1080x1920 = pygame.image.load(os.path.join('image', self.img_name)).convert_alpha()
        self.img_width = self.image_1080x1920.get_width()
        self.img_height = self.image_1080x1920.get_height()

        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio

        self.image_scaled = pygame.transform.smoothscale(self.image_1080x1920, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))

    def set_alpha(self,alpha):
        self.image_scaled.set_alpha(alpha)


class ColorSurface:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

        self.color_image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.color_image.fill(self.color)

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.width / 2
        upperleft_y = center_y - self.height / 2
        surface.blit(self.color_image, (upperleft_x, upperleft_y))


class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()


class ButtonImage(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()


class ButtonColorSurface(ColorSurface):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.rect = self.color_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)


class InterFace():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.clock.tick(60)

    def basic_background(self):

        # 设置logo和界面标题
        game_icon = pygame.image.load(os.path.join('image', 'game_logo.png'))
        game_caption = 'Dungeon Tour'
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption(game_caption)

        # 设置开始界面
        size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
        screen = pygame.display.set_mode(size)

        # 设置背景贴图
        Image('bg3.jpg', 0.6).draw(screen, width / 2, height / 2)

        return size, screen

    def start_interface(self):
        """
        <开始界面><start_interface>
        """
        # 设置<基本背景>
        size, screen = self.basic_background()
        width, height = size

        # 设置<开始界面>文字和贴图
        #        Image('ink.png', ratio=0.4).draw(screen, width * 0.52, height * 0.67)  # 墨印

        button_game_start = ButtonText('开始游戏', Color.BLACK, 'aajht.ttf', 50)  # 开始游戏按钮
        button_game_option = ButtonText('选  项', Color.BLACK, 'aajht.ttf', 50)

        while True:
            Image('bg3.jpg', 0.6).draw(screen, width / 2, height / 2)
            Image('achievement_icon.png', ratio=0.3).draw(screen, width * 0.93, height * 0.05)  # 成就按钮

            Text('地牢使者', Color.BLACK, 'aajht.ttf', 90).draw(screen, width / 2, height * 0.36)  # 游戏名
            Text('Alpha 0.0', Color.VERSION, 'aajht.ttf', 12).draw(screen, width / 2, height * 0.97)  # 版本号
            Text('成就', Color.ACHIEVEMENT, 'aajht.ttf', 16).draw(screen, width * 0.93, height * 0.10)  # 成就

            button_game_start = ButtonText('开始游戏', Color.BLACK, 'aajht.ttf', 50)  # 开始游戏按钮

            button_game_start.draw(screen, width / 2, height * 0.55)
            button_game_option.draw(screen, width / 2, height * 0.65)

            start_hover = button_game_start.rect.collidepoint(pygame.mouse.get_pos())
            option_hover = button_game_option.rect.collidepoint(pygame.mouse.get_pos())

            hover_image = Image('ink.png', ratio=0.35)
            hover_image.set_alpha(100)


            if (start_hover):
                hover_image.draw(screen, width / 2, height * 0.55)
            if(option_hover):
                hover_image.draw(screen, width / 2, height * 0.65)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_game_start.handle_event(self.initial_attribute_interface)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_game_option.handle_event(self.option_interface)




            pygame.display.update()

    def initial_attribute_interface(self):

        pygame.display.set_caption('Dungeon Tour')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(114514)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_back.handle_event(self.start_interface)

            dt = self.clock.tick() / 1000

            self.level.run(dt)
            Image('返回.png', ratio=0.38).draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)
            button_back = ButtonColorSurface(Color.TRANSPARENT, 26, 26)
            button_back.draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)

            pygame.display.update()

    def option_background(self):

        # 设置logo和界面标题
        game_icon = pygame.image.load(os.path.join('image', 'game_logo.png'))
        game_caption = 'Dungeon Tour'
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption(game_caption)

        # 设置开始界面
        size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
        screen = pygame.display.set_mode(size)

        # 设置背景贴图
        # option_bg = pygame.image.load("image/option_bg.jpg")
        Image('option_bg2.jpg', 0.18).draw(screen, width / 2, height / 2)
        return size, screen

    def option_interface(self):
        pygame.display.set_caption("Dungeon Tour")
        size, screen = self.option_background()
        width, height = size
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(114514)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_back.handle_event(self.start_interface)

            Image('返回.png', ratio=0.38).draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)
            button_back = ButtonColorSurface(Color.TRANSPARENT, 26, 26)
            button_back.draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)

            Text('静音', Color.ACHIEVEMENT, 'xxyl.ttf', 38).draw(screen, width / 5, height * 0.20)
            Text('全屏', Color.ACHIEVEMENT, 'xxyl.ttf', 38).draw(screen, width / 5, height * 0.30)
            Text('音量大小', Color.ACHIEVEMENT, 'xxyl.ttf', 32).draw(screen, width / 5, height * 0.40)

            Text('制作人名单', Color.ACHIEVEMENT, 'xxyl.ttf', 40).draw(screen, width * 0.73, height * 0.20)
            Text('A', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.30)
            Text('B', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.38)
            Text('C', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.46)
            Text('D', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.54)
            Text('E', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.62)
            pygame.display.update()


if __name__ == '__main__':
    scene = InterFace()
    # 开始时选定start_interface
    scene.start_interface()
