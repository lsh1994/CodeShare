"""
@author: LiShiHang
@software: PyCharm
@file: 1.1.图片基础.py
@time: 2019/1/3 10:10
@desc:
"""
import cv2
import numpy as np

start = cv2.getTickCount()

img = cv2.imread("../res/lena.jpg")
print(type(img))
assert isinstance(img, np.ndarray)
print(img.shape)
print(img.dtype)

end = cv2.getTickCount()

t = (end - start) * 1000 / cv2.getTickFrequency()
print("\ncost:%.3fms" % t)  # 毫秒

cv2.imshow("lena", img)
cv2.waitKey(0)
