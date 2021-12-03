import pygame
from modules.item import Item

class ItemsTransparentBlock(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 1

        for i in range(self.animation_max):
            self.surface_infos.append(pygame.Surface((setting['window']['moving_width'], setting['window']['block_size'])).convert_alpha())

        return
