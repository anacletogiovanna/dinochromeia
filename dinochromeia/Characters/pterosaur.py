#!/usr/bin/env python3

from Utils import constants as _const
from Characters import obstacle as _obstacle

'''
Classe que herda de obstaculo.
"height_rect" informa a altura (coordenada y) do desenho do pterosaur na tela, 
variando entre NORMAL_PTEROSAUR_RECT_HEIGHT e HIGH_PTEROSAUR_RECT_HEIGHT
'''
class Pterosaur(_obstacle.Obstacle):
    def __init__(self, image, height_rect):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = height_rect
        self.index = 0

    '''
    Função que desenha a imagem do pterosaur na tela.
    De 0 a 4 sera exibida a primeira imagem do pterosaur (resultado 0 na divisao) 
    De 5 a 9 sera exibida a segunda imagem do pterosaur(resultado 1 na divisao) 
    Em 10 o indice sera resetado
    '''
    def draw(self):
        if self.index >= 9:
            self.index = 0
        _const.SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1