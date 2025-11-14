from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(org_picture, start_x, start_y, width, height):
    crop_picture = 


dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

