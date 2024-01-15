import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("test.PNG")

b,g,r = cv2.split(img)

histSize = 256
histRange = (0,256)
b_hist = cv2.calcHist([b],[0],None,[histSize],histRange)
g_hist = cv2.calcHist([g],[0],None,[histSize],histRange)
r_hist = cv2.calcHist([r],[0],None,[histSize],histRange)

plt.plot(r_hist)
plt.plot(b_hist)
plt.plot(g_hist)

plt.xlim([0,255])
plt.show()


