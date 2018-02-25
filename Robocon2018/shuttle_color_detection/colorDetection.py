import cv2
import numpy as np
import os
import time

cap = cv2.VideoCapture(1)


def threshImg(img, lower, upper, color = "some_color", showImg = 1):
    lower_color = np.array(lower)
    upper_color = np.array(upper)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if showImg : cv2.imshow(color, res)
    return mask

number_of_frames = 10
colors = {"red":0, "blue":0, "green":0}
while cap.isOpened():
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    show = [1, 1, 1]     # Show frames of g, b, r
    
    #GOLDEN
    golden_img = threshImg(frame, [10, 40, 120],
                                  [35, 240, 250], "Golden", show[0])

    #BLUE    Not sure ranges.
    blue_img = threshImg(frame, [100, 100, 50],
                                [150, 255, 255], "Blue", show[1])

    #RED: 
    red_img = threshImg(frame, [150,140,0],
                               [180, 255, 255], "Red", show[2])


    r = cv2.countNonZero(red_img)
    g = cv2.countNonZero(golden_img)
    b = cv2.countNonZero(blue_img)

    mx = max([r,g,b])
    mn = min([r,g,b])
    diff = mx-mn
    if mx == r : max2 = max([g, b])
    if mx == g : max2 = max([r, b])
    if mx == b : max2 = max([r, g])

    if mx == r : print("Red")
    elif mx == g : print("Golden")
    elif mx == b : print("Blue")

    if max2 == r : print("Clash with RED")
    if max2 == g : print("Clash with GOLDEN")
    if max2 == b : print("Clash with BLUE")
    print(r,g,b)
    if mx == 0 : print("Division by zero Error.")
    else : print("Difference in pixels", 100*(mx-max2)/mx)
    number_of_frames -= 1

    time.sleep(0.08)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
