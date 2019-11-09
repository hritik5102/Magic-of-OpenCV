import cv2
import numpy as np
import math
counter=0
counter2=15

cap= cv2.VideoCapture('theroad.mp4')
w=cap.get(3)
h=cap.get(4)

def callback(x):
    pass

cv2.namedWindow('frame')
cv2.namedWindow('hough',cv2.WINDOW_NORMAL)
cv2.namedWindow('rad')
cv2.namedWindow('cor')

cv2.createTrackbar('minline','hough',0,1000,callback)
cv2.createTrackbar('maxgap','hough',20,1000,callback)
cv2.createTrackbar('cx','hough',607,2000,callback)
cv2.createTrackbar('cy','hough',554,2000,callback)

cv2.createTrackbar('rad1','rad',700,1000,callback)
cv2.createTrackbar('rad2','rad',600,1000,callback)
cv2.createTrackbar('width','rad',687,1000,callback)

cv2.createTrackbar('x1','cor',0,2000,callback)
cv2.createTrackbar('y1','cor',0,2000,callback)
cv2.createTrackbar('x2','cor',0,2000,callback)
cv2.createTrackbar('y2','cor',0,2000,callback)
cv2.createTrackbar('x3','cor',0,2000,callback)
cv2.createTrackbar('y3','cor',0,2000,callback)
cv2.createTrackbar('x4','cor',0,2000,callback)
cv2.createTrackbar('y4','cor',0,2000,callback)

white2 = np.zeros((720,1280,3), np.uint8)
white2 = cv2.bitwise_not(white2)
white3 = np.zeros((720,1280,3), np.uint8)
white3 = cv2.bitwise_not(white3)
white4 = np.zeros((720,1280,3), np.uint8)
white4 = cv2.bitwise_not(white4)
white5 = np.zeros((720,1280,3), np.uint8)
white5 = cv2.bitwise_not(white5)
white6 = np.zeros((720,1280,3), np.uint8)
white6 = cv2.bitwise_not(white6)
white7 = np.zeros((720,1280,3), np.uint8)
white7 = cv2.bitwise_not(white7)
white8 = np.zeros((720,1280,3), np.uint8)
white8 = cv2.bitwise_not(white8)
white9 = np.zeros((720,1280,3), np.uint8)
white9 = cv2.bitwise_not(white9)
white10 = np.zeros((720,1280,3), np.uint8)
white10 = cv2.bitwise_not(white10)
white11 = np.zeros((720,1280,3), np.uint8)
white11 = cv2.bitwise_not(white11)
white12 = np.zeros((720,1280,3), np.uint8)
white12 = cv2.bitwise_not(white12)
white13 = np.zeros((720,1280,3), np.uint8)
white13 = cv2.bitwise_not(white13)
white14 = np.zeros((720,1280,3), np.uint8)
white14 = cv2.bitwise_not(white14)
white15 = np.zeros((720,1280,3), np.uint8)
white15 = cv2.bitwise_not(white15)                  


while 1:
    counter=counter+1
    counter2=counter2+1
    _,img=cap.read()

    rad1=cv2.getTrackbarPos('rad1','rad')
    rad2=cv2.getTrackbarPos('rad2','rad')
    width=cv2.getTrackbarPos('width','rad')
    
    x1=cv2.getTrackbarPos('x1','cor')
    y1=cv2.getTrackbarPos('x1','cor')
    x2=cv2.getTrackbarPos('x1','cor')
    y2=cv2.getTrackbarPos('x1','cor')
    x3=cv2.getTrackbarPos('x1','cor')
    y3=cv2.getTrackbarPos('x1','cor')
    x4=cv2.getTrackbarPos('x1','cor')
    y4=cv2.getTrackbarPos('x1','cor')
    
   # cv2.ellipse(img,(640,640),(rad1,rad2),0,0,360,(0,0,0),width)
   

    vrx = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]], np.int32)
    vrx = vrx.reshape((-1,1,2))
    img = cv2.polylines(img, vrx, True, (0,255,0))

    if counter2==16:
        white1 = np.zeros((720,1280,3), np.uint8)
        white1 = cv2.bitwise_not(white1)
    if counter2==17:
        white2 = np.zeros((720,1280,3), np.uint8)
        white2 = cv2.bitwise_not(white2)
    if counter2==18:
        white3 = np.zeros((720,1280,3), np.uint8)
        white3 = cv2.bitwise_not(white3)
    if counter2==19:
        white4 = np.zeros((720,1280,3), np.uint8)
        white4 = cv2.bitwise_not(white4)
    if counter2==20:
        white5 = np.zeros((720,1280,3), np.uint8)
        white5 = cv2.bitwise_not(white5)
    if counter2==21:
        white6 = np.zeros((720,1280,3), np.uint8)
        white6 = cv2.bitwise_not(white6)
    if counter2==22:
        white7 = np.zeros((720,1280,3), np.uint8)
        white7 = cv2.bitwise_not(white7)
    if counter2==23:
        white8 = np.zeros((720,1280,3), np.uint8)
        white8 = cv2.bitwise_not(white8)
    if counter2==24:
        white9 = np.zeros((720,1280,3), np.uint8)
        white9 = cv2.bitwise_not(white9)
    if counter2==25:
        white10 = np.zeros((720,1280,3), np.uint8)
        white10 = cv2.bitwise_not(white10)
    if counter2==26:
        white11 = np.zeros((720,1280,3), np.uint8)
        white11 = cv2.bitwise_not(white11)
    if counter2==27:
        white12 = np.zeros((720,1280,3), np.uint8)
        white12 = cv2.bitwise_not(white12)
    if counter2==28:
        white13 = np.zeros((720,1280,3), np.uint8)
        white13 = cv2.bitwise_not(white13)
    if counter2==29:
        white14 = np.zeros((720,1280,3), np.uint8)
        white14 = cv2.bitwise_not(white14)
    if counter2==30:
        white15 = np.zeros((720,1280,3), np.uint8)
        white15 = cv2.bitwise_not(white15)
    
    if counter2==30:
        counter2=15
    white = np.zeros((720,1280,3), np.uint8)
    white = cv2.bitwise_not(white)
 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    thresh=cv2.getTrackbarPos('thresh','hough')
    thresh2=cv2.getTrackbarPos('thresh2','hough')
    _,black=cv2.threshold(gray,120,250,cv2.THRESH_BINARY)

    canny = cv2.Canny(black, 50, 150, None, 3)
    minline=cv2.getTrackbarPos('minline','hough')
    maxgap=cv2.getTrackbarPos('maxgap','hough')
    
    cx=cv2.getTrackbarPos('cx','hough')
    cy=cv2.getTrackbarPos('cy','hough')
    
    linesP = cv2.HoughLinesP(canny, 1, np.pi / 180, 15, None, minline, maxgap)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if counter%15==0:
                cv2.line(white15, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==1:
                cv2.line(white1, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==2:
                cv2.line(white2, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==3:
                cv2.line(white3, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==4:
                cv2.line(white4, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==5:
                cv2.line(white5, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==6:
                cv2.line(white6, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==7:
                cv2.line(white7, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==8:
                cv2.line(white8, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==9:
                cv2.line(white9, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==10:
                cv2.line(white10, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==11:
                cv2.line(white11, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==12:
                cv2.line(white12, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==13:
                cv2.line(white13, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            if counter%15==14:
                cv2.line(white14, (l[0], l[1]), (l[2], l[3]), (0,0,0), 3, cv2.LINE_AA)
            

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

    white=white1+white2+white3+white4+white5+white6+white7+white8+white9+white10+white11+white12+white13+white14+white15
    cv2.rectangle(white,(cx-300,cy+100),(cx+300,cy-100),(0,0,0),4)
    cv2.ellipse(white,(640,640),(rad1,rad2),0,0,360,(0,0,0),width)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(white,kernel,iterations = 6)
    cv2.imshow('white',white)
    erosion= cv2.cvtColor(erosion,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(erosion, 50, 150, None, 3)

    (_,contours,_)=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img,contours,0,(0,0,255),4)
    
         
    for i in contours:
                    area = cv2.contourArea(i)
                  
                      
                    if(area>20000):
                            cv2.drawContours(img,contours,0,(0,0,255),4)
                            
##                            x,y,w,h = cv2.boundingRect(i)
##
##                            rect = cv2.minAreaRect(i)
##                            box = cv2.boxPoints(rect)
##                            box = np.int0(box)
##                            cv2.drawContours(img,[box],0,(0,0,255),2)
##                            cv2.circle(img,(int(x+w/2),int(y+h/2)),3,(0,0,255),-1)                           
##                            #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
##                            #cv2.putText(img,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
##                    j=j+1
    
    cv2.imshow('edge',canny)
    cv2.imshow('erosion',erosion)
    cv2.imshow('img',img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break                          

cap.release()
cv2.destroyAllWindows()
