from PyQt4.QtGui import *

from field_class import *

from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *

import field_resources


class FieldGraphicsScene(QGraphicsScene):
    """This class provides a scene to manage items in the field"""

    def __init__(self,max_crops,max_animals):
        super().__init__()

        self.field = Field(max_animals,max_crops)

        self.background_brush = QBrush()

        self.background_picture = QPixmap(":/field_background.png")
        self.background_brush.setTexture(self.background_picture)
        self.setBackgroundBrush(self.background_brush)

    def harvest_crop(self,crop_to_harvest):
        position = self.field._crops.index(crop_to_harvest)
        self.field.harvest_crop(position) #remove crop from field
        self.removeItem(crop_to_harvest)

    def remove_animal(self,animal_to_remove):
        position = self.field._animals.index(animal_to_remove)
        self.field.remove_animal(position) # remove animal from field
        self.removeItem(animal_to_remove) # remove from visual representation

    def _visualise_graphic_item(self,graphic_item_type):
        if graphic_item_type == "crop":
            x,y = self._drop_position(self.field._crops[-1])
            self.field._crops[-1].setPos(x,y)
            self.addItem(self.field._crops[-1])
        elif graphic_item_type == "animal":
            x,y  = self._drop_position(self.field._animals[-1])
            self.field._animals[-1].setPos(x,y)
            self.addItem(self.field._animals[-1])

    def _drop_position(self, item):
        cursor_pos = QCursor.pos() # gets the global position relative to the screen
        current_view = self.views()[0]
        scene_position = current_view.mapFromGlobal(cursor_pos) #converts the global cursor pos - view coords

        width = item.boundingRect().width()
        height = item.boundingRect().height()

        #workout where the item should be positioned

        width_offset = width/2
        height_offset = height/2

        drop_x = scene_position.x() - width_offset
        drop_y = scene_position.y() - height_offset

        return drop_x, drop_y
        

    

    def _add_graphic_item(self,result,graphic_item_type):

        if result:
            self._visualise_graphic_item(graphic_item_type)
        else:
            error_message = QMessageBox()
            error_message.setText("No more {0}s can be added to this field".format(graphic_item_type))
            error_message.exec()




    #this method overides the parent method
    

    def dragEnterEvent(self, event):
        
        #what to do if an object is dragged into the scene

        event.accept()

    def dragMoveEvent(self,event):
        event.accept()

    def dropEvent(self,event):
        
        event.accept()

        #what to do if an object is dropped onto the scene

        if event.mimeData().hasFormat("application/x-wheat"):
            crop_added = self.field.plant_crop(WheatGraphicsPixmapItem())
            self._add_graphic_item(crop_added,"crop")
        elif event.mimeData().hasFormat("application/x-potato"):
            crop_added = self.field.plant_crop(PotatoGraphicsPixmapItem())
            self._add_graphic_item(crop_added,"crop")
        elif event.mimeData().hasFormat("application/x-cow"):
            animal_added = self.field.add_animal(CowGraphicsPixmapItem())
            self._add_graphic_item(animal_added,"animal")
        elif event.mimeData().hasFormat("application/x-sheep"):
            animal_added = self.field.add_animal(SheepGraphicsPixmapItem())
            self._add_graphic_item(animal_added,"animal")

