import time
from random import randrange

from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def get_rand_bg():
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)

    pic = Picture(100, 100)

    color = (r, g, b)

    pic.setAllPixels(color)

    return pic


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()

