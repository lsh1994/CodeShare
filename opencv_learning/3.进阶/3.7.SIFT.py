"""
@author: LiShiHang
@software: PyCharm
@file: 3.7.SIFT.py
@time: 2019/1/8 21:15
@desc:
"""
# 需要安装扩展模块`pip install opencv-contrib-python==3.3.1.11`
# todo: ...

import cv2
import numpy as np

img = cv2.imread('../res/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

keypoints, des = sift.detectAndCompute(gray, None)  # 关键点和描述符（len(keypoints)x128）

print(keypoints, des)

cv2.drawKeypoints(
    gray,
    keypoints,
    img,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('sift_keypoints.jpg', img)
cv2.waitKey(0)
