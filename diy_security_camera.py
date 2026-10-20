import winsound
import cv2

webcam = cv2.VideoCapture(0)

while True:
    success, image1 = webcam.read()
    success, image2 = webcam.read()
    diff = cv2.absdiff(image1, image2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    success, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    contours, success = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        winsound.PlaySound(
            "sound.wav",
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    cv2.imshow("Security Camera", thresh)
    if cv2.waitKey(10) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
