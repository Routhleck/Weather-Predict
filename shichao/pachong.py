from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras  # 这里可能很多人报错没有keras模块，我直接在阿里云天池平台跑的数据，本地电脑的python需要调整下tensorflow版本等问题


def read_data(N):
    df = pd.read_csv('data.txt', header=None)  # 没有列名，为None
    data = df.values  # 提取数据内容
    X = []
    Y = []
    for i in range(N, len(data)):
        s = []
        for j in range(i - N, i):
            s.append(data[j][0])
        X.append(s)
        Y.append(data[i][0])
    return np.array(X), np.array(Y)


N = 7  # 特征数目
X, Y = read_data(N)
print(X)
print(Y)

min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
x = min_max_scaler.transform(X)#均值化处理
x_ = min_max_scaler.transform([[24.5,25.0,24.0,25.0,21.0,20.5,21.0]])#这里随便取一组数据，作为后面预测用，注意数据维度
print(x_)
