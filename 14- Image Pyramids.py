
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
# lr = cv.pyrDown(img)

# hr = cv.pyrUp(img)



cv.imshow("Original image",img)
# cv.imshow("pyrDown image",lr)
# cv.imshow("pyrUP image",hr)
cv.waitKey(0)
cv.destroyAllWindows()