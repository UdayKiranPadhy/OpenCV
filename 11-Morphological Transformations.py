# Morphological transformation can be applied only on Binary Images

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8)

# Dilate will try to remove black spots inside white boxes using kernal box
# iterations is optional parameter more the kernal size more we lose the black
dilatation = cv2.dilate(mask,kernal,iterations=2)

# Removes the bounderies
erosion = cv2.erode(mask,kernal)

# You can try many more like morphologicalEX , opening , closing


titles = ['image','mask','dilate','erosion']
images = [img,mask,dilatation,erosion]

for i in range(len(images)):
    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()