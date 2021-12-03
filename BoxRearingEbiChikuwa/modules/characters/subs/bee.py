import pygame
from modules.character import Character

class CharacterBee(Character):
    _KIND_FAT = 1
    _KIND_SMALL = 2

    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Character.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [['fly', 'fly']]
        self.animation_file_max = [3]
        self.animation_index = [0]
        self.animation_step = [1]
        self.animation_max = [3]
        self.animation_interval = [1]
        self.animation_interval_index = [0]
        self.animation_interval_step = [1]

        if len(info) < 3:
            info.append(self._KIND_FAT)

        self.frames.append(list())
        frame_index = len(self.frames) - 1

        for i in range(self.animation_max[0] + 1):
            if info[2] == self._KIND_FAT:
                self.frames[frame_index].append(image_loader.get('characters/subs/bee/fat_fly.svg'.replace('.svg', str(i) + '.svg')))
            else:
                self.frames[frame_index].append(image_loader.get('characters/subs/bee/small_fly.svg'.replace('.svg', str(i) + '.svg')))

        return

    def update(self, image_loader, status, setting, foregrounds, info):
        # 追跡処理
        if self.rect.x > info['main_character_rect'].x + 10:
            self.x_distance = -2
        elif self.rect.x < info['main_character_rect'].x - 10:
            self.x_distance = +2
        else:
            self.x_distance = 0

        if self.rect.y > info['main_character_rect'].y + 10:
            self.y_distance = -1
        elif self.rect.y < info['main_character_rect'].y - 10:
            self.y_distance = +1

        for foreground in foregrounds:
            if self.rect.right > foreground.rect.left and self.rect.left < foreground.rect.right:
                # 着地
                if self.y_distance >= 0 and self.rect.top < foreground.rect.top and self.rect.bottom > foreground.rect.top:
                    self.y_distance = -2

                # 頭打ち
                if self.y_distance <= 0 and foreground.rect.top < self.rect.top and foreground.rect.bottom > self.rect.top:
                    self.y_distance = +2

        self.rect.y += self.y_distance

        self.move(image_loader, status, setting, foregrounds, False)

        return

    def hookHitWall(self, kind):
        pass
        if kind == 'DanballWall':
            self.x_distance *= -1
        else:
            self.x_distance = 0

        return
