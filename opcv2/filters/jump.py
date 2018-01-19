import cv2
import numpy as np
temp = cv2.imread('jump2.jpg')
temp2 = temp.copy()
temp2 = cv2.cvtColor(temp2,cv2.COLOR_BGR2GRAY)
cv2.imshow("xx",temp2)
temp2 = cv2.GaussianBlur(temp2,(5,5),0)
# temp2 = cv2.medianBlur(temp2,3)
# canny1 = cv2.Canny(temp2,100,255)
row,col = temp2.shape

ret,thre1 = cv2.threshold(temp2,190,255,cv2.THRESH_BINARY)
# cv2.imshow("1",canny1)

for i in range(0,row):
    for j in range(0,col):
        if temp2[i][j] > 131 and temp2[i][j] < 154:
            temp2[i][j] = 255
        else:
            temp2[i][j] = 0

kernel = np.ones((5,5),np.uint8)
temp3 = cv2.morphologyEx(temp2,cv2.MORPH_ERODE,kernel)
target = cv2.bitwise_xor(thre1,temp2)
# target2 = cv2.bitwise_not(target)

target = cv2.morphologyEx(target,cv2.MORPH_CLOSE,kernel)
target = cv2.morphologyEx(target,cv2.MORPH_OPEN,kernel)
# target = cv2.morphologyEx(target,cv2.MORPH_ERODE,kernel)

cv2.imshow("target",target)
image,contours,hierachy = cv2.findContours(target,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print hierachy
cv2.drawContours(temp,contours,-1,(0,255,0),1)
for cnt in contours:
    # cnt = contours[2]
    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)
    # print defects
    # print defects.shape
    try:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            print cnt[s]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            cv2.line(temp, start, end, [0, 255, 0], 2)
            cv2.circle(temp, far, 5, [0, 0, 255], -1)
    except:
        pass

cv2.imshow("ori",temp)

# cv2.findContours(target2,cv2.)



cv2.waitKey()
cv2.destroyAllWindows()