"""
@author: LiShiHang
@software: PyCharm
@file: 2.1.颜色空间转换.py
@time: 2019/1/3 14:59
@desc: BGR->HSV，追踪特定颜色物体
"""
import cv2
import numpy as np

capture = cv2.VideoCapture("../res/demo_video.mp4")

# 蓝色的范围
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

# 绿色的范围
lower_green = np.array([40, 90, 90])
upper_green = np.array([70, 255, 255])

# 红色的范围
lower_red = np.array([160, 120, 120])
upper_red = np.array([179, 255, 255])


while capture.isOpened():
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # 3.将所有的mask相加，就可以同时显示了
    mask = mask_blue + mask_green + mask_red

    print(mask.shape)
    print(set(mask.reshape(-1).tolist()))  # {0,255}

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(24) == ord('q'):
        break
