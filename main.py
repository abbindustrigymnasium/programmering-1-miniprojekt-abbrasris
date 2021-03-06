import cv2

face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    successful_read, frame = capture.read()

    if (not successful_read):
        print('Unable to read capture.')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
