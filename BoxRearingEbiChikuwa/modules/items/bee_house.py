import pygame
from modules.item import Item

class ItemsBeeHouse(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 4
        self.animation_interval = 200
        self.animation_interval_index = 0
        self.animation_count_max = 20

        for i in range(self.animation_max):
            self.surface_infos.append('items/bee_house.svg'.replace('.svg', str(i) + '.svg'))

        return
