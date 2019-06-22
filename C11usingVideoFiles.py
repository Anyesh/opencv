import cv2
import time

cap = cv2.VideoCapture('mysupervideo.mp4')

if cap.isOpened() == False:
    print('file not found or wrong codec chosen')

while cap.isOpened():

    ret,frame = cap.read()

    if ret:

        #writer 40 frames per second

        time.sleep(1/40)

        cv2.imshow('frame',frame)

        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

