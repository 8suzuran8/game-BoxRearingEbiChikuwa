import pygame
from modules.stages.title import StagesTitlesCursor

class MenuSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/badend_menu.svg')
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

class StagesTitlesBadEnd(StagesTitlesCursor):
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

        return

    def createCursorPosition(self, image_loader, status, setting):
        self.cursor_positions.append(list([self.sprites[self.sprite_indexes['menu']]['sprite'].rect.x + 60, self.sprites[self.sprite_indexes['menu']]['sprite'].rect.y + 36]))
        self.cursor_positions.append(list([self.cursor_positions[0][0], self.cursor_positions[0][1] + 51]))

        return

    def setCursorInitialPosition(self, image_loader, status, setting):
        self.cursor.rect.x = self.cursor_positions[0][0]
        self.cursor.rect.y = self.cursor_positions[0][1]

        return

    def __init__(self, image_loader, status, setting):
        StagesTitlesCursor.__init__(self, image_loader, status, setting)

        self.createCursorPosition(image_loader, status, setting)
        self.setCursorInitialPosition(image_loader, status, setting)

    def chk_menu(self, image_loader, status, setting):
        if self.cursor_index == 0:
            # CONTINUE
            status['score'] -= 1000
            if status['score'] < 0:
                status['score'] = 0

            return status['stage']
            pass
        else:
            # END
            return 0
            pass
