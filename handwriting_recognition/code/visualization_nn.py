# python3
# -*- coding: utf-8 -*-
# @Author  : lina
# @Time    : 2018/5/22 21:20
from pylab import *
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']    # 支持中文输出

#折线图
# x = [1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000]#点的横坐标
x = np.arange(1000, 31000, 2000)
# k1 = [0.9768, 0.9814, 0.9834, 0.9834, 0.9848, 0.9842, 0.9844, 0.9854, 0.9842, 0.9846, 0.9846, 0.9846, 0.9852, 0.9848, 0.9846]#线1的纵坐标
# k2 = [0.9753, 0.9812, 0.9824, 0.9828, 0.9826, 0.9832, 0.9831, 0.9839, 0.9837, 0.9835, 0.9833, 0.9833, 0.984, 0.9836, 0.9832]#线2的纵坐标
k1 = [0.9762, 0.983, 0.9838, 0.9854, 0.9854, 0.9864, 0.9848, 0.986, 0.9854, 0.986, 0.986, 0.9854, 0.9854, 0.986, 0.9854]
k2 = [0.9746, 0.9818, 0.9829, 0.9827, 0.9837, 0.9834, 0.984, 0.9842, 0.983, 0.984, 0.9846, 0.9838, 0.9845, 0.9847, 0.9842]
plt.plot(x, k1, 's-', color='r', label="验证数据集上精度")#s-:方形
plt.plot(x, k2, 'o-', color='g', label="测试数据集上精度")#o-:圆形
plt.xticks(x)
plt.xlabel("迭代轮数")#横坐标名字
plt.ylabel("精度")#纵坐标名字
plt.legend(loc="best")#图例
plt.show()