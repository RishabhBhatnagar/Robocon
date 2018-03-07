import cv2
import numpy as np
import os
import time
#import RPi.GPIO    "Uncomment the import statement when uploading to RPi."

class GPIO:
    '''Comment this class when uploading on RPi
    Since I didn't had a Rpi.GPIO module,
    I've created a GPIO class so that this code can be tested.'''
    BOARD = 1                         #any random number
    OUT = 1
    def cleanup():return
    def setup(*args):return
    def output(*args):return
    def setmode(*args):return
    def setwarnings(*args):return


"Pin numbers for giving output."
red_pin = 7
golden_pin = 11
blue_pin = 13

high = 1
low = 0


'''change 1 to 0 when uploading to RPi.
  #1 is for output ports of your machine that is, for webcam connected, 1 will be used.
  #0 is for default webcam registered in your OS. 
'''
cap = cv2.VideoCapture(0)

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(golden_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

def threshImg(img, lower, upper, color = "some_color", showImg = 1):
    lower_color = np.array(lower)
    upper_color = np.array(upper)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if showImg : cv2.imshow(color, res)
    return mask

def rpiOutput(high_pin, *args):
    """
    Setting the output pins of Raspberry Pi module high for detected color.
    1 is for HIGH
    0 is for LOW
    """
    GPIO.output(high_pin, high)
    for pins in args:
        GPIO.output(pins, low)

number_of_frames = 10
colors = {"red":0, "blue":0, "green":0}
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    show = [1, 1, 1]     # Show frames of g, b, r
    
    #GOLDEN
    golden_img = threshImg(frame, [10, 40, 120],
                                  [35, 240, 250], "Golden1", show[0])

    #BLUE
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
    
    if mx == r :
        rpiOutput(red_pin, golden_pin, blue_pin)
        max2 = max([g, b])
    if mx == g :
        rpiOutput(golden_pin, red_pin, blue_pin)
        max2 = max([r, b])
    if mx == b :
        rpiOutput(blue_pin, golden_pin, red_pin)
        max2 = max([r, g])

    if mx == r : print("Red")
    elif mx == g : print("Golden")
    elif mx == b : print("Blue")

    #checking the closest color that has similar number of pixels.
    if max2 == r : print("Clash with RED")
    if max2 == g : print("Clash with GOLDEN")
    if max2 == b : print("Clash with BLUE")
    
    print(r,g,b)

    if mx == 0 : print("Division by zero Error.")
    else : print("Percenrage difference :", 100*(mx-max2)/mx)

    time.sleep(0.1)   #adding delay so that output can be read.

    cv2.imshow("frame", frame)

cv2.destroyAllWindows()
cap.release()
