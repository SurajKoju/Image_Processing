import numpy as np
from PIL import Image as im, ImageDraw

o_image = im.open('images.png').convert("LA")
row = o_image.size[0]
col = o_image.size[1]
gamma1 = 5
result_img1 = im.new("L", (row, col))



for x in range(1 , row):
    for y in range(1, col):
        value = pow(o_image.getpixel((x,y))[0]/255,(1/gamma1))*255
        if value >= 255 :
            value = 255
        result_img1.putpixel((x,y), int(value))
o_image.show()
result_img1.show()