#encoding:utf-8

import cv2
import numpy
# image = cv2.imread("F:\\123\\mu.png")#读取图像

image=cv2.imread( "4.png", 0 )
# cv2.namedWindow("image",cv2.WINDOW_NORMAL)

a = image[150, 100] 
rows, cols = image.shape
print rows
print cols
image[0:680,0:1080] = 255;
image[1600:1920,0:1080] = 255;
# cv2.imshow("image",image)#
cv2.waitKey(0)
for i in range(0,cols):
    for j in range(680,1600):
        b = image[j, i]
        if((b>a and b-a<22)or(b<a and a-b<22)or(b>143 and b-143<7)or(b<=143 and 143-b<7)):
            image[j, i] = 255
        else:
            image[j, i] = 0


# cv2.imshow("image",image)#显示读取的像素块
im2,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)
print contours

# cv2.imshow("im2",im2)

cv2.waitKey(0)