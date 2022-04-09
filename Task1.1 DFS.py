import numpy as np
from collections import deque
import cv2
import time
#finding a probability between 20 and 30 to have an obstacle
prob=np.random.randint(20,31)  #as range is [Low,High)
print(4*prob)

#We will generate a matrix of size 20*20 and then resize it to 400*400
#Since the number of pixels in a 20*20 matrix is 400, The total number of obstacle pixels will be 4*prob

#generating a 20*20 matrix
img=np.full((20,20),255).astype(np.uint8)
count=0
while(count<4*prob):
    i=np.random.randint(0,20)
    j=np.random.randint(0,20)
    if(img[i,j]!=0):    #checking for repitition
        count+=1
        img[i,j]=0


#resizing it to a 400*400 matrix
img=cv2.resize(src=img,dsize=(40,40),interpolation=cv2.INTER_AREA)

#adding 2 random grey pixels to the maze
n=0
while(n<2):
    i=np.random.randint(0,40)
    j=np.random.randint(0,40)
    if(img[i,j]==255):    #checking for a white pixel
        n+=1
        img[i,j]=128
        print(j,i)
m=i         #taking the second grey pixel formed to be the starting point
n=j
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
            print("cant move", j, i)
            
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
            cv2.waitKey(50)
        exit()
            
begin=time.time()
dfs(m,n)

cv2.waitKey(0)
cv2.destroyAllWindows