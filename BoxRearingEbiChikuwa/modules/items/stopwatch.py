import pygame
from modules.physical import Physical

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

class ItemsStopwatch(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [['normal', 'time_frame']]

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(image_loader.get('items/' + animation_type_info[1] + '.svg'))

            animation_type_index += 1

        return

    def changeTime(self, image_loader, status, setting, time):
        pygame.display.get_surface().blit(self.image, self.rect)
        self.stopwatch_time = ItemsStopwatchTime(image_loader, status, setting, time)
