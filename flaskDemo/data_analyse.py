"""
@Time    : 2018/8/11 15:33
@Author  : Lishihang
@File    : data_analyse.py
@Software: PyCharm
@desc:
"""
import pandas as pd
import numpy as np
import jieba


def loc_counts():

    dic = {'北京': 0, '天津': 0, '河北': 0, '山西': 0, '内蒙古': 0, '辽宁': 0, '吉林': 0, '黑龙江': 0, '上海': 0, '江苏': 0, '浙江': 0,
           '安徽': 0, '福建': 0, '江西': 0, '山东': 0, '河南': 0, '湖北': 0, '湖南': 0, '广东': 0, '广西': 0, '海南': 0, '重庆': 0,
           '四川': 0, '贵州': 0, '云南': 0, '西藏': 1, '陕西': 0, '甘肃': 0, '青海': 0, '宁夏': 0, '新疆': 0, '台湾': 0, '香港': 0,
           '澳门': 0, '南海诸岛': 0}
    uknow = 0

    df = pd.read_csv(r"d:/jiansuo_log.csv")
    # print(df.shape)
    for i in df.loc[:, "LOCATION"]:
        provice = str(i).split()[1]
        if provice in dic:
            dic[provice] += 1
        else:
            uknow += 1
    # print(dic)
    return dic,uknow

def ciyun():
    df = pd.read_csv(r"d:/jiansuo_log.csv")
    data=df.iloc[:5, 1].values
    print(data)
    for i in data:
        s=jieba.cut(i)
        print(' '.join(s))

    # from wordcloud import WordCloud
    # wordcloud = WordCloud(
    #     background_color="white",
    #     max_words=2000,
    #     font_path ='C:\Windows\Fonts\simhei.ttf',
    #     # max_font_size = 50,  # 设置字体最大值
    #     stopwords="",
    #     random_state = 30,  # 设置有多少种随机生成状态，即有多少种配色方
    #     ).generate(" ".join(df.iloc[:,1].values))
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud,interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    # print(" ".join(df.iloc[:5,1].values))

if __name__ == '__main__':
    ciyun()
