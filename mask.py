import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([10, 100,20])
    upper_blue = np.array([25,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Z CamS', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
Change Colour
BGR_color = np.array([[[255,0,0]]])
cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
'''