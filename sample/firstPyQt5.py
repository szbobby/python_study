import lo  # 引入Log文件，引入的同时就会运行lo.py程序

import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 70, 141, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.firstPyQt5_button_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        coo = lo.co()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "母窗口"))
        self.pushButton.setText(_translate("MainWindow", coo))
     #   time.sleep(5)#效果，5秒之后显示窗口
     #   QApplication.processEvents() #效果，5秒之后显示窗口


    def firstPyQt5_button_click(self):
        doo = lo.do()
        QtWidgets.QMessageBox.information(self.pushButton,"小窗口",doo)
        lo.logit()  # 运行lo.py文件中的logit()函数

