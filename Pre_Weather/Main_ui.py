# -*- coding: utf-8 -*-
# @Time: 2020/12/16
# @Author: Eritque arcus
# @File: Main.py
import joblib
import datetime as DT
from GetModel import GetModel
import matplotlib.pyplot as plt

def predict(city):
    # 训练并保存模型并返回MAE
    r = GetModel(city = city)
    print("MAE:", r[0])
    # 读取保存的模型
    model = joblib.load('Model.pkl')

    # 最终预测结果
    preds = model.predict(r[1])
    # 反归一化或标准化，不过出bug了，不用
    # for cols in range(0, len(preds)):
    #     preds[cols] = scaler.inverse_transform(preds[cols])
    # sns.lineplot(data=preds)
    # plt.show()
    # 打印结果到控制台
    print("未来7天预测")
    all_ave_t = []
    all_high_t = []
    all_low_t = []
    all_rainfall = []
    all_pressure = []
    all_wind = []
    all_windSpeed = []
    for a in range(1, 7):
        today = DT.datetime.now()
        time = (today + DT.timedelta(days=a)).date()
        print(time.year, '/', time.month, '/', time.day,
            ': 平均气温',  round(preds[a][0], 2), '℃ ',
            '最高气温', round(preds[a][1], 2), '℃ ',
            '最低气温', round(preds[a][2], 2), '℃ ',
            "降雨量", round(preds[a][3], 2), "mm ",
            '气压', round(preds[a][4], 2), 'hPa ', end=''
            )
        if preds[a][5] <90:
            print('东北风', round(preds[a][5], 2), '° ', end='')
            all_wind.append('东北风' + str(round(preds[a][5], 2)))
        elif preds[a][5] <180:
            print('东南风', round(preds[a][5], 2), '° ', end='')
            all_wind.append('东北风' + str(round(preds[a][5], 2)))
        elif preds[a][5] <270:
            print('西南风', round(preds[a][5], 2), '° ', end='')
            all_wind.append('东北风' + str(round(preds[a][5], 2)))
        elif preds[a][5] <360:
            print('西北风', round(preds[a][5], 2), '° ', end='')
            all_wind.append('东北风' + str(round(preds[a][5], 2)))
        print('风速', round(preds[a][6], 2), 'km/h',)
        all_ave_t.append(round(preds[a][0], 2))
        all_high_t.append(round(preds[a][1], 2))
        all_low_t.append(round(preds[a][2], 2))
        all_rainfall.append(round(preds[a][3], 2))
        all_pressure.append(round(preds[a][4], 2))
        all_windSpeed.append(round(preds[a][6], 2))

    time_list = []
    today = DT.datetime.now()
    for a in range(1, 7):
        time = (today + DT.timedelta(days=a)).date()
        #合并time.year, time.month, time.day
        time_list.append(str(time.year) + '-' + str(time.month) + '-' + str(time.day))

    print(all_ave_t)
    temp = {"time":time_list ,"ave_t": all_ave_t, "high_t": all_high_t, "low_t": all_low_t, "rainfall": all_rainfall, "pressure": all_pressure, "wind": all_wind, "windSpeed": all_windSpeed}
    return temp
    '''
    # 绘画折线图
    plt.plot(range(1, 7), temp["ave_t"], color="green", label="ave_t")
    plt.plot(range(1, 7), temp["high_t"], color="red", label="high_t")
    plt.plot(range(1, 7), temp["low_t"], color="blue", label="low_t")
    plt.legend()  # 显示图例
    plt.ylabel("Temperature(°C)")
    plt.xlabel("day")
    # 显示
    plt.show()
    plt.plot(range(1, 7), temp["rainfall"], color="black", label="rainfall")
    plt.legend()
    plt.ylabel("mm")
    plt.xlabel("day")
    plt.show()
    #气压显示
    plt.plot(range(1, 7), temp["pressure"], color="black", label="pressure")
    plt.legend()
    plt.ylabel("hPa")
    plt.xlabel("day")
    plt.show()
    #风速显示
    plt.plot(range(1, 7), temp["windSpeed"], color="black", label="windSpeed")
    plt.legend()
    plt.ylabel("km/h")
    plt.xlabel("day")
    plt.show()
    '''