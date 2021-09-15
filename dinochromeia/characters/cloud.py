#!/usr/bin/env python3

import random
from Const import constants as _const

class Cloud():
    def __init__(self):
        self.x = _const.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = _const.CLOUD
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = _const.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self):
        _const.SCREEN.blit(self.image, (self.x, self.y))