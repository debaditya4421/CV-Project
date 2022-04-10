import cv2
import numpy as np
import time

img=cv2.imread('homemap.jpeg', 0)
n,m=img.shape
for i in range (n):
    for j in range(m):
        if img[i,j]<243:
            img[i,j]=0
        else:
            img[i,j]=255



kernel = np.ones((2,2), np.uint8)
 

img = cv2.dilate(img, kernel, iterations=1)

a,b=(15,3)
c,d=(46,49)
img[a][b] = 255
print(b,a)
print(d,c)

path1=[]
path2=[]
z=n*n
value=[z,z,z,z,z,z,z,z]
end=0
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
def astar(i,j):
    global end
    if end==0:
        while(i,j!=c,d):
            value=[z,z,z,z,z,z,z,z]
            path1.append(i)
            path2.append(j)
            cv2.imshow('Image', img)
            cv2.waitKey(5)
            if(i-1>=0):
                if((i-1,j)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i-1,j]==255):
                    img[i-1,j]=127
                    g=2
                    h=(c-i+1)**2+(d-j)**2
                    f=g+h
                    value[0]=f

            if(j-1>=0):
                if((i,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i,j-1]==255):
                    img[i,j-1]=127
                    g=2
                    h=(c-i)**2+(d-j+1)**2
                    f=g+h
                    value[1]=f
                   
            if(i+1<n):
                if((i+1,j)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j]==255):
                    img[i+1,j]=127
                    g=2
                    h=(c-i-1)**2+(d-j)**2
                    f=g+h
                    value[2]=f
                    
            if(j+1<m):
                if((i,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i,j+1]==255):
                    img[i,j+1]=127
                    g=2
                    h=(c-i)**2+(d-j-1)**2
                    f=g+h
                    value[3]=f
                    
            if(j+1<m and i+1<n):
                if((i+1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j+1]==255):
                    img[i+1,j+1]=127
                    g=1
                    h=(c-i-1)**2+(d-j-1)**2
                    f=g+h
                    value[4]=f

            if(j+1<m and i-1>=0):
                if((i-1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i-1,j+1]==255):
                    img[i-1,j+1]=127
                    g=2
                    h=(c-i+1)**2+(d-j-1)**2
                    f=g+h
                    value[5]=f

            if(i+1<n and j-1>=0):
                if((i+1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j-1]==255):
                    img[i+1,j-1]=127
                    g=2
                    h=(c-i-1)**2+(d-j+1)**2
                    f=g+h
                    value[6]=f

            if(j-1>=0 and i-1>=0):
                if((i-1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i-1,j-1]==255):
                    img[i-1,j-1]=127
                    g=2
                    h=(c-i+1)**2+(d-j+1)**2
                    f=g+h
                    value[7]=f  

            minpos=value.index(min(value)) 
            if minpos==0:
                astar(i-1,j)
            elif minpos==1:
                astar(i,j-1)
            elif minpos==2:
                astar(i+1,j)
            elif minpos==3:
                astar(i,j+1)
            elif minpos==4:
                astar(i+1,j+1)
            elif minpos==5:
                astar(i-1,j+1)
            elif minpos==6:
                astar(i+1,j-1)
            elif minpos==7:
                astar(i-1,j-1)
            break
    
    else:
        print("final complete")
begin=time.time()        
astar(a,b)
end=time.time()
print("time=", end-begin)
l=len(path1)
print("distance=", l)
for k in range(l-1):
    img[path1.pop(),path2.pop()]=200
    cv2.imshow('Image', img)
    cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows
                        
