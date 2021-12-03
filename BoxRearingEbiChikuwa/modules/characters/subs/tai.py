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
        self.animation_max = [3]

        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(self.animation_max[0] + 1):
            self.frames[frame_index].append(image_loader.get('characters/subs/tai/swim' + str(i) + '.svg'))

        self.x_distance = -3

        return

    def update(self, image_loader, status, setting, foregrounds, info):
        # main character以外で使う?
        self.move(image_loader, status, setting, foregrounds, False)

        return

    def hookHitWall(self, kind):
        self.x_distance *= -1

        return
