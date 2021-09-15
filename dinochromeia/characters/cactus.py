from characters import obstacle as _obstacle

class Cactus(_obstacle.Obstacle):
    def __init__(self, image, number_of_cacti, height_rect):
        super().__init__(image, number_of_cacti)
        self.rect.y = height_rect