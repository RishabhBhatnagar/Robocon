import cv2
import numpy as np

def cannyEdges(frame):
    cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,100)
    cv2.imshow('Edges',edges)

def otherWay(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    
    gray = cv2.medianBlur(gray, 5)
    
    
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (255, 0, 255), 3)
    
    
    #cv2.imshow("detected circles", src)


c=0
arrayOfVideos = ["output_final_succeful.avi", "output_final_unsucceful.avi", 'output3.avi', "output_height_side2.avi", "output_side.avi", 'output_side2.avi', "output_succeful.avi", 'output2.avi', "output3.avi"]
for i in range(len(arrayOfVideos)):
    cap = cv2.VideoCapture(arrayOfVideos[i+3])
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        c = c+1
        print(c)
        cannyEdges(frame)
        otherWay(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
