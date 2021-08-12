import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img2 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.rectangle(img2,(125,0),(250,500),(255,255,255),-1)
cv2.imshow("image",img1)
cv2.imshow('image2',img2)

bitAnd = cv2.bitwise_and(img1,img2)
# similary bitwise_or and bitwise_xor too

cv2.waitKey(0)
cv2.destroyAllWindows()