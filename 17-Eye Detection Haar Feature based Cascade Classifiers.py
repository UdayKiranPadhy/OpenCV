import cv2 # Import Open cv Libray

# Ignore all the warnings
import warnings
warnings.filterwarnings("ignore")

# Create a cascade Classifier
# You can also find many more classifiers online https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


# Create a video Capture Object in order to capture Frames
# If you have single camera use index 0 inside the function. 
# If you have multiple camera's you can use second camera by incrementing the index to 1 , 2 ,...
videoStreamObject = cv2.VideoCapture(1)

# Continously read Video while the Camera is used
while videoStreamObject.isOpened():

    # The VideoCapture object has a method read() ,which when executed starts accessing the camera stream and returns a tuple.
    # The first value is a Boolean value representing whether a frame is captured correctly or not.
    # The second value is the captured frame, which is basically a numpy array.
    ret , frame = videoStreamObject.read()

    if ret and frame is not None:

        # Frame is shown inverted by default so we flip it
        frame=cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # Find all the faces present in the Frame using Detect Multi Select
        faces = face_cascade.detectMultiScale(frame,1.1,4)

        # This waitKey() method takes an argument of type integer denoting the number of seconds to wait for the key press.
        k = cv2.waitKey(1) & 0xFF 
        if k == ord('q'):
            break

        # Draw a rectangle around the face if Present
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            # For Detecting eyes our region of interest becomes face
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_color,1.1,4)

            for ex , ey , ew , eh in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

        # To display this frame on a window we use the opencv library’s imshow() method. 
        # The imshow() method takes in two arguments, the first one is the Title to be displayed 
        # on the window, this argument is a string and the second argument is the frame to be displayed.
        cv2.imshow('img',frame)

    else:
        break

videoStreamObject.release()
cv2.destroyAllWindows()