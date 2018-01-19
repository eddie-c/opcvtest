import cv2
import numpy as np
# img = cv2.imread("graf3.png")
# kernel = np.ones((5,5),np.uint8)
A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
cv2.imshow("123",gpA[5])
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    # cv2.imshow("ge" + str(i), GE)
    L = cv2.subtract(gpA[i-1],GE)
    # cv2.imshow("l" + str(i), L)
    lpA.append(L)


lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

ls_ = LS[0]

# cv2.imshow("l0", LS[0])
# cv2.imshow("l1", LS[1])

for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    # cv2.imshow("th"+str(i), ls_)
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

# cv2.imshow("th7",real)

ori = A.copy()
gpA = [ori]
G = cv2.pyrDown(ori)
# cv2.imshow("th1",ori)
# cv2.imshow("th7",G)
cv2.waitKey()
cv2.destroyAllWindows()
