"""
@author: lishihang
@software: PyCharm
@file: id3_lenses.py
@time: 2018/11/28 21:12
"""
import math
from graphviz import Digraph


def getDataSet():
    """
    特征
    :return:
    """
    f = open("lenses.txt")

    lenses = [i.strip().split('\t') for i in f.readlines()]

    f.close()

    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']

    return lenses, lensesLabels


def calcEnt(dataSet):
    """
    计算给定数据集的信息熵
    :param dataSet:
    :return:
    """
    number = len(dataSet)
    labelCount = {}
    for fecVec in dataSet:
        label = fecVec[-1]
        labelCount[label] = labelCount.get(label, 0) + 1

    ent = 0
    for L, c in labelCount.items():
        prob = c / number
        ent -= prob * math.log2(prob)

    return ent


def splitDataSet(dataSet, column, value):
    """
    将列column中值为value的数据提出来，新数据不再包含column列表示的特征
    :param dataSet:
    :param column:
    :param value:
    :return:
    """
    retDataSet = []
    for feaVec in dataSet:
        if feaVec[column] == value:
            reducedFeaVec = feaVec[:column]
            reducedFeaVec.extend(feaVec[column + 1:])
            # reducedFeaVec+=feaVec[column + 1:]
            retDataSet.append(reducedFeaVec)

    return retDataSet


def chooseBestSplit(dataSet):
    """
    返回最好特征列值
    :param dataSet:
    :return:
    """
    numFea = len(dataSet[0]) - 1  # 特征列数，最后一列是标签
    Ent = calcEnt(dataSet)

    bestFea, bestInfoGain = -1, 0  # 最好的特征列和信息熵

    # 遍历每一列特征
    for i in range(numFea):
        uniqueVals = set([e[i] for e in dataSet])
        iEnt = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / len(dataSet)
            iEnt += prob * calcEnt(subDataSet)
        infoGain = Ent - iEnt
        if infoGain > bestInfoGain:  # 寻找信息增益最大处
            bestInfoGain = infoGain
            bestFea = i

    return bestFea


def majorityCnt(classList):
    """
    返回列表中值的频数最高的值
    :param classList:
    :return:
    """
    assert isinstance(classList, list)

    res = {i: classList.count(i) for i in set(classList)}

    res = sorted(res.items(), key=lambda x: x[0])

    return res[0][0]


def createTree(dataSet, labels):
    """
    创建决策树模型，递归
    :param dataSet:
    :param labels: 特征的名称
    :return:
    """
    classList = [e[-1] for e in dataSet]  # 标签列

    # 停止条件1: 标签列全是一个值
    if classList.count(classList[0]) == len(classList):
        # len(set(classList))==1
        return classList[0]

    # 停止条件2: 所有特征都用完了，只剩下一个标签列
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 选择最优的列，得到其含义
    bestFea = chooseBestSplit(dataSet)
    bestFeaLabel = labels[bestFea]  # 取得标签值，并从标签列中移除

    myTree = {bestFeaLabel: {}}  # 树是一个字典

    for value in set([e[bestFea] for e in dataSet]):
        subLabels = labels[:bestFea] + labels[bestFea + 1:]
        subDataSet = splitDataSet(dataSet, bestFea, value)
        myTree[bestFeaLabel][value] = createTree(subDataSet, subLabels)

    return myTree


def classifyTest(inputTree, feaLabels, testVec):
    """
    将决策树模型用于分类，递归
    :param inputTree: 决策树模型,一个嵌套的字典
    :param feaLabels: 特征的名称,运行过程中不变
    :param testVec: 测试数据
    :return:
    """
    assert isinstance(inputTree, dict)  # 决策树模型是一个字典
    assert isinstance(feaLabels, list)  # 特征名称是列表

    firstStr = list(inputTree.keys())[0]  # 字典的第一个节点，决策(子)数的根

    index = feaLabels.index(firstStr)  # 跟节点值对应的特征位置
    # testVec[index]为跟位置测试数据的值，valueOfFea是跟相邻的下一个节点
    valueOfFea = inputTree[firstStr][testVec[index]]

    if isinstance(valueOfFea, dict):
        classLabel = classifyTest(valueOfFea, feaLabels, testVec)
    else:
        classLabel = valueOfFea

    return classLabel


def plot_model(tree, name):

    g = Digraph("G", filename=name, format='png', strict=False)
    first_label = list(tree.keys())[0]
    g.node("0", first_label)
    _sub_plot(g, tree, "0")
    g.view()


root = "0"


def _sub_plot(g, tree, inc):
    global root

    first_label = list(tree.keys())[0]
    ts = tree[first_label]
    for i in ts.keys():
        if isinstance(tree[first_label][i], dict):
            root = str(int(root) + 1)
            g.node(root, list(tree[first_label][i].keys())[0])
            g.edge(inc, root, str(i))
            _sub_plot(g, tree[first_label][i], root)
        else:
            root = str(int(root) + 1)
            g.node(root, tree[first_label][i])
            g.edge(inc, root, str(i))


if __name__ == '__main__':

    # 创建数据
    dataSet, labels = getDataSet()

    # 构建决策树模型
    tree = createTree(dataSet, labels)
    print("model: ", tree)

    # 测试单个样本
    item = ["young", "hyper", "yes", "normal"]
    res = classifyTest(tree, labels, item)
    print("predict: ", item, res)

    plot_model(tree, "lenses_DT")
