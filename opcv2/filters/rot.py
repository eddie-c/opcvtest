import cv2
import numpy as np
import numpy
img = cv2.imread("3.png")
row,col,dimension = img.shape
m = cv2.getRotationMatrix2D((col*3/4,row/2),90,0.8)
img2 = cv2.warpAffine(img,m,(int(col*0.8),int(row*0.8)))
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

