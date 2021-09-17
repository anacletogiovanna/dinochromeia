#!/usr/bin/env python3
#region Imports
from Utils import constants as _const
#endregion

class Obstacle():
    def __init__(self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.rect.x = _const.SCREEN_WIDTH

    '''
    Funcao de atualizacao da animação do obstaculo.
    Quando o obstaculo sair da tela, ele é retirado da lista de obstaculos. 
    '''
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    '''
    Função que desenha a imagem do obstáculo na tela.
    '''
    def draw(self):
        _const.SCREEN.blit(self.image[self.type], self.rect)