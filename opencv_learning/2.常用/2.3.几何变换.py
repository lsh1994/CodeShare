"""
@author: LiShiHang
@software: PyCharm
@file: 2.3.几何变换.py
@time: 2019/1/4 11:19
@desc:
"""
import cv2
import numpy as np

img = cv2.imread("../res/drawing.jpg")
cv2.imshow("original_picture", img)

# 缩放图片
img_zoom = cv2.resize(img, (500, 100))
img_zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("zoom_map_fixedSize", img_zoom)
cv2.imshow("zoom_map_proportional", img_zoom2)

# 翻转图片
cv2.imshow("reversal", cv2.flip(img, 1))  # 水平翻转

# 平移
M = np.float32([[1, 0, -100], [0, 1, -200]])
cv2.imshow("translation", cv2.warpAffine(img, M, img.shape[:2]))

# 旋转
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols // 2, rows // 2), 45, 1)
cv2.imshow("rotation", cv2.warpAffine(img, M, (cols, rows)))
cv2.waitKey(0)
