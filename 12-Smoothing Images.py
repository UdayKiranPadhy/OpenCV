# There are many types of Filter like Homogenous Filter Gaussion Filter etc.
# Mainly means Bluring

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('opencvlogo.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5),np.float32)/25

# Homogenous Filter
dst = cv2.filter2D(img,-1,kernal)
blur = cv2.blur(img,(5,5))

# Gaussian filter (More better) , mostly used to remove high Frequency Noise
gaussion = cv2.GaussianBlur(img,(5,5),0)

# Median Fikter , best for Salt and pepper Noise (reflections due to light)
median = cv2.medianBlur(img,5)

titles = ['image','2D Convolution','Blur','gaussionBlur','Medianblur']
images = [img,dst,blur,gaussion,median]

for i in range(len(images)):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()