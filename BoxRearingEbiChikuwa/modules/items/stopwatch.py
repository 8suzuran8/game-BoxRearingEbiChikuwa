import pygame
from modules.item import Item

class ItemsStopwatchTime(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting, time):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((160, 190), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = setting['window']['margin_left'] + setting['window']['moving_width'] / 2 - 28
        self.rect.y = 0

        self.drawTime(image_loader, status, setting, time)

    def drawTime(self, image_loader, status, setting, time):

        if int(time) <= 9:
            time = '0' + str(time)
        else:
            time = str(time)

        numbers = list(time)

        positions = [
            [9, 25],
            [29, 25]
        ]

        i = 0
        for number in numbers:
            image = image_loader.get('items/number' + number + '.svg')
            rect = image.get_rect()
            rect.x = positions[i][0]
            rect.y = positions[i][1]
            self.image.blit(image, rect)
            i += 1

        pygame.display.get_surface().blit(self.image, self.rect)

class ItemsStopwatch(Item):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls, image_loader, status, setting, path, info)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        Item.initializeVariable(self, image_loader, status, setting, path, info)

        self.animation_max = 1

        for i in range(self.animation_max):
            self.surface_infos.append('items/time_frame.svg')

        return

    def changeTime(self, image_loader, status, setting, time):
        pygame.display.get_surface().blit(self.image, self.rect)
        self.stopwatch_time = ItemsStopwatchTime(image_loader, status, setting, time)
