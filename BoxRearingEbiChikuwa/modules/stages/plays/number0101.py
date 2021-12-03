import math
import pygame
from modules.stages.play import StagesPlay

class StagesPlaysNumber0101(StagesPlay):
    def __new__(cls, image_loader, status, setting):
        self = super().__new__(cls, image_loader, status, setting)

        return self

    def initializeVariable(self, image_loader, status, setting):
        StagesPlay.initializeVariable(self, image_loader, status, setting)

        self.main_character_initial_position = [
            setting['window']['margin_left'] + setting['window']['block_size'] * 7,
            setting['window']['full_height'] - setting['window']['margin_bottom'] - setting['window']['block_size'],
        ]
        self.npc_position = [
            setting['window']['margin_left'],
            setting['window']['margin_top'] + setting['window']['block_size'] * 6,
        ]
        self.time_travel_zone_position = [
            setting['window']['margin_left'],
            setting['window']['margin_top'] + setting['window']['block_size'] * 10,
        ]

        # 左上が[0, 0]
        # 中中が[11, 7]
        # 右下が[22, 13]
        self.floating_block_infos = [
            self.getMovingXyByPosition(image_loader, status, setting, 11, 13, 'single'),

            self.getMovingXyByPosition(image_loader, status, setting, 14, 10, 'left'),
            self.getMovingXyByPosition(image_loader, status, setting, 15, 10, 'right'),

            self.getMovingXyByPosition(image_loader, status, setting, 18, 7, 'left'),
            self.getMovingXyByPosition(image_loader, status, setting, 19, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 20, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 21, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 22, 7, 'right'),

            self.getMovingXyByPosition(image_loader, status, setting, 14, 4, 'left'),
            self.getMovingXyByPosition(image_loader, status, setting, 15, 4, 'right'),

            self.getMovingXyByPosition(image_loader, status, setting, 11, 7, 'single'),

            self.getMovingXyByPosition(image_loader, status, setting, 7, 4, 'left'),
            self.getMovingXyByPosition(image_loader, status, setting, 8, 4, 'right'),

            self.getMovingXyByPosition(image_loader, status, setting, 0, 7, 'left'),
            self.getMovingXyByPosition(image_loader, status, setting, 1, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 2, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 3, 7, 'center'),
            self.getMovingXyByPosition(image_loader, status, setting, 4, 7, 'right'),

            self.getMovingXyByPosition(image_loader, status, setting, 0, 11, 'single'),
        ]

        self.enemy_infos = [
            self.getMovingXyByPosition(image_loader, status, setting, 15, 13, self.character_factory._KIND_TAKO),
            self.getMovingXyByPosition(image_loader, status, setting, 5, 10, self.character_factory._KIND_TAI),
            self.getMovingXyByPosition(image_loader, status, setting, 3, 12, self.character_factory._KIND_NIIHAMA_TAIKODAI),
        ]

        return

    def __del__(self):
        super().__del__()

        del(self.main_character_initial_position)
        del(self.npc_position)
        del(self.time_travel_zone_position)
        del(self.floating_block_infos)
        del(self.enemy_infos)

        return
    
