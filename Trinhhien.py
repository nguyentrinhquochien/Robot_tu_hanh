import cv2
import numpy as np
import utlis


def getLaneCurve(img):
    imgThres = utlis.thresholding(img)


def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([85, 0, 0])
    upperWhite = np.array([179, 160, 255])
    maskedWhite= cv2.inRange(hsv,lowerWhite,upperWhite)
    return maskedWhite



if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)
        cv2.waitKey(1)