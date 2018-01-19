import cv2
import numpy as np
img = cv2.imread("1.png",0)
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cont = contours[0]
M = cv2.moments(cont)
# area = cv2.contourArea(cont)
# print area
#
# length = cv2.arcLength(cont,True)
# print length

epsilon = 0.01*cv2.arcLength(cont,True)
approx = cv2.approxPolyDP(cont,epsilon,True)

print approx

img = cv2.drawContours(image,approx,0,(100,250,100),10)
# print M
# cx = int(M['m10']/M['m00'])
# print cx
# cy = int(M['m01']/M['m00'])
# print cy
cv2.imshow("th7",img)
cv2.waitKey()
cv2.destroyAllWindows()
