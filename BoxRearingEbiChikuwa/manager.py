import math
import pygame
from modules.stages.factory import StageFactory
from modules.common.image_loader import ImageLoader

class Manager:
    status = {'score': 0, 'stage': '0101'}
    setting = {'language': 'en', 'speed': 0, 'difficult': 0, 'window': {}, 'font': None}
    image_loader = False

    def __new__(cls):
        self = super().__new__(cls)
        return self

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # pygame.display.set_mode((0, 0))
        self.image_loader = ImageLoader()
        self.image_loader.setting(self.setting['language'])

        window_size = pygame.display.get_surface().get_size()

        self.setting['window']['block_size'] = 50
        self.setting['window']['full_width'] = window_size[0]
        self.setting['window']['full_height'] = window_size[1]
        self.setting['window']['moving_width'] = math.floor(window_size[0] * 0.8 / self.setting['window']['block_size']) * self.setting['window']['block_size'] # 可動領域の幅
        self.setting['window']['moving_height'] = math.floor(window_size[1] * 0.8 / self.setting['window']['block_size']) * self.setting['window']['block_size'] # 可動領域の高さ
        self.setting['window']['margin_left'] = math.ceil((window_size[0] - self.setting['window']['moving_width']) / 2)
        self.setting['window']['margin_top'] = math.ceil((window_size[1] - self.setting['window']['moving_height']) / 2) + self.setting['window']['block_size']
        self.setting['window']['margin_right'] = window_size[0] - self.setting['window']['moving_width'] - self.setting['window']['margin_left']
        self.setting['window']['margin_bottom'] = window_size[1] - self.setting['window']['moving_height'] - self.setting['window']['margin_top']

    def __del__(self):
        # ゲーム終了を表す
        pass

    def start(self):
        next_stage_kind = 0

        while True:
            self.current_stage = StageFactory().create(next_stage_kind, self.image_loader, self.status, self.setting)
            if self.current_stage == None:
                break;

            next_stage_kind = self.current_stage.start(self.image_loader, self.status, self.setting)
            if next_stage_kind == -2:
                pygame.time.wait(1000)

            del(self.current_stage)
            self.image_loader.resetMessage()
