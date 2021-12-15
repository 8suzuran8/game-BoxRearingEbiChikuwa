import pygame
from modules.physical import Physical

class ItemsCardboardClose(Physical):
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
                self.frames[frame_index].append(pygame.Surface((setting['window']['full_width'], setting['window']['full_height'])).convert())

            animation_type_index += 1

        self.need_fall = False

        return

    def __init__(self, image_loader, status, setting, info):
        Physical.__init__(self, image_loader, status, setting, info)

        self.image.fill((185, 234, 255))
        self.drawGround(status, setting)

        return

    def drawGround(self, status, setting):
        # 上
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 下
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
            ],
            0
        )

        # ガムテープ
        pygame.draw.polygon(
            self.image,
            (235, 212, 183),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
            ],
            0
        )

        return
