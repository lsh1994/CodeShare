"""
@author: LiShiHang
@software: PyCharm
@file: bayes_remarks.py
@time: 2018/12/3 21:47
"""
# 侮辱性的语言判别，1 表示是
import numpy as np


def load_dataset():
    """
    构造数据集
    :return:
    """
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak',
                        'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]

    return posting_list, class_vec


def create_word_vector(dataset):
    """
    所有出现的单词，词汇表
    :param dataset:
    :return:
    """
    res = set([])
    for word in dataset:
        res = res.union(set(word))  # 集合并集
    return list(res)


def set_word2vec(words_list, input):
    """
    输入单条数据，在单词表中则置为1
    :param words_list:
    :param input:
    :return:
    """
    result = [0] * len(words_list)
    for word in input:
        if word in words_list:
            result[words_list.index(word)] = 1 # 每条出现多次只记一次，伯努利模型、二项独立模型
    return result


def trainNB(train_data, train_label):
    """
    朴素贝叶斯训练函数
    :param train_data:
    :param train_label:
    :return: 返回p(特征=*|类别),p(类别=1)
    """
    train_data = np.array(train_data)

    num_trainDocs = len(train_data)
    num_words = len(train_data[0])

    p_abusive = sum(train_label) / num_trainDocs  # 侮辱性言论占比 p(c_i=1)

    p0Num = np.ones(num_words)  # 每个单词（特征）出现次数累加，初始值设置为1防止分子为0
    p1Num = np.ones(num_words)
    p0Denom = 2  # 避免分母为0，初始值设为2
    p1Denom = 2

    for i in range(num_trainDocs):
        if train_label[i] == 1:

            p1Num += train_data[i]
            p1Denom+=sum(train_data[i])

        else:
            p0Num += train_data[i] # 侮辱性言论指定单词出现总数
            p0Denom+=sum(train_data[i]) # 侮辱性言论单词总数

    p0Vect = np.log(p0Num / p0Denom)  # 防止值太小,使用对数，则概率乘转换为log和
    p1Vect = np.log(p0Num / p0Denom)

    return p0Vect, p1Vect, p_abusive


def classifyNB(vec, p0Vect, p1Vect, p_abusive):
    """
    输入单条数据
    :param vec:
    :param p0Vect:
    :param p1Vect:
    :param p_abusive:
    :return:
    """
    p1 = sum(vec * p1Vect) + np.log(p_abusive)
    p0 = sum(vec * p0Vect) + np.log(1 - p_abusive)

    return int(p1 > p0)


if __name__ == '__main__':
    posting_list, class_vec = load_dataset() # 加载数据集
    word_list = create_word_vector(posting_list) # 词表
    train_data = [set_word2vec(word_list, i) for i in posting_list] # 文本转为词向量

    p0Vect, p1Vect, p_abusive = trainNB(train_data, class_vec) # 训练

    s = set_word2vec(word_list, ['love', 'my', 'dalmation']) # 测试
    print(classifyNB(s, p0Vect, p1Vect, p_abusive))

    s = set_word2vec(word_list, ['stupid', 'garbage'])
    print(classifyNB(s, p0Vect, p1Vect, p_abusive))
