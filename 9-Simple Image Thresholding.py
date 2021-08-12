import cv2 as cv
import numpy as np

img = cv.imread("gradient.jpg")

_,th1 = cv.threshold(img,150,255,cv.THRESH_BINARY)
# Similary Binary_INV,THresh_Trunc

cv.imshow('Image',img)
cv.imshow('th1',th1)

cv.waitKey(0)
cv.destroyAllWindows()