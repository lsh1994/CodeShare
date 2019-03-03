"""
@author: LiShiHang
@software: PyCharm
@file: 3.2.腐蚀与膨胀.py
@time: 2019/1/5 23:25
@desc: 形态学操作一般作用于二值化图
"""
import cv2
import numpy as np

img=cv2.imread("../res/j.bmp",0)
print(set(img.reshape(-1).tolist()))
cv2.imshow("OriginalPicture",img)

# 腐蚀
erosion=cv2.erode(img,np.ones((5,5)))
cv2.imshow("erorsion",erosion)

# 膨胀
dilation=cv2.dilate(img,np.ones((5,5)))
cv2.imshow("dilation",dilation)

cv2.waitKey(0)