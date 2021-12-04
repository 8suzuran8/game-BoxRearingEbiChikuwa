import numpy as np
import pyaudio
import pygame
from modules.character import Character
from modules.weapons.factory import WeaponsFactory

class CharacterEbichikuwa(Character):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Character.initializeVariable(self, image_loader, status, setting, info)

        self.junp_sound = False

        # 落ちないジャンプ。コンボでしか使わない
        self.combo_jump = False
        self.combo_index = -1
        self.combo = False
        self.combo_start = 0
        self.combo_count = 0


        self.animation_type_infos = [
            ['move', 'walk'],
            ['squat', 'squat'],
            ['crush', 'crush'],
        ]

        self.animation_file_max = [
            16,
            15,
            11
        ]

        self.animation_index = [
            0,
            0,
            0,
        ]

        self.animation_step = [
            1,
            1,
            1,
        ]

        self.animation_max = [
            32,
            15,
            11,
        ]

        self.animation_interval = [
            1,
            5,
            50,
        ]

        self.animation_interval_index = [
            1,
            1,
            1,
        ]

        self.animation_interval_step = [
            1,
            1,
            1,
        ]

        # 歩く
        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(17):
            self.frames[frame_index].append(image_loader.get('characters/main/walk' + str(i).zfill(2) + '.svg'))
        # 18は16の左右反転
        # 19は15の左右反転
        # 20は14の左右反転
        # ・・・

        # しゃがむ
        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(16):
            self.frames[frame_index].append(image_loader.get('characters/main/squat' + str(i).zfill(2) + '.svg'))

        # 潰れる
        self.frames.append(list())
        frame_index = len(self.frames) - 1
        for i in range(12):
            self.frames[frame_index].append(image_loader.get('characters/main/crush' + str(i).zfill(2) + '.svg'))

        return

    def __init__(self, image_loader, status, setting, info):
        Character.__init__(self, image_loader, status, setting, info)

        self.jump_sound = self.makeJumpSound()

        return

    def __del__(self):
        Character.__del__(self)

        del(self.junp_sound)

        del(self.combo_jump)
        del(self.combo_index)
        del(self.combo)
        del(self.combo_start)
        del(self.combo_count)

        return

    def update(self, image_loader, status, setting, foregrounds, info):
        pass

    def hookHitWall(self, kind):
        self.x_distance = 0

        return

    def jumpStart(self, image_loader, status, setting, key):
        if self.combo_index > -1:
            return

        if key != pygame.K_SPACE:
            return

        if self.animation_index[1] > 8:
            self.animation_index[1] = 8

        temp_y_distance = self.animation_index[1] * -15

        Character.jumpStart(self, image_loader, status, setting, key)

        # 飛べ
        self.y_distance = temp_y_distance

        return

    def makeJumpSound(self):
        RATE = 44100
        freq = 440.000
        sound_second = 1/3
        wavelength = RATE / freq
        linelength = wavelength / 4
        datalength = 1 / linelength
        wave = np.zeros(int(RATE * sound_second))
        plus = True
        for i in range(int(RATE * sound_second)):
            if i == 0:
                wave[0] = datalength
            else:
                if plus:
                    wave[i] = wave[i - 1] + datalength

                    if wave[i] >= 1:
                        plus = not plus
                else:
                    wave[i] = wave[i - 1] - datalength

                    if wave[i] <= -1:
                        plus = not plus

            if i % 1000 == 0:
                datalength += 0.01

        p = pyaudio.PyAudio()
        stream = p.open(
            format = pyaudio.paFloat32,
            channels = 1,
            rate = RATE,
            frames_per_buffer = 1024,
            output = True
        )

        return pygame.mixer.Sound(wave.astype(np.float32))

    def addAnimation(self, step, kind = 0):
        if kind == 1:
            # しゃがむアニメーションの限界
            if self.animation_index[1] >= self.animation_max[1]:
                self.crush = True
                return True

        if kind == 2:
            # クラッシュアニメーションの終了
            if self.animation_index[kind] >= self.animation_max[kind]:
                return -2

        if kind == 0:
            # 左右無し　且つ　アニメーションの半分を左右反転で対応
            if self.animation_index[kind] > self.animation_file_max[kind]:
                self.image = pygame.transform.flip(self.frames[kind][self.animation_file_max[kind] - (self.animation_index[kind] - self.animation_file_max[kind])], True, False)
            else:
                self.image = self.frames[kind][self.animation_index[kind]]

            return True

        return None

    def moveStep(self):
        if self.y_distance != 0:
            self.x_distance *= 2

        return

    def getHolePositionAndAngle(self):
        # walk animationの数だけある
        if self.animation_index[0] == 0:
            return [(self.rect.x + 30, self.rect.y), (0, -200)] # 真上
        elif self.animation_index[0] == 1:
            return [(self.rect.x + 37, self.rect.y), (40, -160)]
        elif self.animation_index[0] == 2:
            return [(self.rect.x + 43, self.rect.y + 5), (80, -120)]
        elif self.animation_index[0] == 3:
            return [(self.rect.x + 49, self.rect.y + 9), (120, -80)]
        elif self.animation_index[0] == 4:
            return [(self.rect.x + 53, self.rect.y + 16), (160, -40)]
        elif self.animation_index[0] == 5:
            return [(self.rect.x + 58, self.rect.y + 25), (200, 0)] # 真横
        elif self.animation_index[0] == 6:
            return [(self.rect.x + 60, self.rect.y + 35), (180, 20)]
        elif self.animation_index[0] == 7:
            return [(self.rect.x + 60, self.rect.y + 47), (160, 40)]
        elif self.animation_index[0] == 8:
            return [(self.rect.x + 58, self.rect.y + 57), (140, 60)]
        elif self.animation_index[0] == 9:
            return [(self.rect.x + 56, self.rect.y + 59), (120, 80)]
        elif self.animation_index[0] == 10:
            return [(self.rect.x + 53, self.rect.y + 59), (100, 100)]
        elif self.animation_index[0] == 11:
            return [(self.rect.x + 51, self.rect.y + 59), (80, 120)]
        elif self.animation_index[0] == 12:
            return [(self.rect.x + 48, self.rect.y + 59), (60, 140)]
        elif self.animation_index[0] == 13:
            return [(self.rect.x + 44, self.rect.y + 61), (40, 160)]
        elif self.animation_index[0] == 14:
            return [(self.rect.x + 41, self.rect.y + 61), (20, 180)]
        elif self.animation_index[0] == 15:
            return [(self.rect.x + 36, self.rect.y + 61), (20, 180)]
        elif self.animation_index[0] == 16:
            return [(self.rect.x + 30, self.rect.y + 63), (0, 200)] # 真下
        elif self.animation_index[0] == 17:
            return [(self.rect.x + 24, self.rect.y + 61), (-20, 180)]
        elif self.animation_index[0] == 18:
            return [(self.rect.x + 19, self.rect.y + 61), (-20, 180)]
        elif self.animation_index[0] == 19:
            return [(self.rect.x + 16, self.rect.y + 61), (-40, 160)]
        elif self.animation_index[0] == 20:
            return [(self.rect.x + 12, self.rect.y + 59), (-60, 140)]
        elif self.animation_index[0] == 21:
            return [(self.rect.x + 15, self.rect.y + 59), (-80, 120)]
        elif self.animation_index[0] == 22:
            return [(self.rect.x + 13, self.rect.y + 59), (-100, 100)]
        elif self.animation_index[0] == 23:
            return [(self.rect.x + 10, self.rect.y + 59), (-120, 80)]
        elif self.animation_index[0] == 24:
            return [(self.rect.x + 8,  self.rect.y + 57), (-140, 60)]
        elif self.animation_index[0] == 25:
            return [(self.rect.x + 6,  self.rect.y + 47), (-160, 40)]
        elif self.animation_index[0] == 26:
            return [(self.rect.x + 6,  self.rect.y + 35), (-180, 20)]
        elif self.animation_index[0] == 27:
            return [(self.rect.x + 8,  self.rect.y + 25), (-100, 0)] # 真横
        elif self.animation_index[0] == 28:
            return [(self.rect.x + 13, self.rect.y + 16), (-160, -40)]
        elif self.animation_index[0] == 29:
            return [(self.rect.x + 17, self.rect.y + 9), (-120, -80)]
        elif self.animation_index[0] == 30:
            return [(self.rect.x + 23, self.rect.y + 5), (-80, -120)]
        elif self.animation_index[0] == 31:
            return [(self.rect.x + 29, self.rect.y), (-40, -160)]
        else:
            return [(self.rect.x + 29, self.rect.y), (0, -200)]

        return

    def attack(self, image_loader, status, setting, combo = False):
        if self.combo_index == -1 and self.weapons_factory.canCreate(WeaponsFactory._KIND_GUN) == False:
            return

        hole_position_and_angle = self.getHolePositionAndAngle()

        self.weapons.add(self.weapons_factory.create(image_loader, status, setting, WeaponsFactory._KIND_GUN, hole_position_and_angle[0], hole_position_and_angle[1]))
        self.weapons.sprites()[len(self.weapons) - 1].number = pygame.time.get_ticks()

        return

    def comboInput(self, key, drum_aim, drum_rhythm):
        if self.animation_index[1] > 0:
            return

        margin = 20

        for combo_index in [self.combo_index + 1, self.combo_index]:
            if combo_index < 0 or combo_index > len(drum_rhythm.target_angle_and_keys) - 1:
                continue

            # 早い
            angle = 380 - (drum_rhythm.animation_index * 2)

            if angle - margin < 0:
                if drum_rhythm.target_angle_and_keys[combo_index][0] < 360 + (angle - margin) and drum_rhythm.target_angle_and_keys[combo_index][0] > angle + margin:
                    continue
            elif angle + margin > 360:
                if drum_rhythm.target_angle_and_keys[combo_index][0] > (angle + margin) - 360 and drum_rhythm.target_angle_and_keys[combo_index][0] < (angle - margin):
                    continue
            else:
                if drum_rhythm.target_angle_and_keys[combo_index][0] < angle - margin or drum_rhythm.target_angle_and_keys[combo_index][0] > angle + margin:
                    continue

            # キーが違う
            if drum_rhythm.target_angle_and_keys[combo_index][1] != key:
                continue

            # 処理済みコンボ
            if self.combo_index == combo_index:
                return True

            # 未処理コンボ
            if pygame.key.name(key) == 'space':
                self.combo_jump = True
                self.y_distance = -100

            self.combo_index = combo_index
            return combo_index

        self.combo_index = -1

        return False

    def comboAction(self, image_loader, status, setting):
        if self.combo_index > 3:
            self.animation_interval_index[0] += 1
            self.animation(+1, 0)
        if self.combo_index > 7:
            self.attack(image_loader, status, setting)
            if self.combo_start == 0:
                self.combo_start = self.animation_index[0]

        if self.combo_start != 0 and self.combo_start == self.animation_index[0]:
            self.combo_count += 1

        if self.combo_count > 1:
            self.combo_count = 0
            self.combo_index = -1
            self.fall = True

        return
