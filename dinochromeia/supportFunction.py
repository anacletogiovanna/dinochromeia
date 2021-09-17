#!/usr/bin/env python3

import math

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