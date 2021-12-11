import math
import pygame
from modules.physical import Physical

class ItemsRhythmCombo(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        # 24個ぴったり必要
        # [True, pygame.K_SPACE] # 黒 and キー
        # [True, False] # 白
        # [False, False] # 透明(描画無し)
        self.target_angle_and_keys = []
        self.clear_max = 0

        self.animation_index = [0]
        self.animation_step = [1]
        self.animation_max = [360]
        self.animation_file_max = [360]

        self.frames.append(list())
        frame_index = len(self.frames) - 1

        make_target = True
        for i in range(360):

            angle = i
            if angle >= 180:
                angle -= 180

            self.frames[frame_index].append(pygame.Surface((105, 100)).convert_alpha())
            surface_infos_index = len(self.frames[frame_index]) - 1
            self.drawRhythm(360 - angle * 2, make_target, self.frames[frame_index][surface_infos_index])

            self.drawAim(self.frames[frame_index][surface_infos_index], [105, 60])
            self.frames[frame_index][surface_infos_index].blit(image_loader.get('items/rhythm_combo/drum.svg'.replace('.svg', str(i).zfill(3) + '.svg')), [0, 0])

            make_target = False

        self.clear_max = -1
        for target_rhythm_and_key in self.target_rhythm_and_keys:
            if target_rhythm_and_key[0] == True and target_rhythm_and_key[1] != False:
                self.clear_max += 1

        return

    def __del__(self):
        super().__del__()

        del(self.target_angle_and_keys)
        del(self.clear_max)

        return

    def drawRhythm(self, rotate, make_target, surface):
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

    def drawAim(self, surface, position):
        size = 20
        color = (0, 0, 0)

        # 円
        pygame.draw.circle(
            surface,
            color,
            (position[0] - size / 2, position[1] - size / 2),
            size / 2,
            2
        )

        # 十字
        pygame.draw.line(
            surface,
            color,
            (position[0] - size / 2 - 1, position[1] - 0),
            (position[0] - size / 2 - 1, position[1] - size / 2 - 2),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (position[0] - size / 2 - 1, position[1] - size / 2 + 2),
            (position[0] - size / 2 - 1, position[1] - size),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (position[0] - 0, position[1] - size / 2 - 1),
            (position[0] - size / 2 - 2, position[1] - size / 2 - 1),
            2
        )

        pygame.draw.line(
            surface,
            color,
            (position[0] - size / 2 + 2, position[1] - size / 2 - 1),
            (position[0] - size, position[1] - size / 2 - 1),
            2
        )

        return
    
