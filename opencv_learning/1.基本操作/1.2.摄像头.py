"""
@author: LiShiHang
@software: PyCharm
@file: 1.2.摄像头.py
@time: 2019/1/3 10:44
@desc:
"""
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

print(capture.get(4), capture.get(3))  # 图像矩阵行列（高宽）

outfile = cv2.VideoWriter(
    'camera_output.avi', cv2.VideoWriter_fourcc(
        *"XVID"), 24, (640, 480))


cv2.namedWindow("frame", cv2.WINDOW_NORMAL)  # 设置窗口

while capture.isOpened():
    ret, frame = capture.read()

    frame = cv2.flip(frame, 1)

    if ret is False:
        break

    outfile.write(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):  # 返回整数编码，ord(字符);对应的chr(值)
        break
capture.release()
outfile.release()
cv2.destroyAllWindows()
