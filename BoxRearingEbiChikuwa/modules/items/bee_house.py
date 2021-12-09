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
        self.animation_interval_max = [100]
        self.animation_interval_count_max = [20]




        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('items/' + animation_type_info[1] + str(i).zfill(1) + '.svg'))

            animation_type_index += 1

        return
