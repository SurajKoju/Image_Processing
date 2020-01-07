from PIL import Image as im, ImageDraw

img = im.open('live.png').convert("LA")

img_draw = ImageDraw.Draw(img)
img_draw.text((100,250),'SURAJ KOJU',fill='black')

pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        x,y = pixels[i,j][0],pixels[i,j][1]
        x,y = abs(x-255), abs(y-255)
        pixels[i,j] = (x,y)

img.show()