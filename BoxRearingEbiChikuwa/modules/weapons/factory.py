import pygame
from modules.common.singleton import Singleton
from modules.weapons.gun import WeaponsGun

class WeaponsFactory(Singleton):
    _KIND_GUN = 1

    interval_start = pygame.time.get_ticks()

    def canCreate(self, kind):
        if kind == WeaponsFactory._KIND_GUN:
            if self.interval_start + WeaponsGun.interval < pygame.time.get_ticks():
                return True

        return False

    def create(self, image_loader, status, setting, kind, pos, angle):
        weapon = False
        if kind == WeaponsFactory._KIND_GUN:
            weapon = WeaponsGun(image_loader, status, setting, pos, angle)

        if weapon != False:
            self.interval_start = pygame.time.get_ticks()

        return weapon
