import cv2
import numpy as np

canvas = np.zeros((600,600,3),dtype=np.uint8)

p1 = (10,20)
p2 = (500,600)
p3 = (300,10)

cv2.line(canvas,p1,p2,(255,0,0),2)
cv2.line(canvas,p2,p3,(0,255,0),4)
cv2.line(canvas,p3,p1,(0,0,255),6)

cv2.rectangle(canvas,p1,p2,(255,255,255),thickness=3)
cv2.circle(canvas,(300,300),100,(100,100,100),thickness=3)

cv2.putText(canvas,"Hello World!",(50,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,color=(200,100,100),thickness=3)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
