import cv2

faceDefault = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeDefault = cv2.CascadeClassifier("haarcascade_eye.xml")
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDefault.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray = imgGray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeDefault.detectMultiScale(roi_gray, 1.1, 2, minSize=(40,40), maxSize=(50,50))
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),1)

    cv2.imshow('Face',frame)
    cv2.imshow('roi', roi_color)
    print(eyes)

    exitKey = cv2.waitKey(1)

    if exitKey == ord('q'):
        break



video.release()    
cv2.destroyAllWindows()
