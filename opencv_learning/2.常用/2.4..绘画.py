"""
@author: LiShiHang
@software: PyCharm
@file: 2.4..绘画.py
@time: 2019/1/4 13:48
@desc:
"""
import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8) * 255

# 线
cv2.line(img, (0, 0), (400, 300), (240, 12, 12), 2)

# 矩形
cv2.rectangle(img, (100, 200), (300, 300), (120, 45, 120), 2)

# 圆，填充
cv2.circle(img, (250, 250), 45, (255, 0, 0), -1)

# 椭圆，部分
cv2.ellipse(img, (100, 200), (100, 100), 0, 0, 90, (0, 255, 0), 2)

# 四边形
pts = np.array([[300, 105], [50, 10], [70, 20], [20, 30]],
               np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 255), 2)

# 多条折线
line1 = np.array([[100, 20], [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60], [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100], [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 0, 0), 2)

# 文本
cv2.putText(img, "lshhehe", (10, 400), cv2.FONT_HERSHEY_SIMPLEX,
            2, (255, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("PaintingBoard", img)
cv2.waitKey(0)
