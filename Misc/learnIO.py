import cv2
import numpy as np
import os

# loading an image
image = cv2.imread("test.PNG")

# convert to bits array - 1d
byteArray = bytearray(image)
# print(byteArray)

# generate a random color image
rba = bytearray(os.urandom(120000))
flatArray = np.array(rba)

# to gray image
grayImage = flatArray.reshape(300,400)
cv2.imwrite("randomGray.jpg", grayImage)

# to color image
bgrImage = flatArray.reshape(100,400,3)
cv2.imwrite("randomColor.jpg", bgrImage)

# saving an image
cv2.imwrite("MyTest.jpg",image)
