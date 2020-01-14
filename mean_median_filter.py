import numpy as mp
import cv2
from matplotlib import pyplot as plt
from PIL import image, ImageFilter

image2 = cv2.imread('images.png')
image2 = cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)
figure_size = 9
new_image = cv2.blur(image2,(figure_size, figure_size))
plt.figure(figuresize=(11,6))
plt.subplot(121),plt.imshow(image2, cmap='gray'), plt.title(original)
plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(new_image,cmap='gray'), plt.title(mean_filter)
plt.xticks([]), yticks([])
plt.show()

# MEDIAN FILTER

import cv2 
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('new.jpg',cv2.COLOR_BGR2GRAY)
cv2.imshow("input", image)
image = cv2.medianBlur(image,5)
cv2.imshow("output",image)
