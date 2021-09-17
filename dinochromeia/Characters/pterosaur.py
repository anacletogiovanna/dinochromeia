#!/usr/bin/env python3

from Utils import constants as _const
from Characters import obstacle as _obstacle

'''
Classe que herda de obstaculo.
"height_rect" informa a altura (coordenada y) do desenho do passaro na tela, 
variando entre NORMAL_PTEROSAUR_RECT_HEIGHT e HIGH_PTEROSAUR_RECT_HEIGHT
'''
class Pterosaur(_obstacle.Obstacle):
    def __init__(self, image, height_rect):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = height_rect
        self.index = 0

    '''
    Função que desenha a imagem da nuvem na tela.
    '''
    def draw(self):
        if self.index >= 9:
            self.index = 0
        _const.SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1