import cv2

def draw_circle(event,x,y,flags,param):

    global center,clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center =(x,y)
        clicked = False

    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

center = (0,0)
clicked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow(winname='Test')

cv2.setMouseCallback('Test',draw_circle)

while True:
    ret,frame = cap.read()

    if clicked:
        cv2.circle(frame,center,50,(255,0,0),thickness=5)

    cv2.imshow('Test',frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()