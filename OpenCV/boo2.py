import cv2
import numpy as np
import math
counter=0

cap= cv2.VideoCapture('theroad.mp4')
w=cap.get(3)
h=cap.get(4)

def callback(x):
    pass

cv2.namedWindow('frame')
cv2.namedWindow('hough')
cv2.namedWindow('rad')

cv2.createTrackbar('minline','hough',0,1000,callback)
cv2.createTrackbar('maxgap','hough',0,1000,callback)

cv2.createTrackbar('rad1','rad',700,1000,callback)
cv2.createTrackbar('rad2','rad',600,1000,callback)
cv2.createTrackbar('width','rad',687,1000,callback)

while 1:
    _,img=cap.read()

    rad1=cv2.getTrackbarPos('rad1','rad')
    rad2=cv2.getTrackbarPos('rad2','rad')
    width=cv2.getTrackbarPos('width','rad')
    cv2.ellipse(img,(640,640),(rad1,rad2),0,0,360,(0,0,0),width)

##    if (all three of them for loop +3)
    white1 = np.zeros((720,1280,3), np.uint8)
    white1 = cv2.bitwise_not(white1)
    
    white2 = np.zeros((720,1280,3), np.uint8)
    white2 = cv2.bitwise_not(white2)

    white3 = np.zeros((720,1280,3), np.uint8)
    white3 = cv2.bitwise_not(white3)

    white4 = np.zeros((720,1280,3), np.uint8)
    white4 = cv2.bitwise_not(white4)
     
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    thresh=cv2.getTrackbarPos('thresh','hough')
    thresh2=cv2.getTrackbarPos('thresh2','hough')
    _,black=cv2.threshold(gray,120,250,cv2.THRESH_BINARY)

    canny = cv2.Canny(black, 50, 150, None, 3)
    minline=cv2.getTrackbarPos('minline','hough')
    maxgap=cv2.getTrackbarPos('maxgap','hough')
    
    linesP = cv2.HoughLinesP(canny, 1, np.pi / 180, 15, None, minline, maxgap)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
##            cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%3==0:
                cv2.line(white1, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%3==1:
                cv2.line(white2, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%3==2:
                cv2.line(white3, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)

    #res=cv2.bitwise_and(img,img,blank=ablank)

##    lines = cv2.HoughLines(canny, 1, np.pi / 180, 150, None)
##    if lines is not None:
##            for i in range(0, len(lines)):
##                rho = lines[i][0][0]
##                theta = lines[i][0][1]
##                a = math.cos(theta)
##                b = math.sin(theta)
##                x0 = a * rho
##                y0 = b * rho
##                pt1 = (int(x0 + 2000*(-b)), int(y0 + 2000*(a)))
##                pt2 = (int(x0 - 2000*(-b)), int(y0 - 2000*(a)))
##                cv2.line(img, pt1, pt2, (0,0,0), 3, cv2.LINE_AA)

    low=np.array([0,10,10])
    high=np.array([180,255,255])

    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,low,high)

    white4=white1+white2+white3
    
    (_,contours,_)=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,0,(0,0,255),3)
    
    kernel = np.ones((10,10),np.uint8)
    dilation = cv2.dilate(black, kernel , iterations = 2)
    
    cv2.imshow('mask',canny)
    cv2.imshow('img',img)
    cv2.imshow('black',black)
    counter=counter+1
    cv2.imshow('white1',white4)
    cv2.imshow('white2',white2)
    cv2.imshow('white3',white3)
   
    

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break                          

cap.release()
cv2.destroyAllWindows()
