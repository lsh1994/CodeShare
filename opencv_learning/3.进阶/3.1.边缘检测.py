"""
@author: LiShiHang
@software: PyCharm
@file: 3.1.边缘检测.py
@time: 2019/1/4 15:47
@desc:
"""
import cv2
import numpy as np

img = cv2.imread("../res/handwriting.jpg", 0)
print(img.shape)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)  # 先阈值分割
edges = cv2.Canny(thresh, 30, 80)  # 然后边缘检测

cv2.imshow("The original image", img)
cv2.imshow("threshold_segmentation", thresh)
cv2.imshow("cannyEdgeDetection", edges)
cv2.waitKey(0)
