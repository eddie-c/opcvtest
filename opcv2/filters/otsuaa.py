import cv2
import numpy as np
import numpy
img = cv2.imread("noisy2.png",0)
# ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# blur = cv2.GaussianBlur(img,(5,5),0)
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# cv2.imshow("th2",th2)
cv2.imshow("th3",th3)

cv2.waitKey()
cv2.destroyAllWindows()

