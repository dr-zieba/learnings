import cv2, time

video = cv2.VideoCapture(0)
firstFrame = None

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    
    if firstFrame is None:
        firstFrame=gray
        continue

    deltaFrame = cv2.absdiff(firstFrame,gray)
    threshFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame, None, iterations=2)

    (cnts,_) = cv2.findContours(threshFrame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 2000:
            continue
        else:
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('frame',gray)
    cv2.imshow('firstFrame', deltaFrame)
    cv2.imshow('Thresh', threshFrame)
    cv2.imshow('Countours',frame)
    
    exitKey = cv2.waitKey(1)

    if exitKey == ord('q'):
        break

video.release()    
cv2.destroyAllWindows()

