import cv2
import numpy as np


counter2= 15
i=0

cap = cv2.VideoCapture("object.mp4")

def mouse_event(event, x,y,flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (event)
        pixel = hsv[y,x]

        cv2.setTrackbarPos('lowh','trackbar',pixel[0] - 10)
        cv2.setTrackbarPos('highh','trackbar',pixel[0] + 10)
        cv2.setTrackbarPos('lows','trackbar',pixel[1] - 20)
        cv2.setTrackbarPos('highs','trackbar',pixel[1] + 20)
        cv2.setTrackbarPos('lowv','trackbar',pixel[2] - 50)
        cv2.setTrackbarPos('highv','trackbar',pixel[2] + 50)
        
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
    

def callback(x):
        pass

cv2.namedWindow('trackbar')
cv2.namedWindow('imag')

cv2.createTrackbar('lowh','trackbar',0,180,callback)
cv2.createTrackbar('highh','trackbar',0,180,callback)
cv2.createTrackbar('lows','trackbar',0,255,callback)
cv2.createTrackbar('highs','trackbar',0,255,callback)
cv2.createTrackbar('lowv','trackbar',0,255,callback)
cv2.createTrackbar('highv','trackbar',0,255,callback)

while 1:
    i=i+1
    _,img=cap.read()
    cv2.setMouseCallback('imag',mouse_event)
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lowh=cv2.getTrackbarPos('lowh', 'trackbar')
    highh=cv2.getTrackbarPos('highh', 'trackbar')
    lows=cv2.getTrackbarPos('lows', 'trackbar')
    highs=cv2.getTrackbarPos('highs', 'trackbar')
    lowv=cv2.getTrackbarPos('lowv', 'trackbar')
    highv=cv2.getTrackbarPos('highv', 'trackbar')

    lowred=np.array([lowh,lows,lowv])
    highred=np.array([highh,highs,highv])

    mask= cv2.inRange (hsv,lowred,highred)
    
    kernel = np.ones((5,5),np.uint8)
    dilate = cv2.dilate(mask, kernel, iterations = 1)
    closing= cv2.morphologyEx(dilate , cv2.MORPH_CLOSE, kernel)
    
    
    counter2=counter2+1
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
    
    if i!=1:
        closing2=closing
        closing=(closing2+closing)

        #final=cv2.cvtColor(closing,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('closing',closing2)

    #closing = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    final= closing
    #final=cv2.cvtColor(closing,cv2.COLOR_BGR2GRAY)
    white=white1+white2+white3+white4+white5+white6+white7+white8+white9+white10+white11+white12+white13+white14+white15
    cv2.imshow('white',white)
        
    
    #if i==1:
        #continue

    
    gray = cv2.cvtColor(white,cv2.COLOR_BGR2GRAY)
    (_,contours,_)=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,255,0),3)

    
    '''
    for i in contours:
                    area = cv2.contourArea(i)
                    if(area>500):
                            x,y,w,h = cv2.boundingRect(i
                                                       )
                            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                            cv2.putText(img,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    '''

    cv2.imshow('imag',img)
    cv2.imshow('white', white)
    cv2.imshow('closing',closing)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break                          

cap.release()
cv2.destroyAllWindows()



