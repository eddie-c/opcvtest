import cv2
import numpy as np
kernel1 = np.ones((3,3),np.float32)/25
kernel2 = np.ones((5,5),np.float32)/25
img = cv2.imread("opencv_logo2.png")
dst1 = cv2.filter2D(img,-1,kernel1)
dst2 = cv2.filter2D(img,-1,kernel2)


# print kernel
cv2.imshow("th1",dst1)
cv2.imshow("th2",dst2)
cv2.waitKey()
cv2.destroyAllWindows()

