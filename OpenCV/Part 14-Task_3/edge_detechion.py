import numpy as np
import cv2
def nothing(x):
    pass
cap= cv2.VideoCapture(0)
cv2.namedWindow('tb')
cv2.createTrackbar('x','tb',0,200,nothing)
cv2.createTrackbar('y','tb',0,200,nothing)

while 1:
    _, frame= cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    x=cv2.getTrackbarPos('x','tb')
    y=cv2.getTrackbarPos('y','tb')
    

    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,5)
    edges=cv2.Canny(frame,x,y)

    
    #cv2.imshow('original',frame)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('edge',edges)
    


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


    

    
