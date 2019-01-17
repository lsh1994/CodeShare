"""
@author: lishihang
@software: PyCharm
@file: handwritten.py
@time: 2018/11/26 16:18
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from tqdm import tqdm


def img2vec(filename):
    f = open(filename)
    data = [list(map(int, i.strip())) for i in f.readlines()]
    data = np.array(data)

    # plt.imshow(data.reshape(32,-1),cmap='gray')
    # plt.show()

    data = data.reshape(-1)
    return data.tolist()


def readDir(dir):
    assert dir[-1] == '/'
    fs = glob.glob(dir + "*.txt")
    labels = []
    xs = []
    for f in fs:
        labels.append(os.path.split(f)[1].split('_')[0])
        xs.append(img2vec(f))

    labels = np.array(labels)
    xs = np.array(xs)

    # print(xs.shape)
    # print(labels.shape)

    return xs, labels

def knnClaffify(testItem,trainX,trainY,k):
    """
    knn分类算法，单条数据测试
    :param testItem: 测试的单条数据
    :param trainX: 训练集特征
    :param trainY: 训练集标签
    :param k: 邻居个数
    :return: 分类类别
    """
    distances=np.sqrt(np.sum((trainX-testItem)**2,axis=1))

    ind=np.argsort(distances)

    classCount={}
    for i in range(k):
        vote=trainY[ind[i]]
        classCount[vote]=classCount.get(vote,0)+1
    classCount=sorted(classCount.items(),key=lambda x:x[0])

    return classCount[0][0]

def knnTest():
    """
    测试算法
    :return:
    """
    x, y = readDir("trainingDigits/")

    x_test,y_test= readDir("testDigits/")

    print("训练集：{}，测试集：{}".format(len(y),len(y_test)))

    trueCount=0
    for x_item,y_item in tqdm(list(zip(x_test,y_test))):

        result = knnClaffify(x_item, x,y,k=5)

        trueCount+=(y_item==result)

    print("正确率：{}({}/{})".format(trueCount/len(y_test),trueCount,len(y_test)))

if __name__ == '__main__':

    # img2vec("testDigits/8_80.txt")

    knnTest()


