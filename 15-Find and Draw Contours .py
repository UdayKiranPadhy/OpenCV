# Countour is defined as the curve joining continous points which has the same colour
# used for object or shape detection 

from typing import Counter
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opencvlogo.jpg')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# For better accuracy we use binary image
ret , threshold = cv.threshold(imgray,220,255,0)
contours , hierarchy = cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# countiurs is a numpy array of all the points (x,y) of the countourrs
# hierarchy contains topology order
print("Number of Countours = " + str(len(contours)))

cv.drawContours(img,contours,-1,(0,255,0),3)

cv.imshow("Original image",img)
cv.imshow("Grey image",imgray)
cv.imshow("Threshold image",threshold)

cv.waitKey(0)
cv.destroyAllWindows()