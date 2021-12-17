import pygame
from modules.character import Character

class CharacterTai(Character):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Character.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [
            ['swim', 'swim'],
        ]
        self.animation_max = [4]
        self.animation_file_max = [4]

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('characters/subs/tai/' + animation_type_info[1] + str(i).zfill(1) + '.svg'))

            animation_type_index += 1

        self.x_distance = -3
        self.need_fall = False

        return

    def hookHitWall(self, kind):
        self.x_distance *= -1
        self.y_distance *= -1

        return
