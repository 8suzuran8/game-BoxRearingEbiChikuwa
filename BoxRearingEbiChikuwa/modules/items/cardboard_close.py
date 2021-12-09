import pygame

class ItemsCardboardClose(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting, info):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((setting['window']['full_width'], setting['window']['full_height'])).convert()
        self.image.fill((185, 234, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (setting['window']['full_width'] / 2, setting['window']['full_height'] / 2)

        self.drawGround(status, setting)

        pygame.display.get_surface().blit(self.image, self.rect)

    def drawGround(self, status, setting):
        # 上
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 下
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
            ],
            0
        )

        # ガムテープ
        pygame.draw.polygon(
            self.image,
            (235, 212, 183),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 - 40),
                (setting['window']['full_width'] - setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] + setting['window']['moving_height'] / 2 + 60),
            ],
            0
        )
