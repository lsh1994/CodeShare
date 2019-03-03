"""
@author: LiShiHang
@software: PyCharm
@file: 3.5.霍夫变换.py
@time: 2019/1/8 18:52
@desc:
"""
import cv2
import numpy as np

img = cv2.imread("../res/shapes.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("OriginalGrayscaleMap", img_gray)

edges = cv2.Canny(img_gray, 50, 150)
cv2.imshow("edgeDetection", edges)

drawing = np.ones(img.shape[:], dtype=np.uint8)*255
# 统计概率霍夫直线变换
lines = cv2.HoughLinesP(
    edges,
    0.8,
    np.pi / 180,
    90,
    minLineLength=50,
    maxLineGap=10)
for ls in lines:
    x1, y1, x2, y2 = ls[0]
    cv2.line(drawing, (x1, y1), (x2, y2),(0, 0, 255), 1,cv2.LINE_AA)
# 霍夫圆变换
circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param2=30)
print(circles)
for c in circles:
    x,y,r=c[0]
    cv2.circle(drawing,(x,y),r,(0,255,0),1)
cv2.imshow("houghCircleTransformation",drawing)

cv2.waitKey(0)
