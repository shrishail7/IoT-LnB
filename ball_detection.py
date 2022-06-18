'''
Template matching (Object detection)

to detect ball

'''

import cv2
import numpy as np

img = cv2.imread('asset/ball.png',0) #0 - gray scale
img = cv2.resize(img , (0,0), fx=0.6 ,fy = 0.6)
template = cv2.imread('asset/ball.png',0)
template = cv2.resize(template , (0,0), fx=0.6 ,fy = 0.6)
h,w = template.shape

#print(h,w)  (125,124)

#methods of doing template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2 , template , method)
    min_val , max_val , min_loc , max_loc = cv2.minMaxLoc(result)
    
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = [location[0]+w , location[1]+h]
    cv2.rectangle(img2, location , bottom_right , 255,2)
    cv2.imshow("Detected" , img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()