from graphic_field_item_class import *

class CropGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """This class provides a pixmpa item with a preset image for the crop"""

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.crop._status == "Seed":
            self.setPixmap(QPixmap(self.available_graphics[0])).scaledToWidth(25,1)
        elif self.crop._status == "Seedling":
            self.setPixmap(QPixmap(self.available_graphics[1])).scaledToWidth(25,1)
        elif self.crop._status == "Young":
            self.setPixmap(QPixmap(self.available_graphics[2])).scaledToWidth(25,1)
        elif self.crop._status == "Mature":
            self.setPixmap(QPixmap(self.available_graphics[3])).scaledToWidth(25,1)
        elif self.crop._status == "Old":
            self.setPixmap(QPixmap(self.available_graphics[4])).scaledToWidth(25,1)
    def _harvest_crop(self):
        self.scene().harvest_crop(self)
    def contextMenuEvent(self, event):
        menu = QMenu("Crop")

        remove = menu.addAction("Harvest Crop")

        remove.triggered.connect(self._harvest_crop)

        #run the menu

        menu.exec_(event.screenPos())
        
