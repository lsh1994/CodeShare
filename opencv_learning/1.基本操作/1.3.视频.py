"""
@author: LiShiHang
@software: PyCharm
@file: 1.3.视频.py
@time: 2019/1/3 11:14
@desc:
"""
import cv2
import numpy as np


def track_back(x):

    capture.set(cv2.CAP_PROP_POS_FRAMES, x)


capture = cv2.VideoCapture("../res/demo_video.mp4")

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)  # 设置窗口
fs = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar('process', 'frame', 1, fs, track_back)  # 滑动条

while capture.isOpened():
    ret, frame = capture.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 彩色转为灰度图

    cv2.imshow("frame", frame)
    if cv2.waitKey(24) == ord('q'):
        break