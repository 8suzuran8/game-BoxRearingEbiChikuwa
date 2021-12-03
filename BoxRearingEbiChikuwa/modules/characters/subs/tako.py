import pygame
from modules.character import Character

class CharacterTako(Character):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Character.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [
            ['walk', 'walk'],
        ]
        self.animation_max[0] = 4

        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(self.animation_max[0] + 1):
            self.frames[frame_index].append(image_loader.get('characters/subs/tako/walk' + str(i) + '.svg'))

        self.x_distance = -3

        return

    def hookHitWall(self, kind):
        if kind == 'DanballWall':
            self.x_distance *= -1
        else:
            self.fall = True
            self.y_distance = -75

        return
