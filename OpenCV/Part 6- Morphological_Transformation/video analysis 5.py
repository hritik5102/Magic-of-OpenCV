import cv2
import numpy as np

def nothing(x):
    
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('erosion2', cv2.WINDOW_NORMAL)
cv2.namedWindow('dilation', cv2.WINDOW_NORMAL)
cv2.namedWindow('opening', cv2.WINDOW_NORMAL)
cv2.namedWindow('closing', cv2.WINDOW_NORMAL)


while True :
    #take each frame
    _, frame = cap.read()
    

    kernel = np.ones((5,5),np.uint8)
    ##erosion = cv2.erode(mask, kernel , iterations = 2)                                
    erosion2 = cv2.erode(frame, kernel , iterations = 2)
    dilation = cv2.dilate(frame, kernel , iterations = 2)

    opening = cv2.morphologyEx(frame , cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(frame , cv2.MORPH_CLOSE, kernel)
 
    

    



    cv2.imshow('erosion2', erosion2)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing', closing)


    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    

    
