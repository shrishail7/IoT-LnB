import cv2

trainData = cv2.CascadeClassifier("Face.xml")

webCam = cv2.VideoCapture(0)

while True:
    ret , frame = webCam.read()

    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faceCoordinates = trainData.detectMultiScale(grayimg)

    for x,y,w,h in faceCoordinates:
        cv2.rectangle(frame , (x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('photo', frame)

    if cv2.waitKey(1) == ord('q'):
        break

webCam.release()
cv2.destroyAllWindows()