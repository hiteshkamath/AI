from cv2 import imshow, waitKey, destroyAllWindows, cvtColor, bitwise_and, inRange, VideoCapture, COLOR_BGR2HSV
import numpy as np

cap = VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cvtColor(frame, COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = inRange(hsv, lower_blue, upper_blue)
    result = bitwise_and(frame, frame, mask=mask)

    imshow('Original', frame)
    imshow('Mask (White = Blue Area)', mask)
    imshow('Blue Detection', result)

    if waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()