import cv2
import numpy as np
import os
cap = cv2.VideoCapture(1)

def threshImg(img, lower, upper, color = "some_color", showImg = 1):
    lower_color = np.array(lower)
    upper_color = np.array(upper)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if showImg : cv2.imshow(color, res)
    return mask

i = 21000
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    "Writing images to folder : "
    cv2.imwrite(os.path.join("TestImages" , "image" + str(i) + ".png"), frame)

    show = [1, 1, 1, 0]
    
    #GOLDEN
    golden_img = threshImg(frame, [10, 40, 120], [35, 240, 250], "Golden", show[0])

    #BLUE    Not sure ranges.
    blue_img = threshImg(frame, [20, 10, 25],
                                [255, 150, 155], "Blue", show[1])

    #RED: 
    red_img = threshImg(frame, [150,150,50],
                               [180, 255, 255], "Red", show[2])
    
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        pass

cv2.destroyAllWindows()
cap.release()


"""
RED:
    lower_red = np.array([150,150,50])
    upper_red = np.array([180, 255, 255])
BLUE:
    lower_blue = np.array([100,50,30])
    upper_blue = np.array([120,255,255])

Not Blue and Golden :
[(0,0), (0,10 : 160,255), (0, 24 : 221, 255)]
"""
