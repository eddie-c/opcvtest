import cv2
import numpy as np
import numpy
img = cv2.imread("sudoku.jpg",0)
# row,col,dimension = img.shape

img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,3)
th3 = cv2.medianBlur(th3,5)
cv2.imshow("th",th2)
cv2.imshow("th3",th3)
cv2.waitKey()
cv2.destroyAllWindows()

