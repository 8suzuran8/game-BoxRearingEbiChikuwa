import sys
import pygame
from modules.stages.title import StagesTitlesCursor

class MenuSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/start_menu.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = setting['window']['full_width'] - self.rect.width - setting['window']['margin_right']
        self.rect.y = setting['window']['full_height'] - self.rect.height - setting['window']['block_size']

        return

class CursorSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/start_cursor.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)

        return

class StagesTitlesStart(StagesTitlesCursor):
    def drawCopyright(self, image_loader, status, setting):
        copyright_image = image_loader.get('stages/titles/start_copyright.svg')
        copyright_rect = copyright_image.get_rect()
        copyright_rect.center = (copyright_rect.width / 2, copyright_rect.height / 2)
        copyright_rect.x = setting['window']['full_width'] - setting['window']['margin_right'] - copyright_rect.width
        copyright_rect.y = setting['window']['full_height'] - setting['window']['block_size']
        pygame.display.get_surface().blit(copyright_image, copyright_rect)

        return

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
        self.cursor_positions.append(list([self.cursor_positions[0][0], self.cursor_positions[1][1] + 50]))

        return

    def setCursorInitialPosition(self, image_loader, status, setting):
        self.cursor.rect.x = self.cursor_positions[0][0]
        self.cursor.rect.y = self.cursor_positions[0][1]

        return

    def __init__(self, image_loader, status, setting):
        StagesTitlesCursor.__init__(self, image_loader, status, setting)

        self.drawCopyright(image_loader, status, setting)
        self.createCursorPosition(image_loader, status, setting)
        self.setCursorInitialPosition(image_loader, status, setting)

        return

    def chk_menu(self, image_loader, status, setting):
        if self.cursor_index == 0:
            # start
            return status['stage']

        elif self.cursor_index == 1:
            # option
            return -1

        elif self.cursor_index == 2:
            # exit
            pygame.quit()
            sys.exit()
            return
