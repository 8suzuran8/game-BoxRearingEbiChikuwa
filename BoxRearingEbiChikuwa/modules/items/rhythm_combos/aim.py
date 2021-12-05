import pygame
from modules.item import Item

class ItemsRhythmComboAim(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.size = 20
        self.color_type = 0
        self.animation_max = 2

        for i in range(self.animation_max):
            self.surface_infos.append(pygame.Surface((self.size, self.size)).convert_alpha())

        self.draw((0, 0, 0), self.surface_infos[0])
        self.draw((255, 165, 0), self.surface_infos[1])

        return

    def __del__(self):
        super().__del__()

        del(self.size)
        del(self.color_type)

        return

    def draw(self, color, surface):
        # 円
        pygame.draw.circle(
            surface,
            color,
            (self.size / 2, self.size / 2),
            self.size / 2,
            2
        )

        # 十字
        pygame.draw.line(
            surface,
            color,
            (self.size / 2 - 1, 0),
            (self.size / 2 - 1, self.size / 2 - 2),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (self.size / 2 - 1, self.size / 2 + 2),
            (self.size / 2 - 1, self.size),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (0, self.size / 2 - 1),
            (self.size / 2 - 2, self.size / 2 - 1),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (self.size / 2 + 2, self.size / 2 - 1),
            (self.size, self.size / 2 - 1),
            2
        )

        return

    def callAnimation(self, drum_aim_action):
        if self.color_type == 0 and drum_aim_action == True:
            self.color_type = 1
            self.originAnimation()
        elif self.color_type == 1:
            self.color_type = 0
            self.originAnimation()

        return

    def originAnimation(self):
        self.animation_index += 1
        if self.animation_index < 0:
            self.animation_index = self.animation_max - 1
        elif self.animation_index >= self.animation_max:
            self.animation_index = 0

        self.image = self.frames[self.animation_index]

        return

    def animation(self):
        return
