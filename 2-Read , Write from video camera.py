import cv2

# If you want to read from a video file u can enter the file name
cap = cv2.VideoCapture(1)

# For saving the video
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# out = cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))
# 30 is for frames per second
# tuple is height and width 


while cap.isOpened():
    ret , frame = cap.read()

    # Returns The Height and Width of the frame
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # Writes in the video Writer
    # out.write(frame)


    # To convert to gray scale image
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame',gray)
    
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break;


cap.release()
# out.release()
cv2.destroyAllWindows()