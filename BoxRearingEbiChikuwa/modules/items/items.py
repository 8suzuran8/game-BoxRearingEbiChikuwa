import pygame
from modules.item import Item

class ItemsSimple(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 1

        for i in range(self.animation_max):
            self.surface_infos.append(path)

        return
