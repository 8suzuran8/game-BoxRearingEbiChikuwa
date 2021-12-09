import pygame
from modules.physical import Physical

class CharacterTai(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [
            ['swim', 'swim'],
        ]
        self.animation_max = [4]
        self.animation_file_max = [4]

        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(self.animation_max[0]):
            self.frames[frame_index].append(image_loader.get('characters/subs/tai/swim' + str(i) + '.svg'))

        self.x_distance = -3
        self.need_fall = False

        return

    def hookHitWall(self, kind):
        self.x_distance *= -1
        self.y_distance *= -1

        return
