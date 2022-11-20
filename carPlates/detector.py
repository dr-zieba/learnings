import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\zieba\AppData\Local\Tesseract-OCR\tesseract.exe'

img = cv2.imread("auto3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.bilateralFilter(gray, 11, 17, 17)
_,threshFrame = cv2.threshold(gray, 170, 220, cv2.THRESH_BINARY_INV)
#edged = cv2.Canny(gray, 30, 200)
#median = cv2.medianBlur(gray, 5)


cnts,_ = cv2.findContours(threshFrame.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
count=0
for c in cnts:
    if cv2.contourArea(c) < 100:
        continue
    else:
        #cv2.drawContours(img, c, -1, (0,255,0), 3)
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),1)
        
        roi_color = img[y:y+h, x:x+w]
        roi_colorG = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
        _,roi_colorF = cv2.threshold(roi_colorG, 127, 255, cv2.THRESH_BINARY_INV)
        
        cv2.imwrite("IMGF"+str(count)+".jpg",roi_colorF)
        text = tess.image_to_string("IMGF"+str(count)+".jpg", config='-l eng --oem 3 --psm 12')
        if len(text) < 9 and text:
            print("Detected Number is:",text)
        count=count+1



cv2.imshow("IMG",img)
cv2.imshow("IMGG",gray)
cv2.imshow("IMGF",threshFrame)

