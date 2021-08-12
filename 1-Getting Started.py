import cv2

# Note it wont raise error if image File is not found
# The way you need to check is to print the image if it return 
# a numpy array then is means the image has been read
image = cv2.imread('Lena.jpg')

# by default the flag parameter is 1 which stands for color mode
# We can also get a Black and white mode by using 0 flag
# image = cv2.imread('Lena.jpg',0)
# image = cv2.imread('Lena.jpg',1)
# image = cv2.imread('Lena.jpg',-1)


# CV2 imshow is used for showing the image
# parameter 1 window name followed by the image read (numpy arrray)
cv2.imshow('image',image)

# Will wait until we complete watching it
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image)


# We can also write down the image in a jpg or png file and save
cv2.imwrite('lena_copy.png',image)


# We can also capture the waitKey by assigning it to a variable
# k = cv2.waitKey(0)
# if k == ord('s'):
#     cv2.imwrite('lena_save.png',image)