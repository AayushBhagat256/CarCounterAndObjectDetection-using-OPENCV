import cv2
from ultralytics import YOLO
import cvzone

# creating web cam object
cap = cv2.VideoCapture(0)
cap.set(3,1280) # for width
cap.set(4,720) #for height

while True:
    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)