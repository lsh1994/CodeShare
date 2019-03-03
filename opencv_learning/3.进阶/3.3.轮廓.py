"""
@author: LiShiHang
@software: PyCharm
@file: 3.3.轮廓.py
@time: 2019/1/7 10:08
@desc: 轮廓是连续的，边缘并不全都连续；寻找轮廓的操作一般用于二值化图，寻找轮廓是针对白色物体的
"""
import cv2
import numpy as np

img = cv2.imread("../res/handwriting.jpg")  # 读取彩色图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图

# 阈值分割，反色，返回二值化图
_, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 寻找轮廓
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("轮廓数",len(contours))

# 绘制轮廓
contour_drawing = img.copy()
cv2.drawContours(contour_drawing, contours, -1, (0, 0, 255), 1)

cv2.imshow("OriginalPicture", img)
cv2.imshow("thresh", thresh)
cv2.imshow("contour_drawing", contour_drawing)

# ------------------------------------------------------------------
# 计算轮廓特征，根据几何方法算出来的而非像素点数
cnt = contours[0]  # 数字3的轮廓
calculation_feature=img.copy()
cv2.drawContours(calculation_feature, [cnt], -1, (0, 0, 255), 1)

print("面积",cv2.contourArea(cnt))  # 轮廓面积
print("周长",cv2.arcLength(cnt,True)) # 轮廓周长
print("图像矩",cv2.moments(cnt)) # 图像矩，包括面积，质心等

# 外接矩形
x,y,w,h=cv2.boundingRect(cnt)
cv2.rectangle(calculation_feature,(x,y),(x+w,y+h),(0,255,0),2) # 外接矩形

rect=cv2.minAreaRect(cnt)
box=np.array(cv2.boxPoints(rect)).astype(np.int)
cv2.drawContours(calculation_feature,[box],0,(255,0,0),2) # 最小外接矩形，蓝色

cv2.imshow("calculationFeature",calculation_feature)

# 形状匹配
print("数字3距离",cv2.matchShapes(contours[0],contours[0],1,0)) # 数字3
print("数字3和1距离",cv2.matchShapes(contours[0],contours[1],1,0)) # 数字3和1

# opencv显示图
cv2.waitKey(0)
