#!/usr/bin/env python3

from Characters import obstacle as _obstacle

class Bird(_obstacle.Obstacle):
    def __init__(self, image, height_rect):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = height_rect
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1