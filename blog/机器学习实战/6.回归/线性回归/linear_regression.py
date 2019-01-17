"""
@author: LiShiHang
@software: PyCharm
@file: linear_regression.py
@time: 2018/12/21 15:06
@desc:
"""

import matplotlib.pyplot as plt
import numpy as np


def loadDataSet(fileName):
    """
    获取文件中的特征和标签
    :param fileName:
    :return:
    """
    dataMat = []
    labelMat = []
    with open(fileName) as f:
        for line in f.readlines():
            arr = line.strip().split()
            dataMat.append([float(i) for i in arr[:-1]])  # 给的数据第0列为1
            labelMat.append([float(arr[-1])])  # 注意此处标签的读取方式

    return dataMat, labelMat


def plotGit(dataArr, labelMat, w, name):
    """
    可视化
    :param dataArr:
    :param labelMat:
    :param w:
    :return:
    """
    x = [i[1] for i in dataArr]  # 第1列特征
    y = labelMat
    plt.figure(num=name)
    plt.scatter(x, y, s=5, c='r')

    px = np.linspace(min(x), max(x), 3)
    py = [w[0] + w[1] * i for i in px]
    plt.plot(px, py)


def standard_linear_regression(xarr, yarr):
    """
    线性回归，最小二乘法的曲线拟合
    :param xarr:
    :param yarr:
    :return:
    """
    xarr = np.mat(xarr)
    yarr = np.mat(yarr)

    xTx = xarr.T * xarr
    if np.linalg.det(xTx) == 0:
        print("行列式为0，不可转置。")
        return
    w = np.linalg.inv(xTx) * (xarr.T * yarr)  # 最小二乘法公式
    w = w.T.tolist()[0]

    return w


def gradAscent(xarr, yarr):
    """
    线性回归，梯度下降
    :param xarr:
    :param yarr:
    :return:
    """
    xarr = np.mat(xarr)
    yarr = np.mat(yarr)

    alpha = 0.1  # 步长，学习率
    maxCycles = 100  # 迭代次数

    weight = np.ones((xarr.shape[1], 1))

    for k in range(maxCycles):
        # 使用梯度下降算法
        grad = xarr.T * (xarr * weight - yarr) / len(xarr)  # 损失函数所得梯度

        weight = weight - alpha * grad

    weight = weight.T.tolist()[0]
    return weight


if __name__ == '__main__':

    dataMat, labelMat = loadDataSet("ex0.txt")

    w = standard_linear_regression(dataMat, labelMat)
    print(w)
    plotGit(dataMat, labelMat, w, name="最小二乘法线性回归")

    w = gradAscent(dataMat, labelMat)
    print(w)
    plotGit(dataMat, labelMat, w, name="梯度下降线性回归")

    plt.show()
