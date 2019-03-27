"""
@author: LiShiHang
@software: PyCharm
@file: locally_weighted_LR.py
@time: 2018/12/21 16:36
@desc:
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
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


def locally_weighted_linear_regression(test_point, xarr, yarr, k):
    """
    局部加权线性回归，使用高斯核赋予附近点权重
    :param test_point: 需要预测的记录
    :param xarr:
    :param yarr:
    :param k: 高斯核函数参数，与权重衰减速率有关
    :return: 预测估计值
    """
    xarr = np.mat(xarr)
    yarr = np.mat(yarr)

    m = xarr.shape[0]
    weight = np.mat(np.eye(m))  # 由最小化函数也可以看出weight为对角矩阵

    for i in range(m):
        diff = test_point - xarr[i]
        weight[i, i] = np.exp(diff * diff.T / (-2 * k**2))  # 特征距离平方和

    xTx = xarr.T * weight * xarr
    if np.linalg.det(xTx) == 0:
        print("行列式为0，不可转置。")
        return
    # 计算回归系数
    w = np.linalg.inv(xTx) * (xarr.T * weight * yarr)  # 最小二乘法公式

    return (test_point * w).tolist()[0][0]


def lwlrTest(dataMat, labelMat, k):
    x = [i[1] for i in dataMat]  # 第1列特征
    y = labelMat
    plt.figure()
    plt.scatter(x, y, s=2, c='r', label="数据样本")

    px = np.linspace(min(x), max(x), 100)
    py = []
    for i in px:
        res = locally_weighted_linear_regression(
            test_point=np.mat([1, i]), xarr=dataMat, yarr=labelMat, k=k)
        py.append(res)
    plt.plot(px, py, label="LWLR拟合曲线 k=%.3f" % k)

    plt.legend()


if __name__ == '__main__':

    dataMat, labelMat = loadDataSet("ex0.txt")

    lwlrTest(dataMat, labelMat, k=1)
    lwlrTest(dataMat, labelMat, k=0.1)
    lwlrTest(dataMat, labelMat, k=0.01)
    lwlrTest(dataMat, labelMat, k=0.001)
    plt.show()
