"""
@author: LiShiHang
@software: PyCharm
@file: 1.4.滑动条.py
@time: 2019/1/13 17:10
@desc:
"""
import cv2
import numpy as np


def fun_change(x):
    pass


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.createTrackbar("R", "image", 0, 255, fun_change)
cv2.createTrackbar("G", "image", 0, 255, fun_change)
cv2.createTrackbar("B", "image", 0, 255, fun_change)

while True:

    cv2.imshow("image", img)
    if cv2.waitKey(24) == ord('q'):
        break
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    img[:, :, :] = [b, g, r]
