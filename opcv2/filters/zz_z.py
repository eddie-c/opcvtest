import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("zz.jpg",0)
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist,bins = np.histogram(img.ravel(),256,[0,256])
print bins
# print hist
plt.hist(img.ravel(),256,[0,256])
plt.show()


# equ = cv2.equalizeHist(img)
# res = np.hstack((img,equ))
# cv2.imshow("th7",res)
# cv2.waitKey()
# cv2.destroyAllWindows()
