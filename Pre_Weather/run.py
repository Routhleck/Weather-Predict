import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import ui
import Main_ui
import matplotlib.pyplot as plt

#定义全局变量weatherInfo
weatherInfo = {}
class mywindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mywindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
    #设置按钮的功能
    def setupUi(self, MainWindow):
        super(mywindow, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(self.predict)
        self.drawTemp.clicked.connect(self.draw_temp)
        self.drawRain.clicked.connect(self.draw_rain)
        self.drawPre.clicked.connect(self.draw_press)
        self.drawWindSp.clicked.connect(self.draw_wind)
    
    #预测按钮的功能
    def predict(self):
        global weatherInfo
        #获取下拉框的值
        city = self.comboBox.currentText()
        #进行预测
        self.process_label.setText("预测中...")
        self.process_label.setStyleSheet("color:red")
        self.process_label.repaint()
        self.process_label.update()
        self.process_label.show()
        weatherInfo = Main_ui.predict(city)
        #将weatherInfo添加到tableWidget中
        for i in range(0,7):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(weatherInfo["time"][i])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(weatherInfo["ave_t"][i])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(weatherInfo["high_t"][i])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(weatherInfo["low_t"][i])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(weatherInfo["rainfall"][i])))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(weatherInfo["pressure"][i])))
            self.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(weatherInfo["wind"][i])))
            self.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(weatherInfo["windSpeed"][i])))
        self.process_label.setText("预测完成")
        self.process_label.setStyleSheet("color:green")
        self.process_label.repaint()
        self.process_label.update()
        self.process_label.show()

    def draw_temp(self):
        #判断weatherInfo是否为空
        if weatherInfo == None:
            self.process_label.setText("请先预测")
            self.process_label.setStyleSheet("color:red")
            self.process_label.repaint()
            self.process_label.update()
            self.process_label.show()
        else:
            #将字符串去掉最后的字符并转化为float
            ave_t = [float(i.strip("℃")) for i in weatherInfo["ave_t"]]
            high_t = [float(i.strip("℃")) for i in weatherInfo["high_t"]]
            low_t = [float(i.strip("℃")) for i in weatherInfo["low_t"]]
            plt.plot(range(1, 8), ave_t, color="green", label="ave_t")
            plt.plot(range(1, 8), high_t, color="red", label="high_t")
            plt.plot(range(1, 8), low_t, color="blue", label="low_t")
            plt.legend()  # 显示图例
            plt.ylabel("Temperature(°C)")
            plt.xlabel("day")
            plt.show()

    def draw_rain(self):
        #判断weatherInfo是否为空
        if weatherInfo == None:
            self.process_label.setText("请先预测")
            self.process_label.setStyleSheet("color:red")
            self.process_label.repaint()
            self.process_label.update()
            self.process_label.show()
        else:
            #将字符串去掉最后的字符并转化为float
            rainfall = [float(i.strip("mm")) for i in weatherInfo["rainfall"]]
            plt.plot(range(1, 8), rainfall, color="black", label="rainfall")
            plt.legend()
            plt.ylabel("mm")
            plt.xlabel("day")
            plt.show()
    
    def draw_press(self):
        #判断weatherInfo是否为空
        if weatherInfo == None:
            self.process_label.setText("请先预测")
            self.process_label.setStyleSheet("color:red")
            self.process_label.repaint()
            self.process_label.update()
            self.process_label.show()
        else:
            #将字符串去掉最后的字符并转化为float
            pressure = [float(i.strip("hPa")) for i in weatherInfo["pressure"]]
            plt.plot(range(1, 8), pressure, color="black", label="pressure")
            plt.legend()
            plt.ylabel("hPa")
            plt.xlabel("day")
            plt.show()
    
    def draw_wind(self):
        #判断weatherInfo是否为空
        if weatherInfo == None:
            self.process_label.setText("请先预测")
            self.process_label.setStyleSheet("color:red")
            self.process_label.repaint()
            self.process_label.update()
            self.process_label.show()
        else:
            #将字符串去掉最后的字符并转化为float
            windSpeed = [float(i.strip("km/h")) for i in weatherInfo["windSpeed"]]
            plt.plot(range(1, 8), windSpeed, color="black", label="wind")
            plt.legend()
            plt.ylabel("m/s")
            plt.xlabel("day")
            plt.show()


if __name__ == "__main__":
    # 适应高DPI设备
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 适应Windows缩放
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())