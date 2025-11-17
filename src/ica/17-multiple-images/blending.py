from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1, pic2):
    width = pic1.getWidth()
    height = pic1.getHeight()
    blended = Picture(width, height)

    for x in range(width):
        for y in range(height):
            r1, g1, b1 = pic1.getColor(x, y)
            r2, g2, b2 = pic2.getColor(x, y)

            r = (r1 + r2) // 2
            g = (g1 + g2) // 2
            b = (b1 + b2) // 2

            blended.setColor(x, y, (r, g, b))

    blended.show()
    return blended


def blend2(pic1, pic2):
    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            r1, g1, b1 = pic1.getColor(x, y)
            r2, g2, b2 = pic2.getColor(x, y)

            red   = (r1 + r2) // 2
            green = (g1 + g2) // 2
            blue  = (b1 + b2) // 2

            new_pic.setColor(x, y, (red, green, blue))

    new_pic.show()
    return new_pic

def weighted_blend(pic1, pic2, wgt1):
    wgt2 = 1.0 - wgt1

    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            r1, g1, b1 = pic1.getColor(x, y)
            r2, g2, b2 = pic2.getColor(x, y)

            red   = int(wgt1 * r1 + wgt2 * r2)
            green = int(wgt1 * g1 + wgt2 * g2)
            blue  = int(wgt1 * b1 + wgt2 * b2)

            new_pic.setColor(x, y, (red, green, blue))

    new_pic.show()
    return new_pic

p1 = Picture("../SampleImages/daylilies.jpg")
p2 = Picture("../SampleImages/wildColumbine.jpg")
p3 = simple_blend(p1, p2)

p4 = Picture("../SampleImages/muirWoods.jpg")
p5 = Picture("../SampleImages/peony.jpg")
p6 = blend2(p4, p5)

p4 = Picture("../SampleImages/muirWoods.jpg")
p5 = Picture("../SampleImages/peony.jpg")

p7 = weighted_blend(p4, p5, 0.0)
p8 = weighted_blend(p4, p5, 0.25)
p9 = weighted_blend(p4, p5, 0.5)
p10 = weighted_blend(p4, p5, 0.75)
p11 = weighted_blend(p4, p5, 1.0)

keep_windows_open()

