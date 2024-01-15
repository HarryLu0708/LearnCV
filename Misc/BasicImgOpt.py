import cv2

img = cv2.imread("test.PNG")

# Access Single Cell

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if j%10==0:
            img[i,j] = (0,0,0)
        if i%10==0:
            img[i,j] = (0,0,0)

cv2.imshow("Result",img)

# Build ROI
x=50
y=60
w=100
h=200

roi = img[y:y+h,x:x+w]
print(roi.shape)
img[100:150,150:200] = (0,255,0)

cv2.imshow("ROI",roi)
cv2.imshow("ROI 2",img)



cv2.waitKey(0)
cv2.destroyAllWindows()


