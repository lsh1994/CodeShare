"""
@author: LiShiHang
@software: PyCharm
@file: 2.2.阈值分割.py
@time: 2019/1/4 10:21
@desc: 固定阈值，自适应阈值
"""
import cv2
img = cv2.imread("../res/sudoku.jpg", 0)

ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th_adapt = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    17,
    6)  # 最终阈值等于小区域计算出的阈值再减去此值

cv2.imshow("the_original_image", img)
cv2.imshow("fixed_threshold", th)
cv2.imshow("adaptive_threshold", th_adapt)
cv2.waitKey(0)
