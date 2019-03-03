"""
@author: LiShiHang
@software: PyCharm
@file: logistic_regression.py
@time: 2018/12/11 17:24
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
            dataMat.append([1., float(arr[0]), float(arr[1])])  # 第0列数据置为1，偏置
            labelMat.append(int(arr[2]))

    return dataMat, labelMat


def plotGit(dataArr, labelMat, weights,name):
    """
    可视化
    :param dataArr:
    :param labelMat:
    :param weights:
    :return:
    """
    x = [i[1] for i in dataArr]  # 第1列特征
    y = [i[2] for i in dataArr]  # 第2列特征
    color = ['r', 'b']
    label = [color[i] for i in labelMat]
    plt.figure(num=name)
    plt.scatter(x, y, c=label, s=20)

    px = np.linspace(min(x), max(x), 3)
    weights = weights.reshape(-1)
    py = -(weights[0] + weights[1] * px) / weights[2]

    # print(py)
    plt.plot(px, py)


def sigmoid(inx):
    return 1 / (1 + np.exp(-inx))


def gradAscent(dataMat, classLabels):
    """
    梯度下降算法普通版，批处理batch，处理所有数据
    :param dataMat:
    :param classLabels:
    :return:
    """
    dataMat = np.mat(dataMat)
    classLabels = np.mat(classLabels).transpose()

    alpha = 0.1  # 步长，学习率
    maxCycles = 100  # 迭代次数

    weight = np.ones((dataMat.shape[1], 1))

    for k in range(maxCycles):
        # 使用梯度下降算法
        grad = dataMat.transpose() * (sigmoid(dataMat * weight) - classLabels) / len(dataMat) # 损失函数所得梯度

        weight = weight - alpha * grad

    weight = np.array(weight)
    return weight


def StochasticGradientDescent(dataMat, classLabels):
    """
    梯度下降算法修改版，随机梯度下降，逐条处理数据
    :param dataMat:
    :param classLabels:
    :return:
    """
    dataMat = np.mat(dataMat)
    classLabels = np.mat(classLabels).transpose()

    maxCycles = 100  # 迭代次数

    weight = np.ones((dataMat.shape[1], 1))  # 要学习的权重
    for k in range(maxCycles):

        index = np.random.permutation(range(dataMat.shape[0]))

        for i in index:  # 随机选一个

            alpha = 1 / (k + 2) + 0.001  # 步长，学习率，逐渐减小
            grad = dataMat[i].transpose() * (sigmoid(dataMat[i] * weight) - classLabels[i])
            weight = weight - alpha * grad

    weight = np.array(weight)
    return weight


if __name__ == '__main__':

    dataMat, labelMat = loadDataSet("testSet.txt")

    weight = gradAscent(dataMat, labelMat)
    print("weight: \n", weight)
    plotGit(dataMat, labelMat, weight,"梯度下降（全部数据）")

    weight = StochasticGradientDescent(dataMat, labelMat)
    print("weight: \n", weight)
    plotGit(dataMat, labelMat, weight,"随机梯度下降（逐条）+变学习率")

    plt.show()
