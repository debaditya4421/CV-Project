import cv2
import numpy as np
from collections import deque
import time

img=cv2.imread('homemap.jpeg', 0)
x,y=img.shape
for i in range (x):
    for j in range(y):
        if img[i,j]<243:
            img[i,j]=0
        else:
            img[i,j]=255



kernel = np.ones((2,2), np.uint8)
 

img = cv2.dilate(img, kernel, iterations=1)

m,n=(8,23)
c,d=(51,26)

img[c,d]=128       

print(m,n)
img[m,n]=200
x,y=img.shape
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
stack1=deque()
stack2=deque()
q=0
def dfs(i,j):
    global q
    if img[i,j]!=128:
        while(q<1):
            img[i,j]=127
            stack1.append(i)
            stack2.append(j)
            cv2.imshow('Image', img)
            cv2.waitKey(5)
            if(j-1)>=0:
                if(img[i,j-1]==128):
                    print("complete")
                    dfs(i,j-1)
                elif(img[i,j-1]==255):
                    dfs(i,j-1)
            if(j+1<y):
                if(img[i,j+1]==128):
                    print("complete")
                    dfs(i,j+1)
                elif(img[i,j+1]==255):
                    dfs(i,j+1)
            if(i+1<x):
                if(img[i+1,j]==128):
                    print("complete")
                    dfs(i+1,j)
                elif(img[i+1,j]==255):
                    dfs(i+1,j)
            if(i-1)>=0:
                if(img[i-1,j]==128):
                    print("complete")
                    dfs(i-1,j)
                elif(img[i-1,j]==255):
                    dfs(i-1,j)
            
            stack1.pop()
            stack2.pop()
            
            break
    else:
        q=2
        print("complete")
        l=len(stack1)
        print("distance=", l)
        end=time.time()
        print("time=",end-begin)
        for k in range(l):
            img[stack1.pop(),stack2.pop()]=200
            cv2.imshow('Image', img)
            cv2.waitKey(20)
        cv2.waitKey(0)
        exit()
            
begin=time.time()
dfs(m,n)

cv2.waitKey(0)
cv2.destroyAllWindows