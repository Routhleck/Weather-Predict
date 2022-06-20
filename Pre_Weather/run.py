import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import ui
import Main_ui

class mywindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mywindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
    #设置按钮的功能
    def setupUi(self, MainWindow):
        super(mywindow, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(self.predict)
    
    #按下按钮触发函数
    def predict(self):
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
        for i in range(1,6):
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
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())