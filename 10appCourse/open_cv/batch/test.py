import cv2

img = cv2.imread(r"open_cv\batch\galaxy.jpg",1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
resized = cv2.resize(img, (200,200))
cv2.imshow("re", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("gal_resized.jpg", resized)