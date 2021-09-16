#!/usr/bin/env python3

import sys
import neat
import pygame
import random
import supportFunction as _supfunc
from Const import constants as _const
from Characters import bird as _bird
from Characters import cloud as _cloud
from Characters import cactus as _cactus
from Characters import dinosaur as _dino

max_score = 0
max_score_gen = 1

def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = _const.FONT.render(f'Pontos:  {str(points)}', True, (0, 0, 0))
        _const.SCREEN.blit(text, (950, 30))

def statistics(lenDinosaurs, gameSpeed, points, popGeneration):
    global max_score, max_score_gen
    text_1 = _const.FONT.render(f'Dinos Vivos:  {str(lenDinosaurs)}', True, (0, 0, 0))
    text_2 = _const.FONT.render(f'Geracao:  {popGeneration}', True, (0, 0, 0))
    text_3 = _const.FONT.render(f'Velocidade:  {str(gameSpeed)}', True, (0, 0, 0))
    if(max_score < points):
        max_score = points
        max_score_gen = popGeneration
        print(f'Maior Pontuacao:  {str(max_score)}')
        print(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}')
    text_4 = _const.FONT.render(f'Maior Pontuacao:  {str(max_score)}', True, (0, 0, 0))      
    text_5 = _const.FONT.render(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}', True, (0, 0, 0))

    _const.SCREEN.blit(text_1, (50, 430))
    _const.SCREEN.blit(text_2, (50, 460))
    _const.SCREEN.blit(text_3, (50, 490))
    _const.SCREEN.blit(text_4, (50, 520))
    _const.SCREEN.blit(text_5, (50, 550))

def background(game_speed):
    global x_pos_bg, y_pos_bg
    image_width = _const.BG.get_width()
    _const.SCREEN.blit(_const.BG, (x_pos_bg, y_pos_bg))
    _const.SCREEN.blit(_const.BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        x_pos_bg = 0
    x_pos_bg -= game_speed

def reportsNeat():
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

def evaluationFunction(genomes, config):
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs, points

    clock = pygame.time.Clock()
    points = 0
    obstacles = []
    dinosaurs = []
    ge = []
    nets = []
    cloud = _cloud.Cloud()
    dinosaur = _dino.Dinosaur()
    x_pos_bg = 0
    y_pos_bg = 380
    game_speed = 20

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

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(obstacles)

        if len(dinosaurs) == 0:
            break

        if len(obstacles) == 0:
            rand_int = random.randint(0, 3)
            if rand_int == 0:
                obstacles.append(_cactus.Cactus(_const.SMALL_CACTUS, random.randint(0, 2), _const.SMALL_CACTUS_RECT_HEIGHT))
            elif rand_int == 1:
                obstacles.append(_cactus.Cactus(_const.LARGE_CACTUS, random.randint(0, 2), _const.LARGE_CACTUS_RECT_HEIGHT))
            elif rand_int == 2:
                obstacles.append(_bird.Bird(_const.BIRD, _const.NORMAL_BIRD_RECT_HEIGHT))
            elif rand_int == 3:
                obstacles.append(_bird.Bird(_const.BIRD, _const.HIGH_BIRD_RECT_HEIGHT))

        for obstacle in obstacles:
            obstacle.draw(_const.SCREEN)
            obstacle.update(game_speed, obstacles)
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    _supfunc.remove(i, dinosaurs, ge, nets)

            for i, dinosaur in enumerate(dinosaurs):
                output = nets[i].activate((dinosaur.rect.y,
                                        _supfunc.distance(dinosaur.rect.midtop,obstacle.rect.midtop)))

                if output[0] >= 0.55 and dinosaur.rect.y == dinosaur.Y_POS:
                    dinosaur.dino_jump = True
                    dinosaur.dino_run = False

        score()
        background(game_speed)
        statistics(len(dinosaurs), game_speed, points, pop.generation)
        cloud.draw()
        cloud.update(game_speed)
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