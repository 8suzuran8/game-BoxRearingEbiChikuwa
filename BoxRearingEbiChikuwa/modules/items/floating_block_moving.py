import pygame
from modules.physical import Physical

class ItemsFloatingBlockMoving(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('items/floating_box_moving.svg'))

            animation_type_index += 1

        self.x_distance += 1
        self.need_fall = False

        return

    def update(self, image_loader, status, setting, foregrounds, info):
        Physical.update(self, image_loader, status, setting, foregrounds, info)

        if info['main_character'].rect.bottom >= self.rect.top and info['main_character'].rect.bottom - 5 <= self.rect.top and info['main_character'].rect.left < self.rect.right and info['main_character'].rect.right > self.rect.left:
            info['main_character'].x_distance = self.x_distance
            info['main_character'].move(image_loader, status, setting, foregrounds, {'animation': False})

        return

    def hookHitWall(self, kind):
        self.x_distance *= -1

        return
