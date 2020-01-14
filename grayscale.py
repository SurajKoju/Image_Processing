import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = im.imread('Opera-house.png')

color = grayscale(img)

plt.imshow(color, cmap = plt.get_cmap('gray'))



plt.savefig('in_greyscale.png')
plt.show()

