import cv2
import numpy as np
import os

cap = cv2.VideoCapture(1)


i = 0
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)




    lower_golden = np.array([50,0,0])
    upper_golden = np.array([80,150,150])    
    mask = cv2.inRange(hsv, lower_golden, upper_golden)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    img = cv2.imread('wiki.jpg',0)
    cv2.imshow("yellow_mask", mask)

    
    lower_blue = np.array([100,50,30])
    upper_blue = np.array([120,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #counting number of black Pixels:
    number_of_blue_pixels = cv2.countNonZero(mask)
    cv2.imshow('blue_mask',mask)

    lower_red = np.array([30,150,100])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #counting number of black Pixels:
    number_of_red_pixels = cv2.countNonZero(mask)


    if number_of_red_pixels > number_of_blue_pixels:print("red")
    else:print("blue")
    
    cv2.imshow('frame',frame)
    cv2.imshow('red_mask',mask)
    cv2.imshow('res',res)

    cv2.imwrite(os.path.join("TestImages", "test_image" + str(i) + ".png"), frame)
    
    i += 1

cv2.destroyAllWindows()
cap.release()


"""
RED:
    lower_red = np.array([30,150,100])
    upper_red = np.array([255,255,180])

BLUE:
    lower_blue = np.array([100,50,30])
    upper_blue = np.array([120,255,255])
    
"""
