import cv2
import numpy as np
temp = cv2.imread('eye.jpg',0)
img2 = cv2.imread("a.jpg",0)
img3 = cv2.imread("a.jpg",cv2.IMREAD_UNCHANGED)
w,h = temp.shape[::-1]
methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF'
            ,'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img,temp,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(img3,top_left,bottom_right,(255,255,255),2)

    cv2.imshow("th7",img3)
    cv2.waitKey()
    cv2.destroyAllWindows()