"""
@author: LiShiHang
@software: PyCharm
@file: 2.7.金字塔.py
@time: 2019/1/9 12:42
@desc: 金字塔，尺度
"""
import cv2

img = cv2.imread("../res/lena.jpg")

lower = cv2.pyrDown(img)  # 下采样一级
higher = cv2.pyrUp(img)

cv2.imshow("img", img)
cv2.imshow("lower", lower)
cv2.imshow("higher", higher)

cv2.waitKey(0)
