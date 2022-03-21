from ctypes.wintypes import RGB
import cv2 
import numpy as np

img=cv2.imread("myProject/assets/catImage.jpg")

rimg=cv2.resize(img,(300,300))
gray=cv2.cvtColor(rimg,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,200,0.01,10)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(rimg,(x,y),3,(0,0,255),-2)

cv2.imshow("Original Image",rimg)

cv2.waitKey(0)