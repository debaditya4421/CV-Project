import cv2
import numpy as np

img=cv2.imread('map1.2.png',0)
b=880
a=145
d=359
c=563
n,m=img.shape
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
img[a][b] = 255
img[c][d] = 255
img1 = np.full((n, m), 0)
#img2 = np.full((n, m), 255)
img1[a][b] = 1
add = 5
d1 = 25

def step(k):
    global d1
    d1 = 25
    for i in range(n):
        for j in range(m):
            if img1[i][j] == k:
                # global d1
                d1 = 20
                if (i > 0) and (img1[i - 1][j] == 0) and (img[i - 1][j] == 255):
                    img1[i - 1][j] = k + 1
                if (j > 0) and (img1[i][j - 1] == 0) and (img[i][j - 1] == 255):
                    img1[i][j - 1] = k + 1
                if (i + 1 < n) and (img1[i + 1][j] == 0) and (img[i + 1][j] == 255):
                    img1[i + 1][j] = k + 1
                if (j + 1 < m) and (img1[i][j + 1] == 0) and (img[i][j + 1] == 255):
                    img1[i][j + 1] = k + 1
    if d1 == 25:
        global add
        add = 10
k = 0
while add == 5:
    k = k + 1
    step(k)

print(k)
print(img1[a][b])
cv2.namedWindow('NewImage', cv2.WINDOW_NORMAL)

p = img1[c][d]
#img2[c][d] = 0
def path1(r,s,p):
    global c
    global d
    if (r > 0) and (img1[r - 1][s] == p - 1):
        img[r - 1][s] = 127
        c = r-1
        d = s
        cv2.imshow('NewImage', img)
        cv2.waitKey(100)

    elif (s > 0) and (img1[r][s - 1] == p - 1):
        img[r][s - 1] = 127
        c = r
        d = s - 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(100)
    elif (r + 1 < n) and (img1[r + 1][s] == p - 1):
        img[r + 1][s] = 127
        c = r + 1
        d = s
        cv2.imshow('NewImage', img)
        cv2.waitKey(100)
    elif (s + 1 < m) and (img1[r][s + 1] == p - 1):
        img[r][s + 1] = 127
        c = r
        d = s+1
        cv2.imshow('NewImage', img)
        cv2.waitKey(100)
while p>1:
    path1(c,d,p)
    p = p-1

cv2.waitKey(0)
cv2.destroyAllWindows()