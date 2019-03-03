"""
@author: LiShiHang
@software: PyCharm
@file: bybes_spam.py
@time: 2018/12/11 14:57
"""
import numpy as np
import glob
import re


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

def textParse(text):
    """
    将文本内容转为单词向量
    :param text:
    :return:
    """
    listOfTokens=re.split(r'\W+',text)
    return [tok.lower() for tok in listOfTokens if len(tok)>2] # 两个字母之上，转为小写

def spamTest():
    """
    训练并验证
    :return:
    """
    docList=[]
    classList=[]

    for f,f2 in zip(glob.glob("email/ham/*.txt"),glob.glob("email/spam/*.txt")) : # 书籍配套代码 ham/23.txt有非法字符，应该删除
        with open(f,'r') as file:
            docList.append(textParse(file.read()))
            classList.append(0)

        with open(f2,'r') as file2:
            docList.append(textParse(file2.read()))
            classList.append(1)

    vocabList=create_word_vector(docList)

    # 随机，使用后num个用于测试
    rd=np.random.permutation(len(docList))
    num=20

    trainMat=[]
    trainClasses=[]
    for idx in rd[:-num]:
        trainMat.append(set_word2vec(vocabList,docList[idx]))
        trainClasses.append(classList[idx])
    p0V,p1V,pSpam=trainNB(trainMat,trainClasses)

    errorCount=0
    for idx in rd[-num:]:
        if classifyNB(set_word2vec(vocabList,docList[idx]),p0V,p1V,pSpam)!=classList[idx]:
            errorCount+=1

    print("正确率：{2:.2f}({0}/{1})".format(errorCount,num,errorCount/num))


if __name__ == '__main__':

    spamTest()
