import cv2
import numpy as np
img = cv2.imread("sudoku.jpg",0)
img = cv2.Laplacian(img,0)
# img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
sobx = cv2.Sobel(img,0,1,0,ksize=5)
sobx = cv2.Sobel(img,-1,0,1,ksize=5)
cv2.imshow("th7",img)
cv2.imshow("th7",sobx)
cv2.waitKey()
cv2.destroyAllWindows()
