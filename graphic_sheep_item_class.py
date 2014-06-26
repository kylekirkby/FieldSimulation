from graphic_animal_item_class import *

from sheep_class import *

import field_resources

class CowGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    """This class provides a graphical representation of a sheep"""

    def __init__(self):
        self.available_graphics = [":/sheep_baby.png",":/sheep_poor.png",
                                   ":/sheep_fine.png",":/sheep_prime.png"]

        super().__init__(self.available_graphics)

        self.animal = Sheep()
