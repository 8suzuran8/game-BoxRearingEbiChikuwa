import random
import pygame
from modules.item import Item

class ItemsMessage(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 1

        for i in range(self.animation_max):
            self.surface_infos.append(image_loader.get('items/message00.svg'))

        x = 163
        y = 63
        key_count = random.randint(5, 7)
        for i in range(key_count):
            key = random.randint(0, 3)
            if key == 0:
                self.surface_infos[0].blit(image_loader.get('items/arrow_up.svg'), [x, y])
            if key == 1:
                self.surface_infos[0].blit(image_loader.get('items/arrow_right.svg'), [x, y])
            if key == 2:
                self.surface_infos[0].blit(image_loader.get('items/arrow_down.svg'), [x, y])
            if key == 3:
                self.surface_infos[0].blit(image_loader.get('items/arrow_left.svg'), [x, y])

            x += 12

        return
