def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x,y) in small_pic:
        color = small_pic.getColor(x,y)
        target_x = start_x + x
        target_y = start_y + y

        big_pic.setColor(target_x, target_y, color)