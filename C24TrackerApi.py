import cv2

def ask_for_tracker():
    print("Welcome! what tracker api would you like to use?")
    print("Enter 0 for Boosting:")
    print("Enter 1 for MIL:")
    print("Enter 2 for KCF:")
    print("Enter 3 for TLD:")
    print("Enter 4 for MedianFlow:")

    choice = input("Please select your tracker: ")

    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    elif choice == '1':
        tracker = cv2.TrackerMIL_create()
    elif choice =='2':
        tracker = cv2.TrackerKCF_create()
    elif choice =='3':
        tracker = cv2.TrackerTLD_create()
    elif choice =='4':
        tracker = cv2.TrackerMedianFlow_create()

    return tracker

tracker = ask_for_tracker()

cap = cv2.VideoCapture(0)

ret,frame = cap.read()
roi = cv2.selectROI(frame,False)
ret = tracker.init(frame,roi)

while True:

    ret,frame = cap.read()
    success, roi = tracker.update(frame)

    (x,y,w,h) = tuple(map(int,roi))

    if success:
        p1 = (x,y)
        p2 = (x+w,y+h)
        cv2.rectangle(frame,p1,p2,(0,255,0),3)

    else:
        cv2.putText(frame,"Failure",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

    cv2.putText(frame,'tracker',(20,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)

    cv2.imshow('frame',frame)

    if cv2.waitKey(10) & 0xFF==27:
        break

cv2.destroyAllWindows()
cap.release()
