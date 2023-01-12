import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

take_photo = False
while True:
    ret, frame = cap.read()
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_scale, 1.5, 5)
    for (x,y, w, h) in faces:
        color_red = (0,0,255)
        color_blue = (255,0,0)
        cv2.rectangle(frame, (x,y),(x + w, y + h), color_blue, 5)
        roi_gray_scale = gray_scale[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray_scale, 3.6, 6)
        for (sx,sy, sw, sh) in smile:
            if sw > 400:
                take_photo = True
            else: 
                take_photo = False
            #print('Ancho: ', sw)
            #print('Alto: ', sh)
            cv2.rectangle(roi_color, (sx, sy),(sx + sw, sy + sh), color_red, 5)
    if take_photo:
        cv2.imwrite("Smile.jpg",frame)
    cv2.imshow('image', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()