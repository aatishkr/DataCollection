# import the opencv library
import cv2
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=30/1 ! nvvidconv flip-method=0 ! video/x-raw, width=1280, height=720, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'

# define a video capture object
vid = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      
    # output the frame
    out.write(hsv) 
      
    # The original input frame is shown in the window 
    cv2.imshow('Original', frame)
  
    # The window showing the operated video stream 
    cv2.imshow('frame', hsv)
  
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()