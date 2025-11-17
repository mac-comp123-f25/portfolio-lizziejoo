from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(org_picture, start_x, start_y, width, height):
    new_pic = Picture(width, height)
    for x in range(width):
        for y in range(height):
            original_x = start_x + x
            original_y = start_y + y
            color = org_picture.getColor(original_x, original_y)
            new_pic.setColor(x, y, color)

    return new_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

keep_windows_open()



