import cv2
img = cv2.imread('ring.jpg')
##cv2.imshow("original image",img)

"Applying the median filter to original image"
median = cv2.medianBlur(img,5)

#converting image to gray format.
imgray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
##cv2.imshow("Grayscaled image",imgray)

"Converting image to binary"
_,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
##cv2.imshow("thresholded image" ,thresh)


#finding contour in the specified area of thresh image
image,contours,_ = cv2.findContours(thresh[200:700,150:500], 1, 2)

"drawing the found contours on thresh"
"cv2.drawContours(thresh,contours,-1,(0,255,0),3)"

#Fitting all the contours found in cirle
for i in range(len(contours)):
    (x,y),radius = cv2.minEnclosingCircle(contours[i])
    center = (int(x),int(y))
    radius = int(radius)
    image = cv2.circle(image,center,radius,(0,255,0),2)
    cv2.imshow("part processed",image)

cv2.imshow("final image",thresh)
