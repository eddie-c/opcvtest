# import cv2
# import numpy as np
# img = cv2.imread("star.jpg")
# mean = cv2.mean(img)
# # print mean
# ret,thresh = cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
# image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print contours[2]
# print contours[2][:,:,0].argmin()
# print contours[2][50][0]
# print contours[2][contours[2][:,:,0].argmin()][0]
# print contours[2][contours[2][:,:,0].argmax()][0]
# x,y,w,h = cv2.boundingRect(contours[0])
# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# boxpoint = cv2.minAreaRect(contours[2])
# box = cv2.boxPoints(boxpoint)
# box = np.int0(box)
# img = cv2.drawContours(image,[box],0,(255,255,255),3)
#
# (x,y),radius = cv2.minEnclosingCircle(contours[2])
# center = (int(x),int(y))
# radius = int(radius)
# image = cv2.circle(image,center,radius,(255,255,255),3)


# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# hull = cv2.convexHull(contours[0],returnPoints=False)
# print cv2.isContourConvex(contours[0])
# print hull
# cv2.imshow("th7",image)
# cv2.waitKey()
# cv2.destroyAllWindows()
import cv2
import numpy as np
img = cv2.imread('star.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,cv2.THRESH_BINARY)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
# print defects
# print defects.shape
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    print cnt[s]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()