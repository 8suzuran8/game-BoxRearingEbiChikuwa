import pygame
from modules.physical import Physical

class ItemsFloatingBlock(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_max = [1]

        self.frames.append(list())
        frame_index = len(self.frames) - 1

        for i in range(self.animation_max[0]):
            self.frames[frame_index].append(pygame.Surface((50, 50)).convert_alpha())

        return
