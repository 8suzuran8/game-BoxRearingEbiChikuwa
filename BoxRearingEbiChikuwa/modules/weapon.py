import pygame

class Weapon(pygame.sprite.Sprite):
    INTERVAL = 500

    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        self.x_distance = 0
        self.y_distance = 0
        self.last_distance = 0
        self.dead = False
        self.speed_max = 100
        self.timer = 0

        self.fall = False
        self.combo_jump = False

        return

    def __init__(self, image_loader, status, setting, info):
        pygame.sprite.Sprite.__init__(self)

        self.initializeVariable(image_loader, status, setting, info)

        return

    def __del__(self):
        del(self.x_distance)
        del(self.y_distance)
        del(self.last_distance)
        del(self.dead)
        del(self.speed_max)
        del(self.timer)

        del(self.fall)
        del(self.combo_jump)

        return

    def update(self, backgrounds, characters):
        return

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        return

    def jumpMove(self, backgrounds):
        g = 9.8

        self.y_distance += g

        if self.y_distance > self.speed_max:
            self.y_distance = self.speed_max
        if self.x_distance > self.speed_max:
            self.x_distance = self.speed_max

        self.rect.y += self.y_distance / 10
        self.rect.x += self.x_distance / 10

        for background in backgrounds:
            if self.rect.right > background.rect.left and self.rect.left < background.rect.right:
                if self.rect.top < background.rect.bottom and self.rect.bottom > background.rect.top:
                    self.hookHit()

        return

    def hookHit(self):
        return
