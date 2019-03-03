"""
@author: LiShiHang
@software: PyCharm
@file: 2.6.直方图.py
@time: 2019/1/7 16:24
@desc: 
"""
import cv2
import matplotlib.pyplot as plt

cmap="gray" # 或者None

img=cv2.imread("../res/hist.jpg",0)
plt.figure("原灰度图")
plt.imshow(img,cmap=cmap)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure("原灰度图直方图")
plt.plot(hist)

equ=cv2.equalizeHist(img)
plt.figure("直方图均衡化后图")
plt.imshow(equ,cmap=cmap)

plt.figure("直方图均衡化后图的直方图")
plt.hist(equ.flatten(),256,[0,256])

clahe=cv2.createCLAHE(clipLimit=2,tileGridSize=(8,8))
cl1=clahe.apply(img)
plt.figure("自适应直方图均衡化后图")
plt.imshow(img,cmap=cmap)

plt.show()