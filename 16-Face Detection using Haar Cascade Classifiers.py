import cv2 # Import Open cv Libray

# Ignore all the warnings
import warnings
warnings.filterwarnings("ignore")

# Create a cascade Classifier
# You can also find many more classifiers online https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Create a video Capture Object in order to capture Frames
# If you have single camera use index 0 inside the function. 
# If you have multiple camera's you can use second camera by incrementing the index to 1 , 2 ,...
videoStreamObject = cv2.VideoCapture(1)

# Just for unique naming of captured photos
image_index = 0

# Continously read Video while the Camera is used
while videoStreamObject .isOpened():

    # The VideoCapture object has a method read() ,which when executed starts accessing the camera stream and returns a tuple.
    # The first value is a Boolean value representing whether a frame is captured correctly or not.
    # The second value is the captured frame, which is basically a numpy array.
    ret , frame = videoStreamObject.read()

    if ret and frame is not None:

        # Frame is shown inverted by default so we flip it
        frame=cv2.flip(frame, 1)

        # Find all the faces present in the Frame using Detect Multi Select
        faces = face_cascade.detectMultiScale(frame,1.1,4)

        # This waitKey() method takes an argument of type integer denoting the number of seconds to wait for the key press.
        k = cv2.waitKey(1) & 0xFF 
        if k == ord('q'):
            break
        elif k == ord('s'):
            cv2.imwrite('images/c'+str(image_index)+'.jpg',frame)
            image_index += 1

        # Draw a rectangle around the face if Present
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        # To display this frame on a window we use the opencv library’s imshow() method. 
        # The imshow() method takes in two arguments, the first one is the Title to be displayed 
        # on the window, this argument is a string and the second argument is the frame to be displayed.
        cv2.imshow('img',frame)

        if k == ord('y'):
            cv2.imwrite('images/c'+str(image_index)+'_withframe.jpg',frame)
            image_index+=1

    else:
        break

videoStreamObject.release()
cv2.destroyAllWindows()