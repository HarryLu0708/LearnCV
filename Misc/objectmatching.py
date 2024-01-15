import cv2
import numpy as np

template = cv2.imread("moon_target.png")
source_image = cv2.imread("moon.jpg")

template_height, template_width = template.shape[:2]
result = cv2.matchTemplate(source_image,template,cv2.TM_CCOEFF)
min_val, max_val,min_loc,max_loc = cv2.minMaxLoc(result)
top_left = max_loc
buttom_right = (top_left[0]+template_width,top_left[1]+template_height)
cv2.rectangle(source_image,top_left,buttom_right,(0,255,0),1)
cv2.imshow("detection task",source_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
