import pygame

class Weapon(pygame.sprite.Sprite):
    x_distance = 0
    y_distance = 0
    last_distance = 0
    dead = False
    speed_max = 100
    interval = 500

    fall = False
    combo_jump = False

    def __init__(self, image_loader, status, setting, pos, angle):
        pygame.sprite.Sprite.__init__(self)

    def update(self, backgrounds, characters):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

    def hookHit(self):
        pass
