import random
import math
import pygame
from modules.stages.play import StagesPlay

class StagesPlaysNumberRandom(StagesPlay):
    def __new__(cls, image_loader, status, setting):
        self = super().__new__(cls, image_loader, status, setting)

        return self

    def initializeVariable(self, image_loader, status, setting):
        StagesPlay.initializeVariable(self, image_loader, status, setting)

        current_stage_numbers = int(status['stage'][:2]), int(status['stage'][2:])
        self.next_stage = str(current_stage_numbers[0]).zfill(2) + str(current_stage_numbers[1] + 1).zfill(2)

        # 左上が[0, 0]
        # 中中が[11, 7]
        # 右下が[22, 13]

        self.floating_block_infos = list()
        cell_count_in_block = (5, 3)
        for beside in range(4):
            for vertical in range(4):
                # 1点目は5x3のどこか？
                x = random.randint(-3, 5)
                y = random.randint(-1, 3)

                x = 3
                y = 3

                if x < 0 or y < 0:
                    continue

                floating_block_x = beside * cell_count_in_block[0] + x
                floating_block_y = vertical * cell_count_in_block[1] + y

                # 何個連続させるか？
                x_stick = random.randint(-5, 5)
                y_stick = random.randint(-3, 3)

                if x_stick == 0:
                    self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x, floating_block_y, 'single'))
                else:
                    if x_stick < 0:
                        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x, floating_block_y, 'right'))
                        if x_stick + x < 0:
                            x_stick = x * (-1)
                        for i in range(1, abs(x_stick)):
                            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x - i, floating_block_y, 'center'))
                        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x + x_stick, floating_block_y, 'left'))
                    else:
                        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x, floating_block_y, 'left'))
                        if x_stick + x > cell_count_in_block[0]:
                            x_stick = cell_count_in_block[0] - x
                        for i in range(1, x_stick):
                            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x + i, floating_block_y, 'center'))
                        self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x + x_stick, floating_block_y, 'right'))

                if y_stick != 0:
                    if x_stick < 0:
                        if y_stick + y < 0:
                            y_stick = y * (-1)
                        for i in range(1, abs(y_stick) + 1):
                            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x, floating_block_y - i, 'center'))
                    else:
                        if y_stick + y > cell_count_in_block[1]:
                            y_stick = cell_count_in_block[1] - y
                        for i in range(1, y_stick + 1):
                            self.floating_block_infos.append(self.getMovingXyByPosition(image_loader, status, setting, floating_block_x, floating_block_y + i, 'center'))

        # 下から描画しないとブロックの上部分が不恰好なので並び替える
        self.floating_block_infos = sorted(self.floating_block_infos, reverse=True, key=lambda x: x[1]) 

        # 上に何も乗っていないブロックをまとめる
        nothing_on_floating_blocks = list()
        for floating_block_info1 in self.floating_block_infos:
            something_on_floating_block = False
            for floating_block_info2 in self.floating_block_infos:
                if floating_block_info1 == floating_block_info2:
                    continue

                if floating_block_info1[1] == setting['window']['margin_top']:
                    continue

                if floating_block_info1[0] == floating_block_info2[0] and floating_block_info1[1] - setting['window']['block_size'] == floating_block_info2[1]:
                    something_on_floating_block = True
                    break

            if something_on_floating_block == True:
                continue

            nothing_on_floating_blocks.append(floating_block_info1)


        # 主要アイテムの配置
        self.main_character_initial_position = self.getMovingXyByPosition(image_loader, status, setting, 5, 13)
        position = nothing_on_floating_blocks.pop(random.randint(0, len(nothing_on_floating_blocks) - 1))
        self.time_travel_zone_position = [position[0], position[1] - setting['window']['block_size']]
        position = nothing_on_floating_blocks.pop(random.randint(0, len(nothing_on_floating_blocks) - 1))
        self.npc_position = [position[0], position[1] - setting['window']['block_size']]

        # 敵の配置
        self.enemy_infos = list()

        self.enemy_infos.append(self.getMovingXyByPosition(image_loader, status, setting, 21, 13, self.character_factory._KIND_TAKO))

        for i in range(3):
            position = nothing_on_floating_blocks.pop(random.randint(0, len(nothing_on_floating_blocks) - 1))
            self.enemy_infos.append([position[0], position[1] - setting['window']['block_size'], self.character_factory._KIND_TAI])

        for i in range(3):
            position = nothing_on_floating_blocks.pop(random.randint(0, len(nothing_on_floating_blocks) - 1))
            self.enemy_infos.append([position[0], position[1] - setting['window']['block_size'], self.character_factory._KIND_AMMONITE])

        def enemyOriginalInit1(this): this.rect.y += 0; this.y_distance = 0; this.x_distance = 1; return
        self.enemy_infos[4].append(enemyOriginalInit1)
        self.enemy_infos[5].append(enemyOriginalInit1)
        self.enemy_infos[6].append(enemyOriginalInit1)

        return

    def __del__(self):
        super().__del__()

        del(self.next_stage)
        del(self.main_character_initial_position)
        del(self.npc_position)
        del(self.time_travel_zone_position)
        del(self.floating_block_infos)
        del(self.enemy_infos)

        return
