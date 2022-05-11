import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras  # 这里可能很多人报错没有keras模块，我直接在阿里云天池平台跑的数据，本地电脑的python需要调整下tensorflow版本等问题
import tensorflow as tf
import os

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



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
# 数据均值化
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
x = min_max_scaler.transform(X)  # 均值化处理
# x_ = min_max_scaler.transform([[24.5,25.0,24.0,25.0,21.0,20.5,21.0]])#这里随便取一组数据，作为后面预测用，注意数据维度

y = Y
# 划分数据集,按训练集:测试集=8:2比例划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 模型结构，采用relu函数为激活函数，输入层为N个属性
# 下面为4层隐含层，每层的神经元个数依次为1600,1000,750,500
# 输入层对应N个属性
model = keras.Sequential([
    keras.layers.Dense(1600, activation='relu', input_shape=[N]),
    keras.layers.Dense(1000, activation='relu'),
    keras.layers.Dense(750, activation='relu'),
    keras.layers.Dense(500, activation='relu'),
    keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
# 定义损失函数loss，采用的优化器optimizer为Adam
model.compile(loss='mean_absolute_error', optimizer='Adam')
# 开始训练模型
model.fit(x_train, y_train, batch_size=258, epochs=20000)  # 训练20000个批次，每个批次数据量为258

# 保存TensorFlow model
model.save('model.h5')