import cv2
import numpy as np
temp = cv2.imread('jump2.jpg')
temp2 = temp.copy()
temp2 = cv2.cvtColor(temp2,cv2.COLOR_BGR2GRAY)
temp2 = cv2.GaussianBlur(temp2,(3,3),0)
canny1 = cv2.Canny(temp,100,255)
row,col = temp2.shape

cv2.imshow("canny",canny1)
image,contours,hierachy = cv2.findContours(canny1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(temp,contours,-1,(0,255,0),3)
# print hierachy
for cnt in contours:
    # epsilon = 0.01 * cv2.arcLength(cnt, True)
    # approx = cv2.approxPolyDP(cnt, epsilon, True)
    # cv2.drawContours(temp, [cnt], -1, (0, 255, 0), 3)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(temp,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("ori",temp)
cv2.waitKey()
cv2.destroyAllWindows()