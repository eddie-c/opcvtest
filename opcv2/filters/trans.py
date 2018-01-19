import cv2
import numpy as np
import numpy
img = cv2.imread("3.png")
row,col,dimension = img.shape
dimfrom = np.float32([[50,50],[200,50],[50,200]])
dimto = np.float32([[10,100],[200,50],[100,250]])
m = cv2.getAffineTransform(dimfrom,dimto)
# m = cv2.getRotationMatrix2D((col*3/4,row/2),90,0.8)
img2 = cv2.warpAffine(img,m,(col*5,row*5))
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

