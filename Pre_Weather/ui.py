# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_label = QtWidgets.QLabel(self.centralwidget)
        self.check_label.setGeometry(QtCore.QRect(20, 30, 481, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(32)
        self.check_label.setFont(font)
        self.check_label.setTextFormat(QtCore.Qt.AutoText)
        self.check_label.setScaledContents(False)
        self.check_label.setAlignment(QtCore.Qt.AlignCenter)
        self.check_label.setObjectName("check_label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 50, 191, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(32)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 811, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 50, 151, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.process_label = QtWidgets.QLabel(self.centralwidget)
        self.process_label.setGeometry(QtCore.QRect(220, -20, 481, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.process_label.setFont(font)
        self.process_label.setText("")
        self.process_label.setTextFormat(QtCore.Qt.AutoText)
        self.process_label.setScaledContents(False)
        self.process_label.setAlignment(QtCore.Qt.AlignCenter)
        self.process_label.setObjectName("process_label")
        self.drawTemp = QtWidgets.QPushButton(self.centralwidget)
        self.drawTemp.setGeometry(QtCore.QRect(20, 420, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.drawTemp.setFont(font)
        self.drawTemp.setObjectName("drawTemp")
        self.drawRain = QtWidgets.QPushButton(self.centralwidget)
        self.drawRain.setGeometry(QtCore.QRect(240, 420, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.drawRain.setFont(font)
        self.drawRain.setObjectName("drawRain")
        self.drawPre = QtWidgets.QPushButton(self.centralwidget)
        self.drawPre.setGeometry(QtCore.QRect(460, 420, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.drawPre.setFont(font)
        self.drawPre.setObjectName("drawPre")
        self.drawWindSp = QtWidgets.QPushButton(self.centralwidget)
        self.drawWindSp.setGeometry(QtCore.QRect(690, 420, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(17)
        self.drawWindSp.setFont(font)
        self.drawWindSp.setObjectName("drawWindSp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_label.setText(_translate("MainWindow", "请选择查看天气的城市："))
        self.comboBox.setItemText(0, _translate("MainWindow", "广州"))
        self.comboBox.setItemText(1, _translate("MainWindow", "青岛"))
        self.comboBox.setItemText(2, _translate("MainWindow", "北京"))
        self.comboBox.setItemText(3, _translate("MainWindow", "上海"))
        self.comboBox.setItemText(4, _translate("MainWindow", "武汉"))
        self.comboBox.setItemText(5, _translate("MainWindow", "重庆"))
        self.comboBox.setItemText(6, _translate("MainWindow", "乌鲁木齐"))
        self.comboBox.setItemText(7, _translate("MainWindow", "太原"))
        self.comboBox.setItemText(8, _translate("MainWindow", "漠河"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "平均气温"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "最高气温"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "最低气温"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "降雨量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "气压"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "风向"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "风速"))
        self.pushButton.setText(_translate("MainWindow", "开始预测"))
        self.drawTemp.setText(_translate("MainWindow", "绘制气温折线图"))
        self.drawRain.setText(_translate("MainWindow", "绘制降雨量折线图"))
        self.drawPre.setText(_translate("MainWindow", "绘制气压折线图"))
        self.drawWindSp.setText(_translate("MainWindow", "绘制风速折线图"))
