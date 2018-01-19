#encoding:utf-8

import cv2
from random import randint
import numpy
# image = cv2.imread("5.png")#读取图像

image=cv2.imread( "5.png", cv2.IMREAD_COLOR )
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

a = image[150, 100]
print image[155,100]
for i in range(0,len(image)):
    for j in range(0,len(image[0])):
        # print image[i,j]
        if(image[i,j][2] > 125 and image[i,j][2] <= 167 and
                   image[i, j][1] > 125 and image[i, j][1] <= 160 and
                   image[i, j][0] > 140 and image[i, j][0] <= 160):
            image[i,j] = [randint(a[0]-30,a[0]),randint(a[1]-30,a[1]),randint(a[2]-30,a[2])]


# print a
# rows, cols = image.shape
# print rows
# print cols
# image[0:680,0:1080] = 255;
# image[1600:1920,0:1080] = 255;
cv2.imshow("image",image)#
cv2.waitKey(0)
# for i in range(0,cols):
#     for j in range(680,1600):
#         b = image[j, i]
#         if((b>a and b-a<22)or(b<a and a-b<22)or(b>143 and b-143<7)or(b<=143 and 143-b<7)):
#             image[j, i] = 255
#         else:
#             image[j, i] = 0


# cv2.imshow("image",image)#显示读取的像素块
cv2.waitKey(0)
