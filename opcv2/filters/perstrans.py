import cv2
import numpy as np
import numpy
img = cv2.imread("3.png")
row,col,dimension = img.shape
dimfrom = np.float32([[13,40],[64,160],[140,40],[169,201]])
dimto = np.float32([[0,0],[0,200],[200,0],[120,200]])
m = cv2.getPerspectiveTransform(dimfrom,dimto)
# m = cv2.getRotationMatrix2D((col*3/4,row/2),90,0.8)
img2 = cv2.warpPerspective(img,m,(col,row))
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

