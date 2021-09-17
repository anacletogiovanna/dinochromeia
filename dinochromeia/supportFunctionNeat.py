#!/usr/bin/env python3

import sys
import neat
import pygame
import random
import supportFunctionGame as _supfunc
from Utils import constants as _const
from Characters import pterosaur as _ptero
from Characters import cloud as _cloud
from Characters import cactus as _cactus
from Characters import dinosaur as _dino
from Utils import globalVariableAcross as _gva

def reportsNeat():
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)


def evaluationFunction(genomes, config):
    global obstacles, dinosaurs
    _gva.points = 0
    clock = pygame.time.Clock()
    obstacles = []
    dinosaurs = []
    ge = []
    nets = []
    cloud = _cloud.Cloud()
    dinosaur = _dino.Dinosaur()
    _gva.x_pos_bg = 0
    _gva.y_pos_bg = 380
    _gva.game_speed = 20

    for genome_id, genome in genomes:
        dinosaurs.append(_dino.Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            
        _const.SCREEN.fill((255, 255, 255))

        #Atualizo a acao e desenho em tela a animacao do Dino
        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(obstacles)

        #Se o numero de Dinos for zero, saio do loop principal e analiso uma nova geracao.
        if len(dinosaurs) == 0:
            break
        
        #Adiciona aleatoriamente um obstaculo dentre as possiveis opcoes
        if len(obstacles) == 0:
            obstacleChoice = random.randint(0, 3)
            if obstacleChoice == 0:
                obstacles.append(_cactus.Cactus(_const.SMALL_CACTUS, random.randint(0, 2), _const.SMALL_CACTUS_RECT_HEIGHT))
            elif obstacleChoice == 1:
                obstacles.append(_cactus.Cactus(_const.LARGE_CACTUS, random.randint(0, 2), _const.LARGE_CACTUS_RECT_HEIGHT))
            elif obstacleChoice == 2:
                obstacles.append(_ptero.Pterosaur(_const.PTEROSAUR, _const.NORMAL_PTEROSAUR_RECT_HEIGHT))
            elif obstacleChoice == 3:
                obstacles.append(_ptero.Pterosaur(_const.PTEROSAUR, _const.HIGH_PTEROSAUR_RECT_HEIGHT))

        #Desenha os obstaculos na tela e caso o Dino colida com um deles chama a função "removeDino()"
        for obstacle in obstacles:
            obstacle.draw()
            obstacle.update(_gva.game_speed, obstacles)
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    _supfunc.removeDino(i, dinosaurs, ge, nets)

            for i, dinosaur in enumerate(dinosaurs):
                output = nets[i].activate((dinosaur.rect.y,
                                        _supfunc.distance(dinosaur.rect.midtop,obstacle.rect.midtop)))

                if output[0] >= 0.55 and dinosaur.rect.y == dinosaur.Y_POS:
                    dinosaur.dino_jump = True
                    dinosaur.dino_run = False

        _supfunc.score()
        _supfunc.background()
        _supfunc.statistics(len(dinosaurs), pop.generation)
        cloud.draw()
        cloud.update(_gva.game_speed)
        clock.tick(30)
        pygame.display.update()


def setupNeuralNetworkNeat(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )
    pop = neat.Population(config)
    reportsNeat()
    pop.run(evaluationFunction, sys.maxsize)