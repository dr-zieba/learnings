import cv2
import imutils
import numpy as np

img = cv2.imread("auto.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,168])
upper_white = np.array([172,111,255])
mask = cv2.inRange(hsv,lower_white,upper_white)

cnts,_ = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(cnts)

for contour in cnts:
    if cv2.contourArea(contour) < 2000:
        continue
    else:
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
        roi_mask = mask[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
                 


cv2.imshow("IMG",img)
cv2.imshow("IMGE",roi_color)

exitKey = cv2.waitKey(1)

if exitKey == ord('q'):
    cv2.destroyAllWindows()


for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx)==4:
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)


