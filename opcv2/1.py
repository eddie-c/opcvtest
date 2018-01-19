import cv2
import numpy as np

img = cv2.imread('1.png',cv2.IMREAD_COLOR)
kernel = np.ones((6,6),np.uint8)
ersion = cv2.erode(img,kernel,iterations=1)
cv2.imshow('ersion',ersion)
cv2.waitKey()
cv2.destroyAllWindows()