import cv2
import numpy as np

################
### FUNCTION ###
################

# this function will take the parameters like event(what exactly is the movement)
# x and y are the current movements

def draw_circle(event,x,y,flags,param):

    # if the event is left button down draw a circle which will take the parameters.
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),5)

# this function gonna tell cv2 that on which window you have to do something.
cv2.namedWindow(winname='my_drawing')

# this command gonna tell cv2 that you have to map a funtion to window
cv2.setMouseCallback('my_drawing',draw_circle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = np.zeros((512,512,3),np.int8)

while True:

    cv2.imshow('my_drawing',img)

    if cv2.waitKey(10) & 0xFF==27:
        break

cv2.destroyAllWindows()