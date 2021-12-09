import random
import pygame
from modules.physical import Physical

class ItemsMessage(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_max = [1]

        self.frames.append(list())
        frame_index = len(self.frames) - 1

        for i in range(self.animation_max[0]):
            self.frames[frame_index].append(image_loader.get('items/message00.svg'))

        x = 163
        y = 63
        key_count = random.randint(5, 7)
        for i in range(key_count):
            key = random.randint(0, 3)
            if key == 0:
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_up.svg'), [x, y])
            if key == 1:
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_right.svg'), [x, y])
            if key == 2:
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_down.svg'), [x, y])
            if key == 3:
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_left.svg'), [x, y])

            x += 12

        return
