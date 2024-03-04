import cv2 
import sys

capture = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    cv2.imshow("Face", frame)
    
    if cv2.waitKey(5) == ord("s"):
        break
    
capture.release()
cv2.destroyAllWindows

    
