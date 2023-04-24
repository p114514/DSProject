import sys
from settings import *
from level import Level
from DSproject.Interface_component import *


class InterFace:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.size = SCREEN_WIDTH,SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.clock.tick(60)
        self.mute = False
        self.full_screen = False
        self.button_back = ButtonColorSurface(Color.TRANSPARENT, 26, 26)
        self.button_mute = ButtonImage('rec.png', 0.5)
        self.button_full = ButtonImage('rec.png', 0.5)
        self.button_check = ButtonImage('rec_y.png', 0.5)

        pygame.mixer.init()
        pygame.mixer.music.load('music/Chris Lehman-Empyrean.mp3')
        pygame.mixer.music.play(-1, 0)

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
            if (option_hover):
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
        # 设置开始界面

        self.option_background_draw()
        # 设置背景贴图
        # option_bg = pygame.image.load("image/option_bg.jpg")

        return self.size, self.screen

    def option_background_draw(self):
        screen = self.screen
        width, height = SCREEN_WIDTH, SCREEN_HEIGHT

        Image('option_bg2.jpg', 0.18).draw(self.screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Image('返回.png', ratio=0.38).draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)

        self.button_back.draw(self.screen, SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.047)

        Text('全屏', Color.ACHIEVEMENT, 'xxyl.ttf', 38).draw(screen, width / 5, height * 0.30)
        Text('静音', Color.ACHIEVEMENT, 'xxyl.ttf', 38).draw(self.screen, SCREEN_WIDTH / 5, SCREEN_HEIGHT * 0.20)


        Text('音量大小', Color.ACHIEVEMENT, 'xxyl.ttf', 32).draw(screen, width / 5, height * 0.40)
        Text('制作人名单', Color.ACHIEVEMENT, 'xxyl.ttf', 40).draw(screen, width * 0.73, height * 0.20)
        Text('A', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.30)
        Text('B', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.38)
        Text('C', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.46)
        Text('D', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.54)
        Text('E', Color.ACHIEVEMENT, 'xxyl.ttf', 30).draw(screen, width * 0.73, height * 0.62)

    def option_interface(self):
        pygame.display.set_caption("Dungeon Tour")
        size, screen = self.option_background()
        width, height = size
        Text('静音', Color.ACHIEVEMENT, 'xxyl.ttf', 38).draw(screen, width / 5, height * 0.20)
        self.mute_judge()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(114514)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.button_back.handle_event(self.start_interface)
                    self.button_mute.handle_event(self.mutefunc)
                    self.button_full.handle_event(self.fullfunc)

            pygame.display.update()

    def mutefunc(self):
        self.mute = not self.mute
        self.mute_judge()
        if not self.mute:
            pygame.mixer.music.play(-1, 0)
        else:
            pygame.mixer.music.stop()

    def mute_judge(self):
        if not self.mute:
            self.option_background_draw()
            self.button_mute.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.2)

        else:
            self.option_background_draw()
            self.button_check.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.2)

        if self.full_screen:
            self.button_check.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.3)
        else:
            self.button_full.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.3)

    def fullfunc(self):
        self.full_screen = not self.full_screen
        self.full_screen1()

    def full_screen1(self):
        if not self.full_screen:
            self.mute_judge()
            self.button_full.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.3)
        else:
            self.mute_judge()
            button_mute_check = ButtonImage('rec_y.png', 0.5)
            button_mute_check.draw(self.screen, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.3)
