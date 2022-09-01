# import the opencv library
import cv2
import datetime
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=30/1 ! nvvidconv flip-method=0 ! video/x-raw, width=1280, height=720, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'

# define a video capture object
vid = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 6, (frame_width,frame_height))
x = 250
while(x > 0):
	x  = x-1
	ret, frame = vid.read()
	out.write(frame)
	now = datetime.datetime.now()
	print(now)
	cv2.imshow('Original', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()