import cv2
import numpy as np

img =cv2.imread("3.png",cv2.IMREAD_UNCHANGED)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([13,1,143])
upper_blue=np.array([213,255,255])

mask=cv2.inRange(hsv,lower_blue,upper_blue)
res=cv2.bitwise_and(hsv,hsv,mask=mask)
cv2.imshow('a',res)
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,125)

# cv2.findContours()

cv2.imshow('b',thresh)
cv2.waitKey()
cv2.destroyAllWindows()