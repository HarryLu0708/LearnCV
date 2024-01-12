import cv2
import numpy as np

img = cv2.imread("test.PNG")
img = cv2.resize(img,(300,600))

tx = 50
ty = 100
M = np.float32([[1,0,tx],[0,1,ty]])
rows, columns, _ = img.shape
trans_img = cv2.warpAffine(img,M,(columns,rows))

trans_img = cv2.rotate(trans_img,cv2.ROTATE_90_COUNTERCLOCKWISE)
M0 = cv2.getRotationMatrix2D((rows/2,columns/2),90,1)

trans_img = cv2.warpAffine(img,M0,(columns,rows))

x_flip = cv2.flip(trans_img,1)
y_flip = cv2.flip(trans_img,0)
xy_flip = cv2.flip(trans_img,-1)

cv2.imshow("Translated Image",trans_img)

cv2.imshow("x flip",x_flip)
cv2.imshow("y flip",y_flip)
cv2.imshow("xy flip",xy_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()