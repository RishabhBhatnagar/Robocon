import cv2
import numpy as np
import os
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


def threshImg(img, lower, upper, color = "some_color", showImg = 1):
    lower_color = np.array(lower)
    upper_color = np.array(upper)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if showImg : cv2.imshow(color, res)
    return mask

def rpi_output(pin, *args):
    GPIO.output(pin, GPIO.HIGH)
    for pins in args :
        GPIO.output(pins, GPIO.LOW)

number_of_frames = 10
colors = {"red":0, "blue":0, "green":0}
while cap.isOpened and number_of_frames:
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
    
    dominant_color = max(r, g, b)

    if dominant_color == r :
        print("temp_red")
        colors['red'] = colors.get('red') + 1
    if dominant_color == g :
        print("temp_golden")
        colors['golden'] = colors.get('golden') + 1
        output = (1, 0)
    if dominant_color == b :
        print("temp_blue")
        colors['blue'] = colors.get('blue') + 1

    cv2.imshow("frame", frame)
    number_of_frames -= 1
    if cv2.waitKey(1) == 27:
        break
which_color = colors.keys()[colors.values().index(max(colors.values()))]
if which_color == 'red':
    rpi_output(3, 5,7)
elif which_color == 'blue':
    rpi_output(5, 3,7)
else :
    rpi_output(7, 3,5)
cv2.destroyAllWindows()
cap.release()
