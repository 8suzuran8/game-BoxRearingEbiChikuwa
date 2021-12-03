import pygame
from modules.stages.title import StagesTitlesCursor

class MenuSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/option_menu.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = setting['window']['full_width'] - setting['window']['margin_right'] - self.rect.width
        self.rect.y = setting['window']['full_height'] - self.rect.height - setting['window']['block_size']

        return

class CursorSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/start_cursor.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)

        return

class MarkSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/option_cursor.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)

        return

class StagesTitlesOption(StagesTitlesCursor):
    def createSprites(self, image_loader, status, setting):
        StagesTitlesCursor.createSprites(self, image_loader, status, setting)

        self.sprites.append({
            'sprite': MenuSprite(image_loader, status, setting),
            'key': 'menu',
        })
        self.sprite_indexes['menu'] = len(self.sprites) - 1
        self.sprite_group.add(self.sprites[self.sprite_indexes['menu']]['sprite'])

        self.sprites.append({
            'sprite': CursorSprite(image_loader, status, setting),
            'key': 'cursor',
        })
        self.sprite_indexes['cursor'] = len(self.sprites) - 1
        self.cursor = self.sprites[self.sprite_indexes['cursor']]['sprite']
        self.sprite_group.add(self.sprites[self.sprite_indexes['cursor']]['sprite'])

        for i in range(4):
            self.sprites.append({
                'sprite': MarkSprite(image_loader, status, setting),
                'key': 'mark',
            })
            mark_index = len(self.sprites) - 1
            self.marks.append(self.sprites[mark_index]['sprite'])
            self.sprite_group.add(self.sprites[mark_index]['sprite'])

        return

    def createCursorPosition(self, image_loader, status, setting):
        self.cursor_positions.append(list([self.sprites[self.sprite_indexes['menu']]['sprite'].rect.x + 60, self.sprites[self.sprite_indexes['menu']]['sprite'].rect.y + 36]))
        self.cursor_positions.append(list([self.cursor_positions[0][0], self.cursor_positions[0][1] + 51]))
        self.cursor_positions.append(list([self.cursor_positions[0][0], self.cursor_positions[1][1] + 50]))
        self.cursor_positions.append(list([self.cursor_positions[0][0], self.cursor_positions[2][1] + 50]))

        return

    def setCursorInitialPosition(self, image_loader, status, setting):
        self.cursor.rect.x = self.cursor_positions[0][0]
        self.cursor.rect.y = self.cursor_positions[0][1]

        return

    def createMarkPosition(self, image_loader, status, setting):
        self.mark_positions.append(list())
        self.mark_positions[0].append((self.sprites[self.sprite_indexes['menu']]['sprite'].rect.x + 310, self.sprites[self.sprite_indexes['menu']]['sprite'].rect.y + 33))
        self.mark_positions[0].append((self.mark_positions[0][0][0] + 195, self.mark_positions[0][0][1]))
        self.mark_positions.append(list())
        self.mark_positions[1].append((self.mark_positions[0][0][0], self.mark_positions[0][0][1] + 50))
        self.mark_positions[1].append((self.mark_positions[1][0][0] + 90, self.mark_positions[1][0][1]))
        self.mark_positions[1].append((self.mark_positions[1][1][0] + 105, self.mark_positions[1][1][1]))
        self.mark_positions.append(list())
        self.mark_positions[2].append((self.mark_positions[1][0][0], self.mark_positions[1][0][1] + 50))
        self.mark_positions[2].append((self.mark_positions[2][0][0] + 90, self.mark_positions[2][0][1]))
        self.mark_positions[2].append((self.mark_positions[2][1][0] + 105, self.mark_positions[2][1][1]))
        self.mark_positions.append(list())
        self.mark_positions[3].append((self.mark_positions[2][0][0], self.mark_positions[2][0][1] + 50))
        self.mark_positions[3].append((self.mark_positions[3][0][0] + 195, self.mark_positions[3][0][1]))

        return

    def setMarkInitialPosition(self, image_loader, status, setting):
        if setting['language'] == 'en':
            self.marks[0].rect.x = self.mark_positions[0][0][0]
            self.marks[0].rect.y = self.mark_positions[0][0][1]
        else:
            self.marks[0].rect.x = self.mark_positions[0][1][0]
            self.marks[0].rect.y = self.mark_positions[0][1][1]

        if setting['speed'] == -1:
            self.marks[1].rect.x = self.mark_positions[1][0][0]
            self.marks[1].rect.y = self.mark_positions[1][0][1]
        elif setting['speed'] == 0:
            self.marks[1].rect.x = self.mark_positions[1][1][0]
            self.marks[1].rect.y = self.mark_positions[1][1][1]
        elif setting['speed'] == +1:
            self.marks[1].rect.x = self.mark_positions[1][2][0]
            self.marks[1].rect.y = self.mark_positions[1][2][1]

        if setting['difficult'] == -1:
            self.marks[2].rect.x = self.mark_positions[2][0][0]
            self.marks[2].rect.y = self.mark_positions[2][0][1]
        elif setting['difficult'] == 0:
            self.marks[2].rect.x = self.mark_positions[2][1][0]
            self.marks[2].rect.y = self.mark_positions[2][1][1]
        elif setting['difficult'] == +1:
            self.marks[2].rect.x = self.mark_positions[2][2][0]
            self.marks[2].rect.y = self.mark_positions[2][2][1]

        self.marks[3].rect.x = self.mark_positions[3][0][0]
        self.marks[3].rect.y = self.mark_positions[3][0][1]

        return

    def __init__(self, image_loader, status, setting):
        StagesTitlesCursor.__init__(self, image_loader, status, setting)

        self.createCursorPosition(image_loader, status, setting)
        self.setCursorInitialPosition(image_loader, status, setting)
        self.createMarkPosition(image_loader, status, setting)
        self.setMarkInitialPosition(image_loader, status, setting)

        # 初期設定
        if setting['language'] == 'en':
            self.mark_indexes.append(0)
        else:
            self.mark_indexes.append(1)

        self.mark_indexes.append(setting['speed'] + 1)
        self.mark_indexes.append(setting['difficult'] + 1)
        self.mark_indexes.append(0)

        return

    def eventProcess(self, image_loader, status, setting, event):
        result_event_process = StagesTitlesCursor.eventProcess(self, image_loader, status, setting, event)
        if result_event_process != None:
            return result_event_process

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and len(self.mark_positions) > 0 and len(self.mark_positions[self.cursor_index]) > 0:
                if self.mark_indexes[self.cursor_index] == 0:
                    self.mark_indexes[self.cursor_index] = len(self.mark_positions[self.cursor_index]) - 1
                else:
                    self.mark_indexes[self.cursor_index] -= 1

            elif event.key == pygame.K_RIGHT and len(self.mark_positions) > 0 and len(self.mark_positions[self.cursor_index]) > 0:
                if self.mark_indexes[self.cursor_index] == len(self.mark_positions[self.cursor_index]) - 1:
                    self.mark_indexes[self.cursor_index] = 0
                else:
                    self.mark_indexes[self.cursor_index] += 1

        return None

    def loopProcess(self, image_loader, status, setting):
        StagesTitlesCursor.loopProcess(self, image_loader, status, setting)

        for index in range(len(self.mark_indexes)):
            self.marks[index].rect.x = self.mark_positions[index][self.mark_indexes[index]][0]
            self.marks[index].rect.y = self.mark_positions[index][self.mark_indexes[index]][1]

        return None

    def chk_menu(self, image_loader, status, setting):
        if self.cursor_index == 3:
            if self.mark_indexes[3] == 0:
                # 保存
                if self.mark_indexes[0] == 0:
                    setting['language'] = 'en'
                else:
                    setting['language'] = 'jp'

                setting['speed'] = self.mark_indexes[1] - 1
                setting['difficult'] = self.mark_indexes[2] - 1

                # 言語反映
                image_loader.setting(setting['language'])

                # start画面へ
                return 0
            elif self.mark_indexes[3] == 1:
                # キャンセル
                # start画面へ
                return 0

        return
