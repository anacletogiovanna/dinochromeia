#!/usr/bin/env python3

import math
from Utils import constants as _const
from Utils import globalVariableAcross as _gva

'''
Função remove da coleção os Dinos que colidirem no obstáculo.
'''
def removeDino(index, dinosaurs, ge, nets):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)

'''
Função que ....
'''
def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)   

'''
Funcao que calcula a pontuacao e desenha em tela. 
'''
def score():
    _gva.points += 1
    gameSpeed()
    text = _const.FONT.render(f'Pontos: {str(_gva.points)}', True, (0, 0, 0))
    _const.SCREEN.blit(text, (950, 30))

'''
Funcao que calcula a velocidade do jogo, que e acrescida 
a cada vez que a pontuacao alcanca um valor multiplo de 100. 
'''
def gameSpeed():
    if _gva.points % 100 == 0:
        _gva.game_speed += 1

'''
Funcao que desenha a animacao do solo do cenario pre-historico.
'''
def background():
    image_width = _const.BG.get_width()
    _const.SCREEN.blit(_const.BG, (_gva.x_pos_bg, _gva.y_pos_bg))
    _const.SCREEN.blit(_const.BG, (image_width + _gva.x_pos_bg, _gva.y_pos_bg))
    if _gva.x_pos_bg <= -image_width:
        _gva.x_pos_bg = 0
    _gva.x_pos_bg -= _gva.game_speed


def statistics(lenDinosaurs, popGeneration):
    text_1 = _const.FONT.render(f'Dinos Vivos:  {str(lenDinosaurs)}', True, (0, 0, 0))
    text_2 = _const.FONT.render(f'Geracao:  {popGeneration}', True, (0, 0, 0))
    text_3 = _const.FONT.render(f'Velocidade:  {str(_gva.game_speed)}', True, (0, 0, 0))
    if(_gva.max_score < _gva.points):
        _gva.max_score = _gva.points
        _gva.max_score_gen = popGeneration
        print(f'Maior Pontuacao:  {str(_gva.max_score)}')
        print(f'Geracao da Maior Pontuacao:  {str(_gva.max_score_gen)}')
    text_4 = _const.FONT.render(f'Maior Pontuacao:  {str(_gva.max_score)}', True, (0, 0, 0))      
    text_5 = _const.FONT.render(f'Geracao da Maior Pontuacao:  {str(_gva.max_score_gen)}', True, (0, 0, 0))

    _const.SCREEN.blit(text_1, (50, 430))
    _const.SCREEN.blit(text_2, (50, 460))
    _const.SCREEN.blit(text_3, (50, 490))
    _const.SCREEN.blit(text_4, (50, 520))
    _const.SCREEN.blit(text_5, (50, 550))