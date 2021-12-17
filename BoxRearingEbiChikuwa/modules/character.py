from modules.physical import Physical

class Character(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def __init__(self, image_loader, status, setting, info):
        Physical.__init__(self, image_loader, status, setting, info)

        self.rect.y -= 25

        return
