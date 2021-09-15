import os
import constants as const
import supportFunctionNeat as _supfuncNeat

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, const.FILENAME_CONFIG_NEAT)
    _supfuncNeat.setupNeuralNetworkNeat(config_path)