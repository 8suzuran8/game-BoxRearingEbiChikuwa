import math
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

class ItemsRhythmCombo(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        # 24個ぴったり必要
        # [True, pygame.K_SPACE] # 黒 and キー
        # [True, False] # 白
        # [False, False] # 透明(描画無し)
        self.target_angle_and_keys = []

        self.animation_index = 0
        self.animation_step = 1
        self.animation_max = 360

        make_target = True
        for i in range(360):

            angle = i
            if angle >= 180:
                angle -= 180

            self.surface_infos.append(pygame.Surface((100, 100)).convert_alpha())
            surface_infos_index = len(self.surface_infos) - 1
            self.draw(360 - angle * 2, make_target, self.surface_infos[surface_infos_index])

            self.surface_infos[surface_infos_index].blit(image_loader.get('items/rhythm_combo/drum.svg'.replace('.svg', str(i).zfill(3) + '.svg')), [0, 0])

            make_target = False

        self.aim = ItemsRhythmComboAim(image_loader, status, setting, path, [info[0] + 85, info[1] + 40])

        return

    def __del__(self):
        super().__del__()

        del(self.target_angle_and_keys)

        return

    def draw(self, rotate, make_target, surface):
        if rotate < 0:
            rotate = 360
        elif rotate > 360:
            rotate = 0

        for i in range(24): # まるの数だけループ
            if self.target_rhythm_and_keys[i][0] == False:
                continue

            angle = math.radians(i * 15 + rotate)
            x = 45 * math.cos(angle) + 50
            y = 45 * math.sin(angle) + 50

            if i == 0:
                color = (139, 69, 19)
            elif self.target_rhythm_and_keys[i][1] == False:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)

            if self.target_rhythm_and_keys[i][1] != False and make_target == True:
                self.target_angle_and_keys.append([(rotate - i * 15), self.target_rhythm_and_keys[i][1]])

            pygame.draw.circle(
                surface,
                color,
                (x, y),
                5,
                0
            )
