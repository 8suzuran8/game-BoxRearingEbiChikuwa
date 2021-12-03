import pygame

from modules.common.singleton import Singleton
from modules.items.cardboard_close import ItemsCardboardClose
from modules.items.cardboard_open import ItemsCardboardOpen
from modules.items.items import ItemsSimple
from modules.items.stopwatch import ItemsStopwatch
from modules.items.rhythm_combo.drum import ItemsRhythmComboDrum
from modules.items.rhythm_combo.rhythm01 import ItemsRhythmComboRhythm01
from modules.items.rhythm_combo.aim import ItemsRhythmComboAim
from modules.items.bee_house import ItemsBeeHouse
from modules.items.time_travel_zone import ItemsTimeTravelZone
from modules.items.transparent_block import ItemsTransparentBlock # 地面
from modules.items.floating_block import ItemsFloatingBlock # 浮くブロック

class ItemFactory(Singleton):
    def create(self, image_loader, status, setting, kind, path, info):
        return eval(str(kind).title().replace('_', '') + '(image_loader, status, setting, path, info)')
