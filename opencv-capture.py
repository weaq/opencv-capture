import numpy as np
import cv2, time

# Read video from source
cap = cv2.VideoCapture(0)
# Set video ratio 16:9
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 405)

while(True):
    # Capture frame by frame
    ret, frame = cap.read()

    # Wait for keyboard press
    k = cv2.waitKey(1)
    # Press q to exit
    if k == ord('q'):
        break
    # Press s to save
    if k == ord('s'):
        timestr = time.strftime("%Y%m%d%H%M%S")
        # Write capture to file
        cv2.imwrite('img/' + timestr + '.jpg',frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show image
    cv2.imshow('frame',frame)

# Release capture when done
cap.release()
cv2.destroyAllWindows()
