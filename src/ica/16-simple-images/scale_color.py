from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic



def weighted_scale(picture, w1, w2, w3):
    new_pic = duplicatePicture(picture)

    for pixel in getPixels(new_pic):
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)

        lumin = w1 * r + w2 * g + w3 * b

        setColor(pixel, makeColor(lumin, lumin, lumin))

    return new_pic

pic = Picture("../SampleImages/antiqueTractors.jpg")
