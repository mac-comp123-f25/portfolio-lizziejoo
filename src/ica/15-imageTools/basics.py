from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic = Picture("../SampleImages/mightyMidway.jpg")

width = pic.getWidth()
height = pic.getHeight()

num_pixels = width * height
print("Width:", width)
print("Height:", height)
print("Number of pixels:", num_pixels)

copy_pic = pic.copy()

# Step 5: Define the color red in RGB
red = (255, 0, 0)

copy_pic.setColor(0, 0, red)

copy_pic.setColor(width - 1, 0, red)

copy_pic.setColor(0, height - 1, red)

copy_pic.setColor(width - 1, height - 1, red)

copy_pic.save("../SampleImages/mightyMidway-redCorners.jpg")

copy_pic.show()
copy_pic.explore()

keep_windows_open()





