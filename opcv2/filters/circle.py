import cv2
import numpy as np
import numpy
img = cv2.imread("logo.png")
print img
# img = cv2.medianBlur(img,5)
a = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print a
# img = cv2.Canny(img,150,200)
# cv2.imshow("3",img)
# img2 = cv2.imread("logo.png")
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,None,50,30,40,500)
# print circles
# # circles = np.uint16(np.round(circles))
#
# for i in circles[0,:]:
#     cv2.circle(img2,(i[0],i[1]),i[2],(0,0,0),2)
#
#
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

