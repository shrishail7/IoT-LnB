
import cv2

trainData = cv2.CascadeClassifier("Face.xml")

img = cv2.imread("temp/family.png")

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCoordinates = trainData.detectMultiScale(grayimg)

for x, y, w, h in faceCoordinates:
    cv2.rectangle(img , (x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Narendra Modi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()