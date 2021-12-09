import pygame
from modules.weapons.factory import WeaponsFactory

class Physical(pygame.sprite.Sprite):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        self.weapons_factory = WeaponsFactory()
        self.weapons = pygame.sprite.RenderUpdates()

        self.animation_type_infos = [
            # [key, file_name],
        ]
        self.frames = list() # 二次元配列で複数種類を入れる。animation_type_infosの数と一致させる

        # 以下はanimation_type_infosの数と一致させる
        # animation_indexは常に+animation_stepする
        # animation_indexがanimation_maxに達すると0にする

        # animation_interval_countは常に+1する
        # animation_interval_countがanimation_interval_count_max

        self.animation_type_infos = [['normal', 'normal']]
        self.animation_index = [0] 
        self.animation_step = [1]
        self.animation_max = [1]
        self.animation_file_max = [1]

        self.animation_interval_max = [1]
        self.animation_interval_index = [1]
        self.animation_interval_step = [1]
        self.animation_interval_count = [1]
        self.animation_interval_count_max = [1]

        self.x_distance = 0
        self.y_distance = 0
        self.last_distance = 0

        self.need_fall = True
        self.fall = False # 落ちるジャンプ
        self.crush = False

        return

    def __init__(self, image_loader, status, setting, info):
        pygame.sprite.Sprite.__init__(self)

        self.initializeVariable(image_loader, status, setting, info)

        self.image = self.frames[0][0]
        self.rect = self.image.get_rect()

        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = info[0]
        self.rect.y = info[1]

        self.weapon_interval_start = pygame.time.get_ticks()

        return

    def __del__(self):
        del(self.weapons_factory)
        del(self.weapons)

        del(self.animation_type_infos)
        del(self.frames)

        del(self.animation_index)
        del(self.animation_step)
        del(self.animation_max)
        del(self.animation_interval_max)
        del(self.animation_interval_index)
        del(self.animation_interval_count)
        del(self.animation_interval_count_max)

        del(self.x_distance)
        del(self.y_distance)
        del(self.last_distance)

        del(self.need_fall)
        del(self.fall)
        del(self.crush)

        return

    def clear(self, background_image):
        pygame.display.get_surface().blit(background_image, self.rect, self.rect)
        return

    def update(self, image_loader, status, setting, foregrounds, info):
        self.move(image_loader, status, setting, foregrounds)

        return

    def addAnimation(self, step, kind = 0):
        return None

    def animation(self, step, kind = 0):
        if self.animation_max[kind] == 1 and self.animation_file_max[kind] == 1:
            return True

        # 初期化
        if self.animation_interval_index[kind] == 0 and self.animation_interval_count[kind] == 0:
            for i in range(len(self.animation_type_infos)):
                if i == kind:
                    continue

                self.animation_index[i] = 0
                self.animation_interval_index[i] = 0
                self.animation_interval_count[i] = 0

        if self.animation_interval_max[kind] > 1 or self.animation_interval_count_max[kind] > 1:
            if self.animation_interval_count[kind] == 0 or self.animation_interval_count[kind] % self.animation_interval_count_max[kind] == 0:
                self.animation_interval_index[kind] += self.animation_interval_step[kind]
                if self.animation_interval_index[kind] == 0 or self.animation_interval_index[kind] % self.animation_interval_max[kind] != 0:
                    return True

            self.animation_interval_count[kind] += 1

        if step != 0:
            step = int(step / abs(step))

        step *= self.animation_step[kind]

        self.animation_index[kind] += step

        if step > 0 and self.animation_index[kind] >= self.animation_max[kind]:
            self.animation_index[kind] = 0

        elif step < 0 and self.animation_index[kind] <= 0:
            self.animation_index[kind] = self.animation_max[kind] - 1

        add_animation_result = self.addAnimation(step, kind)
        if add_animation_result != None:
            return add_animation_result

        if self.last_distance > 0:
            self.image = pygame.transform.flip(self.frames[kind][self.animation_index[kind]], True, False)
        else:
            self.image = self.frames[kind][self.animation_index[kind]]

        return True

    def hookHitWall(self, kind):
        pass

    def jumpStart(self, image_loader, status, setting, key):
        self.fall = True
        self.y_distance = -100

        if self.animation_index[1] >= 8:
            self.animation_index[1] = 8

        # しゃがむアニメーションをリセット
        self.animation_index[1] = 0
        self.animation_interval_index[1] = 0
        self.animation(0)

        return

    def jumpMove(self, foregrounds):
        g = 9.8

        self.y_distance += g
        
        if (self.__class__.__name__ == 'CharacterEbichikuwa' and self.combo_jump == True) and self.y_distance > -20:
            self.y_distance = 0
            self.combo_jump = False

        self.rect.y += self.y_distance / 4

        for foreground in foregrounds:
            if (self.fall == True or (self.__class__.__name__ == 'CharacterEbichikuwa' and self.combo_jump == True)) and self.rect.right > foreground.rect.left and self.rect.left < foreground.rect.right:
                # 着地
                if self.y_distance >= 0 and self.rect.top < foreground.rect.top and self.rect.bottom > foreground.rect.top:
                    found_ground = True
                    self.fall = False
                    self.rect.y = self.rect.y - (self.rect.bottom - foreground.rect.top)
                    self.y_distance = 0

                # 頭打ち
                if self.y_distance <= 0 and foreground.rect.top < self.rect.top and foreground.rect.bottom > self.rect.top:
                    self.rect.y = foreground.rect.bottom + 1
                    self.y_distance = 0

        return

    def moveStep(self):
        pass

    # 横移動のみ
    def move(self, image_loader, status, setting, foregrounds):
        if self.y_distance == 0 and self.x_distance == 0:
            return

        self.animation_interval_index[0] += 1

        self.moveStep()

        found_ground = False
        for foreground in foregrounds:
            # 横へ移動中に衝突
            if self.rect.top < foreground.rect.bottom and self.rect.bottom > foreground.rect.top:
                if self.x_distance > 0:
                    if self.rect.right + 1 >= foreground.rect.left and self.rect.right + 1 <= foreground.rect.right:
                        self.hookHitWall(type(foreground).__name__)
                elif self.x_distance < 0:
                    if self.rect.left - 1 <= foreground.rect.right and self.rect.left - 1 >= foreground.rect.left:
                        self.hookHitWall(type(foreground).__name__)

            # 落下の為の着地確認
            if self.need_fall:
                if self.rect.top < foreground.rect.top and self.rect.bottom >= foreground.rect.top and self.rect.right > foreground.rect.left and self.rect.left < foreground.rect.right:
                    found_ground = True

        # 段ボールの壁に衝突
        if (self.x_distance < 0 and self.rect.left <= setting['window']['margin_left']) or (self.x_distance > 0 and self.rect.right >= setting['window']['full_width'] - setting['window']['margin_right']):
            self.hookHitWall('DanballWall')

        # 落下
        if self.need_fall:
            if found_ground == False:
                self.fall = True

        if self.animation_interval_index[0] >= self.animation_interval_max[0]:
            self.animation(self.x_distance)
            self.animation_interval_index[0] = 0

        self.rect.x += self.x_distance
        if self.fall != True:
            self.rect.y += self.y_distance

        if self.x_distance != 0:
            self.last_distance = self.x_distance

        return
