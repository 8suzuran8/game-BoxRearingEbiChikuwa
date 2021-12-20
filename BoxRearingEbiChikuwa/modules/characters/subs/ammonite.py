import pygame
from modules.physical import Physical

class CharacterAmmonite(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [['swim', 'swim']]

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('characters/subs/ammonite/' + animation_type_info[1] + '.svg'))

            animation_type_index += 1

        self.unbeatable = True
        self.x_distance = 0
        self.y_distance = +1
        self.need_fall = False

        return

    def hookHitWall(self, kind):
        self.y_distance *= -1
        self.x_distance *= -1

        return
