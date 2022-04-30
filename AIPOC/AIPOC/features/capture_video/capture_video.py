
import time
 
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
 
def capturevideo():
    # Are we using the Pi Camera?
    count = 0
    # usingPiCamera = True
    # Set initial frame size.
    frameSize = (600, 600)
    
    # Initialize mutithreading the video stream.
    vs = VideoStream(src=0, resolution=frameSize,
            framerate=32).start()
    # Allow the camera to warm up.
    time.sleep(2.0)
    
    timeCheck = time.time()
    while True:
        # Get the next frame.
        frame = vs.read()
        
        # If using a webcam instead of the Pi Camera,
        # we take the extra step to change frame size.
        # if not usingPiCamera:
        frame = imutils.resize(frame, width=frameSize[0])
    
        # Show video stream
        cv2.imshow('orig', frame)
        key = cv2.waitKey(1) & 0xFF
        count+=1
        print(count)
        # if the `q` key was pressed, break from the loop.
        if count == 5000:
            break
        
        print(1/(time.time() - timeCheck))
        timeCheck = time.time()
    
    # Cleanup before exit.
    cv2.destroyAllWindows()
    vs.stop()
