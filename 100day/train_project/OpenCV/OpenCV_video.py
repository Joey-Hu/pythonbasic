#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: OpenCV_video.py
# @time: 2019/6/14 10:11
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import cv2

# 当参数 = 0，调取本地摄像头
cap = cv2.VideoCapture(0)



# 读取连续的视频and人脸识别
detector = cv2.CascadeClassifier('./feature_data/haarcascade_frontalface_default.xml')

while cap.isOpened():
    flag, frame1 = cap.read()

    if flag == False:
        break

    frame = cv2.resize(frame1, dsize=(720, 480))
    face_zone = detector.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=2, )
    for x,y,w,h in face_zone:
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=2)
    cv2.imshow('bayern', frame)

    if ord('q') == cv2.waitKey(10):
        break

cv2.destroyAllWindows()
cap.release()