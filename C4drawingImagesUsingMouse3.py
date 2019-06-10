import cv2
import numpy as np

#################
### VARIABLES ###
#################

#true while mouse button down and false while mouse button up
drawing = False
ix,iy=-1,-1

################
### FUNCTION ###
################

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing

    # if event is left button down then assign ix and iy to mouse's current value
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    
    # if mouse is moving with button pressed then draw rectangle
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
        
    # if button is released, then set drawing to false and draw a final rectangle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)


#########################
### SHOWING THE IMAGE ###
#########################

img = np.zeros((512,512,3))

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:

    cv2.imshow('my_drawing',img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()

