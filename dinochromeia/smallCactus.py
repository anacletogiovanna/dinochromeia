import constants as const
import obstacle as _obstacle

class SmallCactus(_obstacle.Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = const.SMALL_CACTUS_RECT