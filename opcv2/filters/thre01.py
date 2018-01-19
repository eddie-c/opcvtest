import cv2
import numpy as np
import numpy
img = cv2.imread("gray.jpg")
row,col,dimension = img.shape
ret,thresh1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("th",thresh5)
cv2.waitKey()
cv2.destroyAllWindows()

