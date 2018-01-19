import cv2
import numpy as np

im1 = cv2.imread("2.jpg")
im1 = im1[0:173,0:198]
a,b,c = im1.shape
print a,b,c
im2 = cv2.imread("3.png")

im2 = im2[0:173,0:198]

a,b,c = im2.shape
print a,b,c
im3 = cv2.addWeighted(im1,0.9,im2,0.1,-10)
# im3[:,:,2] = 0
print "::"
print im3
# print im3[:,:,2]
# print "============"
# print im3[:,:][2]
# print "::"
# print im3[20,20][2]

cv2.imwrite("im3.png",im3)
