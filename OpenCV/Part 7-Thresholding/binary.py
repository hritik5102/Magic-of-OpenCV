import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

def nothing(x):
    pass

#define trackbar
cv2.namedWindow('trackbar')
#cv2.createTrackbar('Block-size','trackbar',2,100,nothing)
cv2.createTrackbar('constant','trackbar',-50,100,nothing)
cv2.setTrackbarPos('constant','trackbar',100)
# read the frame
frame = cv2.imread('scan5.jpg')

#resize
frame  = cv2.resize(frame , (600,600))

#gray scale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray' , gray)

# kernel size 
ksize = 15

#filter
median = cv2.medianBlur(gray,ksize)
bilateral = cv2.bilateralFilter(gray,15,100,100)
kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(gray,-1,kernel)

#canny edge detector

img = median.copy()
canny = imutils.auto_canny(gray)


#block size
#bs = 15
# constant
#c = 28

while(1):
    #bs = cv2.getTrackbarPos('Block-size','trackbar')
    bs=21
    #c = 100
    c = cv2.getTrackbarPos('constant','trackbar')
    thresh = cv2.adaptiveThreshold(cv2.bitwise_not(gray), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bs, c)
    output = cv2.bitwise_and(cv2.bitwise_not(gray),thresh)
    cv2.imshow('canny', canny)
    cv2.imshow('thresh', thresh)
    cv2.imshow('output' , output)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break


cv2.destroyAllWindows()
