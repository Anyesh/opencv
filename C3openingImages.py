import cv2

img = cv2.imread('imgs/puppy.jpg')

while True:

    #open a new slide named puppy and having image img.
    cv2.imshow('puppy',img)

    #wait for 1 milisecond and see if the key pressed by keyboared is esc.
    if cv2.waitKey(1) & 0xFF ==27:
        break

#destroy all windows which represents opencv
cv2.destroyAllWindows()