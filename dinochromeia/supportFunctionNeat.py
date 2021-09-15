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


game_speed = 0
max_score = 0
max_score_gen = 1


def reportsNeat(pop):
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

def eval_genomes(genomes, config):
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs, ge, nets, points
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

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = _const.FONT.render(f'Pontos:  {str(points)}', True, (0, 0, 0))
        _const.SCREEN.blit(text, (950, 50))

    def statistics():
        global dinosaurs, game_speed, ge, points, max_score, max_score_gen
        text_1 = _const.FONT.render(f'Dinos Vivos:  {str(len(dinosaurs))}', True, (0, 0, 0))
        text_2 = _const.FONT.render(f'Geração:  {pop.generation}', True, (0, 0, 0))
        text_3 = _const.FONT.render(f'Velocidade:  {str(game_speed)}', True, (0, 0, 0))
        if(max_score < points):
            max_score = points
            max_score_gen = pop.generation
            print(f'Maior Pontuacao:  {str(max_score)}')
            print(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}')
        text_4 = _const.FONT.render(f'Maior Pontuação:  {str(max_score)}', True, (0, 0, 0))      
        text_5 = _const.FONT.render(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}', True, (0, 0, 0))

        _const.SCREEN.blit(text_1, (50, 450))
        _const.SCREEN.blit(text_2, (50, 480))
        _const.SCREEN.blit(text_3, (50, 510))
        _const.SCREEN.blit(text_4, (50, 540))
        _const.SCREEN.blit(text_5, (50, 570))

    def background():
        global x_pos_bg, y_pos_bg
        image_width = _const.BG.get_width()
        _const.SCREEN.blit(_const.BG, (x_pos_bg, y_pos_bg))
        _const.SCREEN.blit(_const.BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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

        statistics()
        score()
        background()
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
    reportsNeat(pop)
    pop.run(eval_genomes, sys.maxsize)