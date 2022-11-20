import cv2

#cv2.imread -> 0= read in grayscall, 1= read in bgr
img = cv2.imread(r"C:\Users\zieba\Desktop\python\10appCourse\openCV\smallgray.png",1)
im2 = cv2.imwrite(r"C:\Users\zieba\Desktop\python\10appCourse\openCV\test.png", img)
print(img)
print(im2)
