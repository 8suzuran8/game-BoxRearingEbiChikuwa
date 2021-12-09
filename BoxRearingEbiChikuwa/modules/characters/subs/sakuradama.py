import math
import pygame
from modules.physical import Physical

class CharacterSakuradama(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [
            ['stand', 'stand'],
        ]

        self.clear = False

        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(self.animation_max[0]):
            self.frames[frame_index].append(image_loader.get('characters/subs/sakuradama/stand.svg'))

        self.need_fall = False

        return

    def __del__(self):
        Physical.__del__(self)

        del(self.clear)

        return
