
import cv2
import numpy as np
mode=0

def nothing(x):
    pass

def CallBackFunc(event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDOWN:
            pix_val = hsv(y,x)

        upper =  np.array([pix_val[0] + 10, pix_val[1] + 10, pix_val[2] + 40])
        lower =  np.array([pix_val[0] - 10, pix_val[1] - 10, pix_val[2] - 40])
        
        if mode ==0  :      
            cv2.setTrackbarPos('lowh','trackbars',pix_val[0]-20)
            cv2.setTrackbarPos('highh','trackbars',pix_val[0]+20)
            cv2.setTrackbarPos('lows','trackbars',pix_val[1]-20)
            cv2.setTrackbarPos('highs','trackbars',pix_val[1]+20)
            cv2.setTrackbarPos('lowv','trackbars',pix_val[2]-20)
            cv2.setTrackbarPos('highv','trackbars',pix_val[2]+20)

def callback(x):
        pass
    

ilowh=0;
ihighh = 13;
ilows = 121;
ihighs = 247;
ilowv = 28;
ihighv = 255;

ilowh1=255;
ihighh1 = 255;
ilows1 = 255;
ihighs1 = 255;
ilowv1 =255;
ihighv1 =255;

ilowh2=170;
ihighh2 = 179;
ilows2 = 159;
ihighs2 = 255;
ilowv2 = 52;
ihighv2 = 255;

cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)
cap=cv2.VideoCapture(0)

while 1:
            
    ret,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    cv2.setMouseCallback('frame',CallBackFunc)
    if(mode==0):
        ilowh=cv2.getTrackbarPos('lowh', 'image')
        ihighh=cv2.getTrackbarPos('highh', 'image')
        ilows=cv2.getTrackbarPos('lows', 'image')
        ihighs=cv2.getTrackbarPos('highs', 'image')
        ilowv=cv2.getTrackbarPos('lowv', 'image')
        ihighv=cv2.getTrackbarPos('highv', 'image')
    #lowh,lows,lowv=0,24,56
    #highh,highs,highv=180,255,255
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([ilowh,ilows,ilowv])
    upper_red = np.array([ihighh,ihighs,ihighv])

    mask = cv2.inRange(hsv, lower_red , upper_red)
    
    _,contours,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    '''
    rect= cv2.minAreaRect(cnt)
    box= cv2.boxPoints(rect)  
    box= np.uint0(box)
    '''
    for c in contours:
        x,y,w,h=cv2.boundingRect(c)
        img= cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    #cv2.drawContours(frame,contours,-1,(225,0,0),3)
    cv2.imshow('frame',frame)
    cv2.imshow("mask",mask)
    #cv2.imshow("gray",gray)
    k = cv2.waitKey(10) & 0xFF 
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()


'''

import cv2
import numpy as np
while 1:
    up=np.array([180,255,255])
    low=np.array([0,0,0])
    
    img=cv2.imread('triangles.png')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,low,up)
    #gray=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    ret,boo = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    _,contours,_ = cv2.findContours(boo,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contours,-1,(0,0,255),3)
    cv2.imshow('frame',boo)
    cv2.imshow('img',img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()
'''
