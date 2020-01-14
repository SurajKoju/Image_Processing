# load and display an image with Matplotlib

import matplotlib.pyplot as plt
import matplotlib.image as im

# load image as pixel array
img = im.imread('grayscale.png')

# summarize shape of the pixel array
print(img)
print(img.shape)

# display the array of pixels as an image
plt.imshow(img)
plt.show()
