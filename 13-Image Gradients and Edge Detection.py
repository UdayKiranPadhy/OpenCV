# Image Gradients are used to detect edges. It is the directional change
# in the intensity of the image

# Image Gradient
# Lapsion Derivative
#  Sobal X
#  Sobal Y

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.jpg',cv.IMREAD_GRAYSCALE)

# We are using 64nit Float due to negative slope occured due to transforming to Black
lap = cv.Laplacian(img,cv.CV_64F,ksize=1)
# Take the absolute value and convert it into non negative number
lap = np.uint8(np.absolute(lap))

sobel_x = cv.Sobel(img,cv.CV_64F,1,0)
sobel_x = np.uint8(np.absolute(sobel_x))

sobel_y = cv.Sobel(img,cv.CV_64F,0,1)
sobel_y = np.uint8(np.absolute(sobel_y))

canny = cv.Canny(img,70,255)

# Combine both SobelX and Sobel Y

sobelCombined = cv.bitwise_or(sobel_x,sobel_y)

titles = ['image','Lapsion Methon','SobelX','SobelY','Combined','Canny']
images = [img,lap,sobel_x,sobel_y,sobelCombined,canny]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()