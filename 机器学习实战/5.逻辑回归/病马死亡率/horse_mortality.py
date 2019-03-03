"""
@author: LiShiHang
@software: PyCharm
@file: horse_mortality.py
@time: 2018/12/13 14:48
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
            dataMat.append([1.]+[float(i) for i in arr[:-1]])  # 第0列数据置为1，偏置
            labelMat.append(int(float(arr[-1])))

    return dataMat, labelMat

def sigmoid(inx):
    return 1 / (1 + np.exp(-inx))

def StochasticGradientDescent(dataMat, classLabels,maxCycles=100):
    """
    梯度下降算法修改版，随机梯度下降，逐条处理数据
    :param dataMat:
    :param classLabels:
    :param maxCycles: # 迭代次数
    :return:
    """
    dataMat = np.mat(dataMat)
    classLabels = np.mat(classLabels).transpose()

    weight = np.ones((dataMat.shape[1], 1))  # 要学习的权重
    for k in range(maxCycles):

        index = np.random.permutation(range(dataMat.shape[0]))

        for i in index:  # 随机选一个

            alpha = 1 / (k + 2) + 0.001  # 步长，学习率，逐渐减小
            grad = dataMat[i].transpose() * (sigmoid(dataMat[i] * weight) - classLabels[i])
            weight = weight - alpha * grad

    weight = np.array(weight)
    return weight

def classifyLR(feas,weights):
    """
    逻辑回归分类，
    :param feas: 一条特征向量
    :param weights: 权重
    :return:
    """
    feas=np.mat(feas)
    prob=sigmoid(feas*weights)
    return int(prob>0.5)

def testOnce():
    """
    测试
    :return:
    """
    dataMat, labelMat = loadDataSet("horseColicTraining.txt")
    weight = StochasticGradientDescent(dataMat,labelMat,100)
    # 读取测试文件，测试
    testDataMat, testDatalabelMat = loadDataSet("horseColicTest.txt")

    accuracyCount=0
    for i in range(len(testDataMat)):
        accuracyCount+=int(classifyLR(testDataMat[i],weight)==testDatalabelMat[i])

    accuracyRate=accuracyCount/len(testDataMat)
    print("单次训练准确率：{:.2f}% ({}/{})".format(accuracyRate*100,accuracyCount,len(testDatalabelMat)))

    return accuracyRate


if __name__ == '__main__':

    # dataMat, labelMat = loadDataSet("horseColicTraining.txt")
    # import pandas as pd
    # data = pd.DataFrame(dataMat)
    # data[data == 0] = np.nan
    # 可以看出，数据缺失值严重，不过文件中设置为0 并不影像逻辑回归算法
    # print(data.info())

    rate=0
    numIter=5
    for k in range(numIter):
        rate+=testOnce()
    print()
    print("多次准确率平均值：%.2f%%" % (rate/numIter*100))





