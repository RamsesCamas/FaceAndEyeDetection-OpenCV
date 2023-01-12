import numpy as np
import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

i = 0
while True:
    ret, frame = cap.read()
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_scale, 1.3, 5)
    for (x,y, w, h) in faces:
        color_red = (0,0,255)
        color_blue = (255,0,0)
        cv2.rectangle(frame, (x,y),(x + w, y + h), color_blue, 5)
        roi_gray_scale = gray_scale[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray_scale, 1.3, 5)
        if len(eyes) > 0:
            i += 1
        else:
            i = 0

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), color_red, 5)
    print(i)
    if i >= 300:
        print("Te quedaste viendo 10 segundos")
        cv2.imwrite("Original.jpg",frame)
        i = 0
    cv2.imshow('image', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()