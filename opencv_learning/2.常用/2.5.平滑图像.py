"""
@author: LiShiHang
@software: PyCharm
@file: 2.5.平滑图像.py
@time: 2019/1/4 15:47
@desc:
"""
import cv2
import pandas as pd

img = cv2.imread("../res/lena.jpg")
cv2.imshow("OriginalPicture", img)

mean_filtering = cv2.blur(img, (3, 3))  # 均值滤波（还有一个方框滤波，差不多）
cv2.imshow("mean_filtering", mean_filtering)

gaussian_filtering = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波；高斯噪声
cv2.imshow("gaussian_filtering", gaussian_filtering)

median_filtering = cv2.medianBlur(img, 5)  # 中值滤波、中位数；椒盐噪声、斑点噪声
cv2.imshow("median_filtering", mean_filtering)

bilateral_filtering = cv2.bilateralFilter(img, 9, 75, 75)  # 双边滤波，保存了图像边缘特征
cv2.imshow("bilateral_filtering", bilateral_filtering)

cv2.waitKey(0)
