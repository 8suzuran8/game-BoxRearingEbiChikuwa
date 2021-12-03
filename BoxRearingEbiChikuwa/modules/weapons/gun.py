import pygame
from modules.weapon import Weapon

class WeaponsGun(Weapon):
    size = 10

    def __init__(self, image_loader, status, setting, pos, angle):
        Weapon.__init__(self, image_loader, status, setting, pos, angle)

        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = pos
        self.x_distance = angle[0]
        self.y_distance = angle[1]

        self.fall = True
        self.interval = 200

        self.drawWeapon()

    def drawWeapon(self):
        pygame.draw.circle(
            self.image,
            (80, 0, 0),
            (self.size / 2, self.size / 2),
            self.size / 2
        )

    def hookHit(self):
        self.fall = False
        self.dead = True

    def update(self, backgrounds, characters):
        self.move(-3, backgrounds)
