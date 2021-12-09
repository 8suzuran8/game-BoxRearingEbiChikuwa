import pygame
from modules.weapon import Weapon

class WeaponsGun(Weapon):
    INTERVAL = 200

    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Weapon.initializeVariable(self, image_loader, status, setting, info)

        self.size = 10

        return

    def __init__(self, image_loader, status, setting, info):
        Weapon.__init__(self, image_loader, status, setting, info)

        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = info[0]
        self.x_distance = info[1][0]
        self.y_distance = info[1][1]

        self.fall = True

        self.drawWeapon()

        return

    def __del__(self):
        Weapon.__del__(self)

        del(self.size)

        return

    def drawWeapon(self):
        pygame.draw.circle(
            self.image,
            (80, 0, 0),
            (self.size / 2, self.size / 2),
            self.size / 2
        )

        return

    def hookHit(self):
        self.fall = False
        self.dead = True

        return

    def update(self, backgrounds, characters):
        self.move(-3, backgrounds)

        return
