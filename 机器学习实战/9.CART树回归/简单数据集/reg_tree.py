"""
@author: LiShiHang
@software: PyCharm
@file: reg_tree.py
@time: 2019/3/4 11:52
@desc: 
"""


def bin_split(dataset,feature,value):
    """
    根据feature的value将数据一份为2
    :param dataset:
    :param feature:
    :param value:
    :return:
    """
    left = dataset[dataset[:,feature]<value]