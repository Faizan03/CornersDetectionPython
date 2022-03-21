import cv2 as cv
import numpy as np,matplotlib.pyplot as plt

def click_event(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x," ",y)

        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,str(x)+","+str(y),(x,y),font,1,(255,0,0),2)
        cv.imshow("image",image)
    if event==cv.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
 
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv.imshow('image', image)    
if __name__=="__main__":
    imgAddress='assets/pageImage.jpg'
    img=cv.imread(imgAddress)
    # print(img.shape)
    image=cv.resize(img,(512,512))
    # print(image.shape)
    imgCopy=np.copy(image)
    # cv.imwrite("assets/resizeImg.jpg",image)
    # cv.imshow('image',image)
    # cv.setMouseCallback('image',click_event)
    pt1=np.float32([[125,156],[416,138],[25,481],[496,490]])
    pt2=np.float32([[25,156],[490,138],[25,481],[496,490]])
    matrix=cv.getPerspectiveTransform(pt1,pt2)
    result=cv.warpPerspective(image,matrix,(500,500))
    cv.imshow('frame',image)
    cv.imshow("frame2",result)
    cv.waitKey(0)
    cv.destroyAllWindows()