import pygame
from modules.item import Item

class ItemsRhythmComboDrum(Item):
    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 360
        self.animation_step = 2

        for i in range(self.animation_max):
            self.surface_infos.append('items/rhythm_combo/drum.svg'.replace('.svg', str(i).zfill(3) + '.svg'))

        return
