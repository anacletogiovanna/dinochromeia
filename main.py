import pygame
import os
import random
import math
import sys
import neat
import constants as const

max_score = 0
max_score_gen = 1

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img=const.RUNNING[0]):
        self.run_img = const.RUNNING
        self.jump_img = const.JUMPING
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0

    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = const.JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def run(self):
        self.image = const.RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        for obstacle in obstacles:
            pygame.draw.line(SCREEN, self.color, (self.rect.x + 54, self.rect.y + 12), obstacle.rect.center, 2)

class Cloud:
    def __init__(self):
        self.x = const.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = const.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = const.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.rect.x = const.SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 300

class BirdNormal(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class BirdSuperLow(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 325
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class BirdSuperHigh(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config):
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs, ge, nets, points
    clock = pygame.time.Clock()
    points = 0


    obstacles = []
    dinosaurs = []
    ge = []
    nets = []

    cloud = Cloud()
    dinosaur = Dinosaur()

    x_pos_bg = 0
    y_pos_bg = 380

    game_speed = 20

    for genome_id, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = const.FONT.render(f'Pontos:  {str(points)}', True, (0, 0, 0))
        const.SCREEN.blit(text, (950, 50))

    def statistics():
        global dinosaurs, game_speed, ge, points, max_score, max_score_gen
        text_1 = const.FONT.render(f'Dinos Vivos:  {str(len(dinosaurs))}', True, (0, 0, 0))
        text_2 = const.FONT.render(f'Geração:  {pop.generation}', True, (0, 0, 0))
        text_3 = const.FONT.render(f'Velocidade:  {str(game_speed)}', True, (0, 0, 0))
        if(max_score < points):
            max_score = points
            max_score_gen = pop.generation
            print(f'Maior Pontuacao:  {str(max_score)}')
            print(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}')
        text_4 = const.FONT.render(f'Maior Pontuação:  {str(max_score)}', True, (0, 0, 0))      
        text_5 = const.FONT.render(f'Geracao da Maior Pontuacao:  {str(max_score_gen)}', True, (0, 0, 0))

        const.SCREEN.blit(text_1, (50, 450))
        const.SCREEN.blit(text_2, (50, 480))
        const.SCREEN.blit(text_3, (50, 510))
        const.SCREEN.blit(text_4, (50, 540))
        const.SCREEN.blit(text_5, (50, 570))

    def background():
        global x_pos_bg, y_pos_bg
        image_width = const.BG.get_width()
        const.SCREEN.blit(const.BG, (x_pos_bg, y_pos_bg))
        const.SCREEN.blit(const.BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        const.SCREEN.fill((255, 255, 255))

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(const.SCREEN)

        if len(dinosaurs) == 0:
            break

        if len(obstacles) == 0:
            rand_int = random.randint(0, 3)
            if rand_int == 0:
                obstacles.append(SmallCactus(const.SMALL_CACTUS, random.randint(0, 2)))
            elif rand_int == 1:
                obstacles.append(LargeCactus(const.LARGE_CACTUS, random.randint(0, 2)))
            elif rand_int == 2:
                 obstacles.append(BirdNormal(const.BIRD))
            elif rand_int == 3:
                obstacles.append(BirdSuperHigh(const.BIRD))
            # elif rand_int == 4:
            #     obstacles.append(BirdSuperLow(BIRD))

        for obstacle in obstacles:
            obstacle.draw(const.SCREEN)
            obstacle.update()
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    remove(i)

            for i, dinosaur in enumerate(dinosaurs):
                output = nets[i].activate((dinosaur.rect.y,
                                        distance(dinosaur.rect.midtop,obstacle.rect.midtop)))

                if output[0] >= 0.55 and dinosaur.rect.y == dinosaur.Y_POS:
                    dinosaur.dino_jump = True
                    dinosaur.dino_run = False
                    
        statistics()
        score()
        background()
        cloud.draw(const.SCREEN)
        cloud.update()
        clock.tick(30)
        pygame.display.update()


# Setup NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)

    # Add a stdout para mostrar o report do progresso do NEAT no terminal.
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    pop.run(eval_genomes, sys.maxsize)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)