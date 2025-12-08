from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *

def scale_up(pic):
    width = pic.getWidth()
    height = pic.getHeight()

    new_pic = Picture(width * 2, height * 2)

    for x in range(width):
        for y in range(height):
            color = pic.getColor(x, y)

            target_x = x * 2
            target_y = y * 2

            new_pic.setColor(target_x,     target_y,     color)
            new_pic.setColor(target_x + 1, target_y,     color)
            new_pic.setColor(target_x,     target_y + 1, color)
            new_pic.setColor(target_x + 1, target_y + 1, color)

    return new_pic

keep_windows_open()