#!/usr/bin/env python3
#region Imports
import os
import pygame
from Utils import constants as _const
import supportFunctionNeat as _supfuncNeat
#endregion

if __name__ == '__main__':
    pygame.display.set_caption(_const.GAMENAME)
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, _const.FILENAME_CONFIG_NEAT)
    _supfuncNeat.setupNeuralNetworkNeat(config_path)