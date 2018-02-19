import cv2
import numpy as np
import os
cap = cv2.VideoCapture(1)

def threshImg(img, lower, upper, color = "some_color", showImg = 1):
    lower_color = np.array(lower)
    upper_color = np.array(upper)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if showImg : cv2.imshow(color, mask)

i = 0
while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    "Writing images to folder : "
    cv2.imwrite(os.path.join("TestImages" , "image" + str(i) + ".png"), frame)
    
    #GOLDEN
    threshImg(frame.copy(), [50, 0, 0], [80, 150, 150], "Golden", 1)

    #BLUE    
    threshImg(frame.copy(), [100, 50, 30], [120, 255, 255], "Blue", 1)

    #RED:
    threshImg(frame.copy(), [30, 150, 100], [255, 255, 180], "Red", 1)
    if ret == True:
        
        cv2.imshow('frame',frame)
    i += 1
    print(i)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()


"""
RED:
    lower_red = np.array([30,150,100])
    upper_red = np.array([255,255,180])
BLUE:
    lower_blue = np.array([100,50,30])
    upper_blue = np.array([120,255,255])
GOLDEN:
    lower_golden = np.array([50,0,0])
    upper_golden = np.array([80,150,150])
    
"""
