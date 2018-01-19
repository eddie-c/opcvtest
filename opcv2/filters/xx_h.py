import cv2
import numpy as np
img = cv2.imread("a.jpg",cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
# img = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# img[:,:,[0]]
img2 = cv2.bitwise_not(img)
# img2 = cv2.morphologyEx(img,cv2.MORPH_ERODE,kernel)
img2 = cv2.flip(img2,1)
# cv2.imwrite("aout.jpg",img2)

cv2.imshow("th7",img2)
cv2.waitKey()
cv2.destroyAllWindows()