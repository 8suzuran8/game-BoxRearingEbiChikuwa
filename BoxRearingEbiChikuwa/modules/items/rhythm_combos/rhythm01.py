import pygame
from modules.items.rhythm_combo import ItemsRhythmCombo

class ItemsRhythmCombosRhythm01(ItemsRhythmCombo):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        # 24個ぴったり必要
        # [True, pygame.K_SPACE] # 黒 and キー
        # [True, False] # 白
        # [False, False] # 透明(描画無し)
        self.target_rhythm_and_keys = [
            [True, pygame.K_SPACE],
            [True, False],
            [True, pygame.K_SPACE],
            [True, pygame.K_SPACE],
            [True, pygame.K_SPACE],

            # 3つの空白
            [False, False],
            [False, False],
            [False, False],

            [True, False],
            [True, False],
            [True, pygame.K_RIGHT],
            [True, False],
            [True, pygame.K_RIGHT],
            [True, pygame.K_RIGHT],
            [True, pygame.K_RIGHT],

            # 1つの空白
            [False, False],

            [True, pygame.K_z],
            [True, False],
            [True, pygame.K_z],
            [True, False],
            [True, pygame.K_z],

            # 3つの空白
            [False, False],
            [False, False],
            [False, False],
        ]

        ItemsRhythmCombo.initializeVariable(self, image_loader, status, setting, path, info)

        return

    def __del__(self):
        super().__del__()

        del(self.target_rhythm_and_keys)

        return
