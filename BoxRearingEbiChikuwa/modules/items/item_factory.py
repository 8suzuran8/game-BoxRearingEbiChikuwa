import pygame

from modules.common.singleton import Singleton
from modules.items.cardboard_close import ItemsCardboardClose
from modules.items.cardboard_open import ItemsCardboardOpen
from modules.items.message import ItemsMessage
from modules.items.stopwatch import ItemsStopwatch
from modules.items.rhythm_combos.rhythm01 import ItemsRhythmCombosRhythm01
from modules.items.bee_house import ItemsBeeHouse
from modules.items.time_travel_zone import ItemsTimeTravelZone
from modules.items.transparent_block import ItemsTransparentBlock # 地面
from modules.items.floating_block import ItemsFloatingBlock # 浮くブロック
from modules.items.floating_block_moving import ItemsFloatingBlockMoving # 動く浮くブロック

class ItemFactory(Singleton):
    def create(self, image_loader, status, setting, kind, info):
        return eval(str(kind).title().replace('_', '') + '(image_loader, status, setting, info)')
