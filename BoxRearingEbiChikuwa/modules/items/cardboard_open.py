import pygame

class ItemsCardboardOpen(pygame.sprite.Sprite):
    def __init__(self, image_loader, status, setting, path, info):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((setting['window']['full_width'], setting['window']['full_height'])).convert()
        self.image.fill((185, 234, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (setting['window']['full_width'] / 2, setting['window']['full_height'] / 2)

        self.drawGround(status, setting)

        for i in range(3):
            x = i * 400 + 250
            y = setting['window']['margin_top'] + setting['window']['moving_height'] - setting['window']['margin_bottom'] / 2 - 100
            self.image.blit(image_loader.get('items/mountain01.svg'), [x, y])

        for i in range(4):
            x = i * 300 + 190
            y = setting['window']['margin_top'] / 3 * 4
            if i % 2 == 1:
                y += setting['window']['block_size']
            self.image.blit(image_loader.get('items/cloud01.svg'), [x, y])

    def drawGround(self, status, setting):
        # 奥上下
        pygame.draw.rect(
            self.image,
            (156, 122, 78),
            pygame.Rect(
                setting['window']['full_width'] / 2 - 10,
                setting['window']['margin_top'] / 3 * 4,
                20,
                setting['window']['moving_height'] - setting['window']['margin_bottom'] * 2
            ),
            0
        )

        # 内左
        pygame.draw.polygon(
            self.image,
            (189, 157, 115),
            [
                (setting['window']['margin_left'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['margin_left'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 内右
        pygame.draw.polygon(
            self.image,
            (189, 157, 115),
            [
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 内上
        pygame.draw.polygon(
            self.image,
            (189, 157, 115),
            [
                (setting['window']['margin_left'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 内下
        pygame.draw.polygon(
            self.image,
            (207, 169, 120),
            [
                (setting['window']['margin_left'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
            ],
            0
        )

        # 左上ライン
        pygame.draw.line(
            self.image,
            (156, 122, 78),
            (setting['window']['margin_left'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
            (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            5
        )

        # 右上ライン
        pygame.draw.line(
            self.image,
            (156, 122, 78),
            (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
            (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            5
        )

        # 左下ライン
        pygame.draw.line(
            self.image,
            (156, 122, 78),
            (setting['window']['margin_left'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
            5
        )

        # 右下ライン
        pygame.draw.line(
            self.image,
            (156, 122, 78),
            (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['full_height']),
            5
        )

        # 外上
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, 0),
                (setting['window']['margin_left'] / 3 * 4, 0),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
            ],
            0
        )

        # 外左
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['margin_left'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['margin_left'] / 3 * 2, setting['window']['full_height']),
                (0, setting['window']['full_height']),
                (0, setting['window']['margin_top']),
            ],
            0
        )

        # 外右
        pygame.draw.polygon(
            self.image,
            (222, 184, 135),
            [
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['margin_top'] / 3 * 2),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 2, setting['window']['full_height']),
                (setting['window']['full_width'], setting['window']['full_height']),
                (setting['window']['full_width'], setting['window']['margin_top']),
            ],
            0
        )

        # 奥の隙間
        pygame.draw.rect(
            self.image,
            (185, 234, 255),
            pygame.Rect(
                setting['window']['full_width'] / 2 - 25,
                setting['window']['full_height'] / 2 + 50,
                50,
                20
            ),
            0
        )

        # 奥左
        pygame.draw.polygon(
            self.image,
            (189, 157, 115),
            [
                (setting['window']['margin_left'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] / 2 - 10, setting['window']['margin_top'] / 3 * 4 - 10),
                (setting['window']['full_width'] / 2 - 10, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2 + 10),
                (setting['window']['margin_left'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            ],
            0
        )

        # 奥左ライン
        pygame.draw.polygon(
            self.image,
            (156, 122, 78),
            [
                (setting['window']['margin_left'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] / 2 - 10, setting['window']['margin_top'] / 3 * 4 - 10),
                (setting['window']['full_width'] / 2 - 10, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2 + 10),
                (setting['window']['margin_left'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            ],
            3
        )

        # 奥右
        pygame.draw.polygon(
            self.image,
            (189, 157, 115),
            [
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] / 2 + 10, setting['window']['margin_top'] / 3 * 4 - 10),
                (setting['window']['full_width'] / 2 + 10, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2 + 10),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            ],
            0
        )

        # 奥右ライン
        pygame.draw.polygon(
            self.image,
            (156, 122, 78),
            [
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['margin_top'] / 3 * 4),
                (setting['window']['full_width'] / 2 + 10, setting['window']['margin_top'] / 3 * 4 - 10),
                (setting['window']['full_width'] / 2 + 10, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2 + 10),
                (setting['window']['full_width'] - setting['window']['margin_right'] / 3 * 4, setting['window']['full_height'] - setting['window']['margin_bottom'] * 2),
            ],
            3
        )

