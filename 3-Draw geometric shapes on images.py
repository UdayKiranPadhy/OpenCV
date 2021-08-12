import cv2
import numpy
# img = cv2.imread('lena.jpg',1)

# We can also give image as numpy array
img  = numpy.zeros([512,512,3],numpy.uint8)

# cv2.imshow('Image',img)
# Note anything which u draw will update the original image , it doesnt return new image
lined_img = cv2.line(img,(0,0),(255,255),(255,0,0),10)
lined_img = cv2.arrowedLine(lined_img,(0,255),(255,255),(255,0,0),10)

lined_img = cv2.rectangle(lined_img,(384,0),(510,128),(255,0,0),10)
lined_img = cv2.circle(lined_img,(447,63),63,(0,0,255),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
text_img = cv2.putText(img,'Lena',(10,500),font,4,(0,255,0),10,cv2.LINE_AA)

cv2.imshow('text',text_img)
cv2.imshow('gg',lined_img)
# cv2.imshow('Image2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()