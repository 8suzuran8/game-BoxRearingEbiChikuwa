import random
import pygame
from modules.physical import Physical

class ItemsMessage(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [['normal', 'message']]

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('items/' + animation_type_info[1] + str(i).zfill(2) + '.svg'))

            animation_type_index += 1

        x = 135
        y = 63
        self.keys = list()
        key_count = random.randint(5, 7)
        for i in range(key_count):
            key = random.randint(0, 3)
            if key == 0:
                self.keys.append(pygame.K_UP)
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_up.svg'), [x, y])
            if key == 1:
                self.keys.append(pygame.K_RIGHT)
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_right.svg'), [x, y])
            if key == 2:
                self.keys.append(pygame.K_DOWN)
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_down.svg'), [x, y])
            if key == 3:
                self.keys.append(pygame.K_LEFT)
                self.frames[frame_index][0].blit(image_loader.get('items/arrow_left.svg'), [x, y])

            x += 12

        return

    def __del__(self):
        super().__del__()

        del(self.keys)

        return
