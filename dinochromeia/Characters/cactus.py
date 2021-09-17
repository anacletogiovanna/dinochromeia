#!/usr/bin/env python3
#region Imports
from Characters import obstacle as _obstacle
#endregion

'''
Classe que herda de obstaculo.
"height_rect" informa a altura (coordenada y) do desenho do cacto na tela, 
variando entre SMALL_CACTUS_RECT_HEIGHT e LARGE_CACTUS_RECT_HEIGHT
'''
class Cactus(_obstacle.Obstacle):
    def __init__(self, image, number_of_cacti, height_rect):
        super().__init__(image, number_of_cacti)
        self.rect.y = height_rect