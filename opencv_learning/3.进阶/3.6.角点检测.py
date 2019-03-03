"""
@author: LiShiHang
@software: PyCharm
@file: 3.6.角点检测.py
@time: 2019/1/8 19:50
@desc:
"""
import cv2
import numpy as np

img = cv2.imread("../res/corner_sample.jpg")  # chessboard.png
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("originalPicture", img)

# Harris角点检测
harris_dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
harris_dst = cv2.dilate(harris_dst, None)  # 腐蚀一下
img_copy = img.copy()
img_copy[harris_dst > 0.01 * harris_dst.max()] = (0, 0, 255)  # 着色
cv2.imshow("harris_dst", img_copy)

# Shi-Tomasi角点检测
st_corners = cv2.goodFeaturesToTrack(img_gray, 20, 0.01, 10)
st_corners = np.array(st_corners).astype(np.int)
img_copy2 = img.copy()
for i in st_corners:
    cv2.circle(img_copy2, tuple(i[0]), 4, (255, 0, 0), -1)
cv2.imshow("Shi-Tomasi_corners", img_copy2)


cv2.waitKey(0)
