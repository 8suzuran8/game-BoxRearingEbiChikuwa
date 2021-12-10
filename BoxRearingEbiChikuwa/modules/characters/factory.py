import random
from modules.common.singleton import Singleton

from modules.characters.subs.niihama_taikodai import CharacterNiihamaTaikodai
from modules.characters.main.ebichikuwa import CharacterEbichikuwa
from modules.characters.subs.tako import CharacterTako
from modules.characters.subs.tai import CharacterTai
from modules.characters.subs.bee import CharacterBee
from modules.characters.subs.sakuradama import CharacterSakuradama
from modules.characters.subs.ammonite import CharacterAmmonite

class CharacterFactory(Singleton):
    _KIND_NIIHAMA_TAIKODAI = 2
    _KIND_EBICHIKUWA = 3
    _KIND_TAKO = 4
    _KIND_TAI = 5
    _KIND_BEE = 6
    _KIND_SAKURADAMA = 7
    _KIND_AMMONITE = 8

    def create(self, image_loader, status, setting, kind, info):
        if kind == CharacterFactory._KIND_NIIHAMA_TAIKODAI:
            return CharacterNiihamaTaikodai(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_EBICHIKUWA:
            return CharacterEbichikuwa(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_TAKO:
            return CharacterTako(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_TAI:
            return CharacterTai(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_BEE:
            bee_kind = random.randint(CharacterBee._KIND_FAT, CharacterBee._KIND_SMALL)
            info.append(bee_kind)
            return CharacterBee(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_SAKURADAMA:
            return CharacterSakuradama(image_loader, status, setting, info)
        elif kind == CharacterFactory._KIND_AMMONITE:
            return CharacterAmmonite(image_loader, status, setting, info)
