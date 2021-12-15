import pygame
from modules.items.item_factory import ItemFactory

class StagesTitle():
    def __new__(cls, image_loader, status, setting):
        self = super().__new__(cls)

        return self

    def initializeVariable(self, image_loader, status, setting):
        self.item_factory = ItemFactory()

        self.background_image = False

        # 上下選択用
        self.cursor = False
        self.cursor_index = 0
        self.cursor_positions = list()

        # 左右選択用
        # 上下メニューの数だけある
        self.marks = list()
        self.mark_indexes = list()
        self.mark_positions = list()

        self.sprite_group = pygame.sprite.RenderUpdates()

        # 全spriteを入れなければならない。
        # self.sprites = [
        #     [
        #         'sprite': sprite,
        #         'key': string, # 空文字OK
        #     ]
        # ]
        self.sprites = list()
        self.sprite_indexes = {}

        return

    def drawTitle(self, image_loader, status, setting):
        title_image = image_loader.get('stages/titles/start_title.svg')
        title_rect = title_image.get_rect()
        title_rect.center = (title_rect.width / 2, title_rect.height / 2)
        title_rect.x = 150
        title_rect.y = 150
        pygame.display.get_surface().blit(title_image, title_rect)

        return

    def createSprites(self, image_loader, status, setting):
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_cardboard_close', [0, 0]),
            'key': 'background',
        })
        self.sprite_indexes['background'] = len(self.sprites) - 1
        self.background_image = self.sprites[self.sprite_indexes['background']]['sprite'].image

        return

    def __init__(self, image_loader, status, setting):
        self.initializeVariable(image_loader, status, setting)
        self.createSprites(image_loader, status, setting)

        pygame.display.get_surface().blit(self.sprites[self.sprite_indexes['background']]['sprite'].image, self.sprites[self.sprite_indexes['background']]['sprite'].rect)
        self.drawTitle(image_loader, status, setting)

        pygame.key.set_repeat(500)

        return

    def __del__(self):
        del(self.item_factory)

        del(self.background_image)

        # 上下選択用
        del(self.cursor)
        del(self.cursor_index)
        del(self.cursor_positions)

        # 左右選択用
        # 上下メニューの数だけある
        del(self.marks)
        del(self.mark_indexes)
        del(self.mark_positions)

        self.sprite_group.empty()
        del(self.sprite_group)

        del(self.sprites)
        del(self.sprite_indexes)

        return

    def eventProcess(self, image_loader, status, setting, event):
        return None

    def loopProcess(self, image_loader, status, setting):
        return None

    # return next stage kind
    def start(self, image_loader, status, setting):
        self.cursor_index = 0

        while True:
            for event in pygame.event.get():
                result_event_process = self.eventProcess(image_loader, status, setting, event)
                if result_event_process != None:
                    return result_event_process

            self.loopProcess(image_loader, status, setting)

            self.sprite_group.clear(pygame.display.get_surface(), self.background_image)
            self.sprite_group.draw(pygame.display.get_surface())
            pygame.display.update()

        return

    # return next stage kind
    def chk_menu(self, image_loader, status, setting):
        pass

class StagesTitlesCursor(StagesTitle):
    def eventProcess(self, image_loader, status, setting, event):
        result_event_process = StagesTitle.eventProcess(self, image_loader, status, setting, event)
        if result_event_process != None:
            return result_event_process

        if self.cursor != False and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.cursor_index == 0:
                    self.cursor_index = len(self.cursor_positions) - 1
                else:
                    self.cursor_index -= 1

                self.mark_index = 0

            elif event.key == pygame.K_DOWN:
                if self.cursor_index == len(self.cursor_positions) - 1:
                    self.cursor_index = 0
                else:
                    self.cursor_index += 1

                self.mark_index = 0

            elif event.key == pygame.K_RETURN:
                return self.chk_menu(image_loader, status, setting)

        return None

    def loopProcess(self, image_loader, status, setting):
        StagesTitle.loopProcess(self, image_loader, status, setting)

        if self.cursor != False:
            self.cursor.rect.x = self.cursor_positions[self.cursor_index][0]
            self.cursor.rect.y = self.cursor_positions[self.cursor_index][1]

        return None
