import pygame

from modules.common.singleton import Singleton
from modules.stages.titles.start import StagesTitlesStart
from modules.stages.titles.option import StagesTitlesOption
from modules.stages.titles.bad_end import StagesTitlesBadEnd
from modules.stages.titles.good_end import StagesTitlesGoodEnd
from modules.stages.plays.number0101 import StagesPlaysNumber0101
from modules.stages.plays.number0102 import StagesPlaysNumber0102
from modules.stages.plays.number_random import StagesPlaysNumberRandom

class StageFactory(Singleton):
    def create(self, kind, image_loader, status, setting):
        kind_type = type(kind).__name__

        if kind_type == 'int':
            if kind == 0:
                # start
                return StagesTitlesStart(image_loader, status, setting)

            elif kind == -1:
                # option
                return StagesTitlesOption(image_loader, status, setting)

            elif kind == -2:
                # bad end
                return StagesTitlesBadEnd(image_loader, status, setting)

            elif kind == -3:
                # good end
                return StagesTitlesGoodEnd(image_loader, status, setting)
        elif kind_type == 'str':
            try:
                return eval('StagesPlaysNumber' + kind + '(image_loader, status, setting)')
            except:
                return StagesPlaysNumberRandom(image_loader, status, setting)
