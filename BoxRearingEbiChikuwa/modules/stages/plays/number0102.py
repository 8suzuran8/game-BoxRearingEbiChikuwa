import math
import pygame
from modules.stages.play import StagesPlay

class StagesPlaysNumber0102(StagesPlay):
    def __new__(cls, image_loader, status, setting):
        self = super().__new__(cls, image_loader, status, setting)

        return self

    def initializeVariable(self, image_loader, status, setting):
        StagesPlay.initializeVariable(self, image_loader, status, setting)

        self.next_stage = -3

        # 左上が[0, 0]
        # 中中が[11, 7]
        # 右下が[22, 13]

        # self.main_character_initial_position = self.getMovingXyByPosition(image_loader, status, setting, 5, 13)
        self.main_character_initial_position = self.getMovingXyByPosition(image_loader, status, setting, 1, 9)
        self.npc_position = self.getMovingXyByPosition(image_loader, status, setting, 22, 5)
        self.time_travel_zone_position = self.getMovingXyByPosition(image_loader, status, setting, 0, 13)

        self.floating_block_infos = list()

        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 0, 10, 'left'))
        for i in range(1, 22 - 3):
            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, i, 10, 'center'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, i + 1, 10, 'right'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, i + 2, 11, 'single'))

        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 2, 7, 'single'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 3, 6, 'left'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 4, 6, 'right'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 5, 6, 'moving'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 15, 6, 'left'))
        for i in range(16, 22):
            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, i, 6, 'center'))
        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, i + 1, 6, 'right'))

        self.enemy_infos = [
            self.getMovingXyByPosition(image_loader, status, setting, 11, 12, self.character_factory._KIND_NIIHAMA_TAIKODAI),
        ]

        return

    def __init__(self, image_loader, status, setting):
        super().__init__(image_loader, status, setting)

        return

    def __del__(self):
        super().__del__()

        del(self.next_stage)
        del(self.main_character_initial_position)
        del(self.npc_position)
        del(self.time_travel_zone_position)
        del(self.floating_block_infos)
        del(self.enemy_infos)

        return
    
