import sys
import pygame
from modules.items.item_factory import ItemFactory
from modules.characters.factory import CharacterFactory

class StagesPlay:
    def __new__(cls, image_loader, status, setting):
        self = super().__new__(cls)

        return self

    def initializeVariable(self, image_loader, status, setting):
        self.foregrounds = pygame.sprite.RenderUpdates() # マップ処理
        self.animations = pygame.sprite.RenderUpdates() # 遅いアニメーション
        self.speed_animations = pygame.sprite.RenderUpdates() # 早いアニメーション
        self.characters = pygame.sprite.RenderUpdates() # 当たり判定

        self.item_factory = ItemFactory()
        self.character_factory = CharacterFactory()

        self.PYGAME_EVENTTYPE_TIMEREVENT = pygame.USEREVENT + 1
        self.stopwatch_timer = 99

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

    def createSprites(self, image_loader, status, setting):
        # 背景
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_cardboard_open', '', [0, 0]),
            'key': 'background',
        })
        self.sprite_indexes['background'] = len(self.sprites) - 1

        # 霧 @TODO
        # for i in range(int(setting['window']['moving_height'] / 50)): # y
        #     for j in range(int(setting['window']['moving_width'] / 50)): # x
        #         x = j * 50 + setting['window']['margin_left']
        #         y = i * 50 + setting['window']['margin_top']
        #         self.sprites[self.sprite_indexes['background']]['sprite'].image.blit(image_loader.get('items/smoke.svg'), [x, y])

        # 時間枠
        x = setting['window']['margin_left'] + setting['window']['moving_width'] / 2 - 28
        y = 0
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_stopwatch', '99', [x, y]),
            'key': 'stopwatch',
        })
        self.sprite_indexes['stopwatch'] = len(self.sprites) - 1
        self.stopwatch = self.sprites[self.sprite_indexes['stopwatch']]['sprite']

        # 浮遊ブロック
        for floating_block_info in self.floating_block_infos:
            self.sprites.append({
                'sprite': self.item_factory.create(image_loader, status, setting, 'items_floating_block', '', floating_block_info),
                'key': 'floating_block',
            })
            floating_block_index = len(self.sprites) - 1
            self.foregrounds.add(self.sprites[floating_block_index]['sprite'])
            self.sprites[self.sprite_indexes['background']]['sprite'].image.blit(image_loader.get('items/floating_box_' + floating_block_info[2] + '.svg'), [self.sprites[floating_block_index]['sprite'].rect.x, self.sprites[floating_block_index]['sprite'].rect.y - 10])

        # 蜂の巣
        x = setting['window']['full_width'] / 2 - 50
        y = setting['window']['margin_top'] + 30
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_bee_house', 'items/bee_house.svg', [x, y]),
            'key': 'bee_house',
        })
        self.sprite_indexes['bee_house'] = len(self.sprites) - 1
        self.speed_animations.add(self.sprites[self.sprite_indexes['bee_house']]['sprite'])

        # 和太鼓
        x = 200
        y = 0
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_rhythm_combos_rhythm01', '', [x, y]),
            'key': 'rhythm_combo',
        })
        self.sprite_indexes['rhythm_combo_drum'] = len(self.sprites) - 1
        self.speed_animations.add(self.sprites[self.sprite_indexes['rhythm_combo_drum']]['sprite'])
        # 吹き出し
        message_position = [
            self.npc_position[0] + setting['window']['block_size'],
            self.npc_position[1],
        ]
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_message', '', message_position),
            'key': 'message',
        })
        self.sprite_indexes['message'] = len(self.sprites) - 1

        # 天井
        x = setting['window']['margin_left']
        y = setting['window']['margin_top'] - setting['window']['block_size']
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_transparent_block', '', [x, y]),
            'key': 'topground',
        })
        self.sprite_indexes['topground'] = len(self.sprites) - 1
        self.foregrounds.add(self.sprites[self.sprite_indexes['topground']]['sprite'])

        # 底辺の地面
        x = setting['window']['margin_left']
        y = setting['window']['margin_top'] + setting['window']['moving_height']
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_transparent_block', '', [x, y]),
            'key': 'bottomground',
        })
        self.sprite_indexes['bottomground'] = len(self.sprites) - 1
        self.foregrounds.add(self.sprites[self.sprite_indexes['bottomground']]['sprite'])

        self.background_image = self.sprites[self.sprite_indexes['background']]['sprite'].image.copy()

        # タイムトラベルゾーン
        self.sprites.append({
            'sprite': self.item_factory.create(image_loader, status, setting, 'items_time_travel_zone', '', self.time_travel_zone_position),
            'key': 'time_travel_zone',
        })
        self.sprite_indexes['time_travel_zone'] = len(self.sprites) - 1
        self.time_travel_zone = self.sprites[self.sprite_indexes['time_travel_zone']]['sprite']
        self.speed_animations.add(self.sprites[self.sprite_indexes['time_travel_zone']]['sprite'])

        # NPC
        self.sprites.append({
            'sprite': self.character_factory.create(image_loader, status, setting, self.character_factory._KIND_SAKURADAMA, self.npc_position),
            'key': 'npc',
        })
        self.sprite_indexes['npc'] = len(self.sprites) - 1

        # 主人公
        self.sprites.append({
            'sprite': self.character_factory.create(image_loader, status, setting, self.character_factory._KIND_EBICHIKUWA, self.main_character_initial_position),
            'key': 'main_character',
        })
        self.sprite_indexes['main_character'] = len(self.sprites) - 1

        # 敵キャラ
        for enemy_info in self.enemy_infos:
            self.sprites.append({
                'sprite': self.character_factory.create(image_loader, status, setting, enemy_info[2], [enemy_info[0], enemy_info[1]]),
                'key': 'enemy',
            })

            enemy_index = len(self.sprites) - 1
            self.animations.add(self.sprites[enemy_index]['sprite'])
            if enemy_info[2] != self.character_factory._KIND_NIIHAMA_TAIKODAI:
                self.characters.add(self.sprites[enemy_index]['sprite'])

            if len(enemy_info) == 4:
                enemy_info[3](self.sprites[enemy_index]['sprite'])

        return

    def getMovingXyByPosition(self, image_loader, status, setting, x_index, y_index, kind):
        return [
            setting['window']['margin_left'] + setting['window']['block_size'] * x_index,
            setting['window']['margin_top'] + setting['window']['block_size'] * y_index,
            kind,
        ]

    def __init__(self, image_loader, status, setting):
        self.initializeVariable(image_loader, status, setting)
        self.createSprites(image_loader, status, setting)

        pygame.display.get_surface().blit(self.sprites[self.sprite_indexes['background']]['sprite'].image, self.sprites[self.sprite_indexes['background']]['sprite'].rect)
        pygame.display.get_surface().blit(self.sprites[self.sprite_indexes['stopwatch']]['sprite'].image, self.sprites[self.sprite_indexes['stopwatch']]['sprite'].rect)

        pygame.key.set_repeat(30)
        pygame.time.set_timer(self.PYGAME_EVENTTYPE_TIMEREVENT, 50)
        self.sprites[self.sprite_indexes['stopwatch']]['sprite'].changeTime(image_loader, status, setting, self.stopwatch_timer)

        return

    def __del__(self):
        # emptyでdelも実行される
        self.foregrounds.empty()
        self.animations.empty()
        self.speed_animations.empty()
        self.characters.empty()

        del(self.item_factory)
        del(self.character_factory)

        del(self.PYGAME_EVENTTYPE_TIMEREVENT)
        del(self.stopwatch_timer)

        del(self.sprites)
        del(self.sprite_indexes)

        return

    def chkDie(self, image_loader, status, setting):
        # 死亡条件チェック
        for character in self.characters:
            # 敵の破壊
            killed = False
            for weapon in self.sprites[self.sprite_indexes['main_character']]['sprite'].weapons:
                if character.rect.colliderect(weapon.rect):
                    character.kill()
                    del(character)
                    weapon.kill()
                    del(weapon)
                    killed = True
                    break

            if killed:
                continue

            # 自分の破壊
            if self.sprites[self.sprite_indexes['main_character']]['sprite'].rect.colliderect(character.rect):
                self.sprites[self.sprite_indexes['main_character']]['sprite'].crush = True

        return

    def timeEventAction50(self, image_loader, status, setting, timeevent_count):
        # 飛ぶ
        for jump_target in pygame.sprite.RenderUpdates(self.characters, self.sprites[self.sprite_indexes['main_character']]['sprite'], self.sprites[self.sprite_indexes['main_character']]['sprite'].weapons):
            if jump_target.fall or (jump_target.__class__.__name__ == 'CharacterEbichikuwa' and jump_target.combo_jump):
                self.sprites[self.sprite_indexes['main_character']]['sprite'].clear(self.background_image)
                pygame.display.update(self.sprites[self.sprite_indexes['main_character']]['sprite'].rect)
                jump_target.jumpMove(self.foregrounds)

            if jump_target.__class__.__name__ == 'WeaponsGun' and jump_target.dead:
                jump_target.kill()
                del(jump_target)

        # 弾丸
        self.sprites[self.sprite_indexes['main_character']]['sprite'].weapons.clear(pygame.display.get_surface(), self.sprites[self.sprite_indexes['background']]['sprite'].image)

        # 敵の移動
        self.characters.update(image_loader, status, setting, self.foregrounds, {'main_character_rect': self.sprites[self.sprite_indexes['main_character']]['sprite'].rect})

        self.sprites[self.sprite_indexes['main_character']]['sprite'].comboAction(image_loader, status, setting)

        for speed_animation in self.speed_animations.sprites():
            if type(speed_animation).__name__.startswith('Items'):
                # Characterはmoveに合わせてアニメーションさせるため。
                speed_animation.animation()

        return

    def timeEventAction500(self, image_loader, status, setting, timeevent_count):
        return

    def timeEventAction3000(self, image_loader, status, setting, timeevent_count):
        if timeevent_count != 0 and timeevent_count % 60 != 0:
            return

        if self.stopwatch_timer > 0:
            self.stopwatch_timer -= 1
            self.stopwatch.changeTime(image_loader, status, setting, self.stopwatch_timer)
            pygame.display.update(self.stopwatch.rect)

        if self.stopwatch_timer % 10 == 0:
            x = setting['window']['full_width'] / 2 - 50
            y = setting['window']['margin_top'] + 30
            self.sprites.append({
                'sprite': self.character_factory.create(image_loader, status, setting, self.character_factory._KIND_BEE, [x, y]),
                'key': 'enemy',
            })
            enemy_index = len(self.sprites) - 1
            self.characters.add(self.sprites[enemy_index]['sprite'])
            self.speed_animations.add(self.sprites[enemy_index]['sprite'])

        return

    def start(self, image_loader, status, setting):
        surface = pygame.display.get_surface()

        timeevent_count = 0
        rhythm_combo_aim_action = False

        pygame.display.flip()

        while True:
            rect_list = []

            if self.sprites[self.sprite_indexes['main_character']]['sprite'].crush == True:
                crush_animation_result = self.sprites[self.sprite_indexes['main_character']]['sprite'].animation(+1, 2)
                if type(crush_animation_result).__name__ == 'int':
                    return crush_animation_result

                self.sprites[self.sprite_indexes['main_character']]['sprite'].clear(self.background_image)
                surface.blit(self.sprites[self.sprite_indexes['main_character']]['sprite'].image, self.sprites[self.sprite_indexes['main_character']]['sprite'].rect)
                pygame.display.update(self.sprites[self.sprite_indexes['main_character']]['sprite'].rect)

                continue

            pygame.time.wait(30)

            self.sprites[self.sprite_indexes['main_character']]['sprite'].clear(self.background_image)
            self.animations.clear(surface, self.background_image)
            self.speed_animations.clear(surface, self.background_image)

            for event in pygame.event.get():
                if event.type == self.PYGAME_EVENTTYPE_TIMEREVENT: # 50 ms
                    timeevent_count += 1

                    self.chkDie(image_loader, status, setting)
                    self.timeEventAction50(image_loader, status, setting, timeevent_count)
                    self.timeEventAction500(image_loader, status, setting, timeevent_count)
                    self.timeEventAction3000(image_loader, status, setting, timeevent_count)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return

                    if self.sprites[self.sprite_indexes['main_character']]['sprite'].combo_index > -1:
                        rhythm_combo_aim_action = True
                        continue

                    if event.key == pygame.K_LEFT:
                        if self.sprites[self.sprite_indexes['main_character']]['sprite'].animation_index[1] == 0:
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].x_distance = -2
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].move(image_loader, status, setting, self.foregrounds)
                    elif event.key == pygame.K_RIGHT:
                        if self.sprites[self.sprite_indexes['main_character']]['sprite'].animation_index[1] == 0:
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].x_distance = 2
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].move(image_loader, status, setting, self.foregrounds)
                    elif event.key == pygame.K_SPACE:
                        # ジャンプ溜め
                        if self.sprites[self.sprite_indexes['main_character']]['sprite'].fall == False:
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].animation(+1, 1)

                    if self.sprites[self.sprite_indexes['main_character']]['sprite'].rect.colliderect(self.sprites[self.sprite_indexes['npc']]['sprite'].rect):
                        self.sprites[self.sprite_indexes['npc']]['sprite'].clear = True

                elif event.type == pygame.KEYUP:
                    self.sprites[self.sprite_indexes['main_character']]['sprite'].comboInput(event.key, self.sprites[self.sprite_indexes['rhythm_combo_drum']]['sprite'])

                    if event.key == pygame.K_z:
                        if self.sprites[self.sprite_indexes['main_character']]['sprite'].animation_index[1] == 0:
                            self.sprites[self.sprite_indexes['main_character']]['sprite'].attack(image_loader, status, setting)

                    elif event.key == pygame.K_SPACE:
                        # ジャンプ
                        self.sprites[self.sprite_indexes['main_character']]['sprite'].jumpStart(image_loader, status, setting, event.key)

            rhythm_combo_aim_action = False

            pygame.display.get_surface().blit(self.sprites[self.sprite_indexes['npc']]['sprite'].image, self.sprites[self.sprite_indexes['npc']]['sprite'].rect)
            if self.sprites[self.sprite_indexes['npc']]['sprite'].clear == True:
                surface.blit(self.sprites[self.sprite_indexes['message']]['sprite'].image, self.sprites[self.sprite_indexes['message']]['sprite'].rect)
            surface.blit(self.sprites[self.sprite_indexes['main_character']]['sprite'].image, self.sprites[self.sprite_indexes['main_character']]['sprite'].rect)

            rect_list += self.sprites[self.sprite_indexes['main_character']]['sprite'].weapons.draw(surface)
            rect_list += self.animations.draw(surface)
            rect_list += self.speed_animations.draw(surface)
            rect_list += [self.sprites[self.sprite_indexes['npc']]['sprite'].rect]
            rect_list += [self.sprites[self.sprite_indexes['message']]['sprite'].rect]
            rect_list += [self.sprites[self.sprite_indexes['main_character']]['sprite'].rect]

            if len(rect_list) > 0:
                pygame.display.update(rect_list)
