import pygame

class Item(pygame.sprite.Sprite):
    def __new__(cls, image_loader, status, setting, path, info):
        self = super().__new__(cls)

        return self

    def initializeVariable(self, image_loader, status, setting, path, info):
        self.surface_infos = list()
        self.frames = list()

        self.animation_index = 0
        self.animation_step = 1
        self.animation_max = 4

        self.animation_interval = 0
        self.animation_interval_index = 0
        self.animation_count_max = 0
        self.animation_count = 0

        return

    def __init__(self, image_loader, status, setting, path, info):
        pygame.sprite.Sprite.__init__(self)

        self.initializeVariable(image_loader, status, setting, path, info)

        for i in range(self.animation_max):
            if type(self.surface_infos).__name__ == 'dict' and i not in self.surface_infos.keys():
                continue

            if type(self.surface_infos[i]).__name__ == 'str':
                self.frames.append(image_loader.get(self.surface_infos[i]))
            else:
                self.frames.append(self.surface_infos[i])

        self.image = self.frames[0]

        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.w / 2, self.rect.h / 2)
        self.rect.x = info[0]
        self.rect.y = info[1]

        return

    def __del__(self):
        del(self.surface_infos)
        del(self.frames)

        del(self.animation_index)
        del(self.animation_step)
        del(self.animation_max)

        del(self.animation_interval)
        del(self.animation_interval_index)
        del(self.animation_count_max)
        del(self.animation_count)

        return
    
    def animation(self):
        self.animation_interval_index += 1

        if self.animation_interval_index < self.animation_interval:
            return

        self.animation_count += 1
        if self.animation_count_max > 0 and self.animation_count >= self.animation_count_max:
            self.animation_interval_index = 0
            self.animation_count = 0
            return

        self.animation_index += self.animation_step
        if self.animation_index <= 0:
            self.animation_index = self.animation_max - 1
        elif self.animation_index >= self.animation_max:
            self.animation_index = 0

        self.image = self.frames[self.animation_index]

        return
