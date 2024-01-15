import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("test.PNG")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
num_bins = 8
bin_range = [0,256]

hist = cv2.calcHist([gray_img],[0],None,[num_bins],bin_range)
hist2 = cv2.calcHist([gray_img],[0],None,[256],bin_range)

plt.plot(hist)
plt.xlim([0,num_bins-1])
plt.show()

plt.plot(hist2)
plt.xlim([0,255])
plt.show()
