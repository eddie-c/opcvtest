import cv2
import numpy as np
img = cv2.imread("star2.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img = cv2.drawContours(image,contours,0,(0,255,0),3)

cv2.imshow("th7",img)
cv2.waitKey()
cv2.destroyAllWindows()
