import pygame
from modules.stages.title import StagesTitle

class MenuSprite(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting):
        pygame.sprite.Sprite.__init__(self)

        self.image = image_loader.get('stages/titles/goodend_menu.svg')
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = setting['window']['full_width'] - setting['window']['margin_right'] - self.rect.width
        self.rect.y = setting['window']['full_height'] - self.rect.height - setting['window']['block_size']

        return

class StagesTitlesGoodEnd(StagesTitle):
    def createSprites(self, image_loader, status, setting):
        StagesTitle.createSprites(self, image_loader, status, setting)

        self.sprites.append({
            'sprite': MenuSprite(image_loader, status, setting),
            'key': 'menu',
        })
        self.sprite_indexes['menu'] = len(self.sprites) - 1
        self.sprite_group.add(self.sprites[self.sprite_indexes['menu']]['sprite'])

    def __init__(self, image_loader, status, setting):
        StagesTitle.__init__(self, image_loader, status, setting)

    def eventProcess(self, image_loader, status, setting, event):
        result_event_process = StagesTitle.eventProcess(self, image_loader, status, setting, event)
        if result_event_process != None:
            return result_event_process

        if event.type == pygame.KEYDOWN:
            return 0

        return None

    def chk_menu(self, image_loader, status, setting):
        return 0
