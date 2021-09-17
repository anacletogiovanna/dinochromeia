#!/usr/bin/env python3

import random
import pygame
from Const import constants as _const

class Dinosaur():
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img=_const.RUNNING[0]):
        self.run_img = _const.RUNNING
        self.jump_img = _const.JUMPING
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0

    '''
    Funcao de atualizacao das acoes do Dino baseado no estado em que o mesmo se encontra.
    step_index apoia na troca de imagens para dar a animacar ao Dino.
    '''
    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    '''
    Funcao responsavel pelo animacao da acao de pular do Dino.
    '''
    def jump(self):
        self.image = _const.JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    '''
    Funcao responsavel pela animacao da acao de correr do Dino.
    De 0 a 4 sera exibida a primeira imagem de corrida (resultado 0 na divisao) 
    De 5 a 9 sera exibida a segunda imagem de corrida (resultado 1 na divisao) 
    '''
    def run(self):
        self.image = _const.RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    '''
    Função que desenha a imagem do Dino na tela.
    Envolvendo-o com um retangulo de cor aleatoria e 
    com uma linha de mesma cor do Dino até os obstáculos.
    '''
    def draw(self, obstacles):
        _const.SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(_const.SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        for obstacle in obstacles:
            pygame.draw.line(_const.SCREEN, self.color, (self.rect.x + 54, self.rect.y + 12), obstacle.rect.center, 2)
