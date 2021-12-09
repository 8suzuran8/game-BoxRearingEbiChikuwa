import pygame
from modules.physical import Physical

class ItemsBeeHouse(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [['bee_house', 'bee_house']]
        self.animation_max = [4]
        self.animation_file_max = [4]
        self.animation_interval = [200]
        self.animation_interval_index = [0]
        self.animation_count_max = [20]

        self.frames.append(list())
        frame_index = len(self.frames) - 1

        for i in range(self.animation_max[0]):
            self.frames[frame_index].append(image_loader.get('items/bee_house.svg'.replace('.svg', str(i) + '.svg')))

        return
