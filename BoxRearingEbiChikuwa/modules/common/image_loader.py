import pygame
from modules.common.singleton import Singleton

class ImageLoader(Singleton):
    images = {}

    def __init__(self):
        pass

    # language = 'jp' or 'en'
    def setting(self, language):
        self.base_path = 'BoxRearingEbiChikuwa/images/'

        self.images['stages/titles/start_title.svg'] = pygame.image.load(self.base_path + 'stages/titles/start_title_' + language + '.svg').convert_alpha()
        self.images['stages/titles/start_copyright.svg'] = pygame.image.load(self.base_path + 'stages/titles/start_copyright_' + language + '.svg').convert_alpha()
        self.images['stages/titles/start_menu.svg'] = pygame.image.load(self.base_path + 'stages/titles/start_menu_' + language + '.svg').convert_alpha()
        self.images['stages/titles/start_cursor.svg'] = pygame.image.load(self.base_path + 'stages/titles/start_cursor.svg').convert_alpha()

        self.images['stages/titles/option_menu.svg'] = pygame.image.load(self.base_path + 'stages/titles/option_menu_' + language + '.svg').convert_alpha()
        self.images['stages/titles/option_manual.svg'] = pygame.image.load(self.base_path + 'stages/titles/option_manual_' + language + '.svg').convert_alpha()
        self.images['stages/titles/option_cursor.svg'] = pygame.image.load(self.base_path + 'stages/titles/option_cursor.svg').convert_alpha()

        self.images['stages/titles/badend_title.svg'] = pygame.image.load(self.base_path + 'stages/titles/badend_title_' + language + '.svg').convert_alpha()
        self.images['stages/titles/badend_menu.svg'] = pygame.image.load(self.base_path + 'stages/titles/badend_menu_' + language + '.svg').convert_alpha()
        self.images['stages/titles/badend_cursor.svg'] = pygame.image.load(self.base_path + 'stages/titles/badend_cursor.svg').convert_alpha()

        self.images['stages/titles/goodend_title.svg'] = pygame.image.load(self.base_path + 'stages/titles/goodend_title_' + language + '.svg').convert_alpha()
        self.images['stages/titles/goodend_menu.svg'] = pygame.image.load(self.base_path + 'stages/titles/goodend_menu_' + language + '.svg').convert_alpha()

        self.images['items/mountain01.svg'] = pygame.image.load(self.base_path + 'items/mountain01.svg')
        self.images['items/cloud01.svg'] = pygame.image.load(self.base_path + 'items/cloud01.svg')

        for i in range(4):
            self.images['items/bee_house' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'items/bee_house' + str(i) + '.svg')

        self.images['items/time_frame.svg'] = pygame.image.load(self.base_path + 'items/time_frame.svg')
        for i in range(10):
            self.images['items/number' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'items/number' + str(i) + '.svg')

        self.images['items/floating_box_single.svg'] = pygame.image.load(self.base_path + 'items/floating_box_single.svg')
        self.images['items/floating_box_left.svg'] = pygame.image.load(self.base_path + 'items/floating_box_left.svg')
        self.images['items/floating_box_center.svg'] = pygame.image.load(self.base_path + 'items/floating_box_center.svg')
        self.images['items/floating_box_right.svg'] = pygame.image.load(self.base_path + 'items/floating_box_right.svg')
        self.images['items/floating_box_moving.svg'] = pygame.image.load(self.base_path + 'items/floating_box_moving.svg')

        self.images['items/smoke.svg'] = pygame.image.load(self.base_path + 'items/smoke.svg')

        for i in range(17):
            self.images['characters/main/walk' + str(i).zfill(2) + '.svg'] = pygame.image.load(self.base_path + 'characters/main/walk' + str(i).zfill(2) + '.svg').convert_alpha()

        for i in range(16):
            self.images['characters/main/squat' + str(i).zfill(2) + '.svg'] = pygame.image.load(self.base_path + 'characters/main/squat' + str(i).zfill(2) + '.svg').convert_alpha()

        for i in range(12):
            self.images['characters/main/crush' + str(i).zfill(2) + '.svg'] = pygame.image.load(self.base_path + 'characters/main/crush' + str(i).zfill(2) + '.svg').convert_alpha()

        for i in range(4):
            self.images['characters/subs/tai/swim' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'characters/subs/tai/swim' + str(i) + '.svg').convert_alpha()

        for i in range(5):
            self.images['characters/subs/tako/walk' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'characters/subs/tako/walk' + str(i) + '.svg').convert_alpha()

        for i in range(4):
            self.images['characters/subs/bee/fat_fly' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'characters/subs/bee/fat_fly' + str(i) + '.svg').convert_alpha()

        for i in range(4):
            self.images['characters/subs/bee/small_fly' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'characters/subs/bee/small_fly' + str(i) + '.svg').convert_alpha()

        for i in range(1):
            self.images['characters/subs/ammonite/swim.svg'] = pygame.image.load(self.base_path + 'characters/subs/ammonite/swim.svg').convert_alpha()

        self.images['characters/subs/sakuradama/stand.svg'] = pygame.image.load(self.base_path + 'characters/subs/sakuradama/stand.svg').convert_alpha()

        for i in range(360):
            self.images['items/rhythm_combo/drum' + str(i).zfill(3) + '.svg'] = pygame.image.load(self.base_path + 'items/rhythm_combo/drum' + str(i).zfill(3) + '.svg').convert_alpha()

        for i in range(10):
            self.images['items/time_travel_zone' + str(i) + '.svg'] = pygame.image.load(self.base_path + 'items/time_travel_zone' + str(i) + '.svg').convert_alpha()

        for i in range(1):
            self.images['items/message' + str(i).zfill(2) + '.svg'] = pygame.image.load(self.base_path + 'items/message' + str(i).zfill(2) + '.svg').convert_alpha()

        self.images['items/arrow_up.svg'] = pygame.image.load(self.base_path + 'items/arrow_up.svg').convert_alpha()
        self.images['items/arrow_right.svg'] = pygame.image.load(self.base_path + 'items/arrow_right.svg').convert_alpha()
        self.images['items/arrow_down.svg'] = pygame.image.load(self.base_path + 'items/arrow_down.svg').convert_alpha()
        self.images['items/arrow_left.svg'] = pygame.image.load(self.base_path + 'items/arrow_left.svg').convert_alpha()

        return

    def resetMessage(self):
        for i in range(1):
            self.images['items/message' + str(i).zfill(2) + '.svg'] = pygame.image.load(self.base_path + 'items/message' + str(i).zfill(2) + '.svg').convert_alpha()

        return

    def get(self, path):
        return self.images[path]
