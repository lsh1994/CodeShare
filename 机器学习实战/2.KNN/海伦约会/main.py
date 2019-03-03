import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

def autoNorm(x):
    """
    最大值最小值归一化
    :param x: 需要归一化的特征向量
    :return: 新的数组、极差、最小值
    """
    assert isinstance(x,np.ndarray)

    minVals=x.min(axis=0)
    maxVals=x.max(axis=0)
    ranges=maxVals-minVals

    x_new=(x-minVals)/ranges # 广播

    return x_new,ranges,minVals

def getdata_normal():
    """
    读取原始文本数据
    :return:
    """
    fp="datingTestSet.txt"

    f=open(fp,mode='r')

    data=[line.strip().split('\t') for line in f.readlines()]
    data=np.array(data)

    x=data[:,:-1].astype(np.float)
    y=data[:,-1]

    f.close()

    # 可视化特征
    labels=copy.deepcopy(y)
    dic={"largeDoses": "r", "smallDoses": 'g', "didntLike": 'b'}
    for k, v in dic.items():
        labels[labels==k]=v
    plt.scatter(x[:, 0], x[:, 1], 10,labels)
    plt.title(dic)
    plt.show()

    return x,y

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
    x, y = getdata_normal()
    x, _, _ = autoNorm(x)

    total=len(x)
    splittest=int(0.9*total) # 分割训练集和测试集,训练集占比0.8
    print("分割位置：{}，总数：{}".format(splittest,total))

    trueCount=0
    for i in range(splittest,total):
        result = knnClaffify(x[i], x[:splittest],y[:splittest],k=3)
        trueCount+=(y[i]==result)

    print("正确率：{2}({0}/{1})".format(trueCount,total-splittest,trueCount/(total-splittest)))

def knnForPerson():

    x, y = getdata_normal()
    x,ranges,minVals = autoNorm(x)

    t1 = float(input("每年旅行距离："))
    t2 = float(input("玩游戏时间占比："))
    t3 = float(input("每周吃的冰激凌："))

    item=(np.array([t1,t2,t3])-minVals)/ranges
    result=knnClaffify(item,x,y,k=3)
    print("predict: ",result)

if __name__ == '__main__':

    knnTest()
    knnForPerson()


