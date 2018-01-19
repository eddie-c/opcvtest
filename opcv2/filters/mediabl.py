import cv2
import numpy as np
import numpy
img = cv2.imread("noise.png",0)
img = cv2.medianBlur(img,5)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()

