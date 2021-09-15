import constants as const
import obstacle as _obstacle

class LargeCactus(_obstacle.Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = const.LARGE_CACTUS_RECT