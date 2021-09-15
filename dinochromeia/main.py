#!/usr/bin/env python3

import os
from Const import constants as _const
import supportFunctionNeat as _supfuncNeat

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, _const.FILENAME_CONFIG_NEAT)
    _supfuncNeat.setupNeuralNetworkNeat(config_path)