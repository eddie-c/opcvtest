import cv2
import numpy as np
temp = cv2.imread('eye.jpg',0)
img2 = cv2.imread("a.jpg",0)
img3 = cv2.imread("a.jpg",cv2.IMREAD_UNCHANGED)
w,h = temp.shape[::-1]

res = cv2.matchTemplate(img2,temp,cv2.TM_CCOEFF_NORMED)

threshold = 0.99

loc = np.where(res>threshold)

a = loc[1]
b = loc[0]
for pt in zip(a,b):
    cv2.rectangle(img3,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow("sdf",img3)
cv2.waitKey()
cv2.destroyAllWindows()