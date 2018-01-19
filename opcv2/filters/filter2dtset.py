import cv2
import numpy as np
import numpy
img = cv2.imread("2.jpg")
kernel = np.array([[0,-1,0],
          [-1,5,-1],
          [0,-1,0]])
# kernel = [[0,-1,0],
#           [-1,5,-1],
#           [0,-1,0]]
a,b,c = img.shape
print a,b,c

outimg = cv2.filter2D(img,-1,kernel)
cv2.imwrite("outimg.jpg",outimg)
