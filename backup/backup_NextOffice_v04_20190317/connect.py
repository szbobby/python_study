from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
import os
import time
import sqlite3

#连接数据库的配置项
config = {
          'host':'27.54.227.137',
          'port':3306,#MySQL默认端口
          'user':'nextai',#mysql默认用户名
          'password':'orTEdd6HQ3',
          'db':'nextai',#数据库
          'charset':'utf8',
          }

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.resize(413, 64)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 171, 21))
        self.label.setObjectName("label")
        self.label_gif = QtWidgets.QLabel(Form)
        self.label_gif.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label_gif.setObjectName("label_gif")
        self.pushButton_connect = QtWidgets.QPushButton(Form)
        self.pushButton_connect.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(350, 20, 51, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "正在连接服务器进行数据同步，请稍候..."))
        self.label_gif.setText(_translate("Form", ""))
        self.pushButton_connect.setText(_translate("Form", "重新连接"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))

    def database(self):
        print("opening database...")
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  # 创建游标
        curs.execute("SELECT * from customer")
        data = curs.fetchall()  # 将数据库全部内容读入data中
        curs.close()  # 关闭游标
        #        conn.commit() #保存数据库
        conn.close()  # 关闭数据库连接
        return data

    def connectMySQL(self):
        print("connecting...")
        data=self.database()
        try:
            conn = pymysql.connect(**config)
        except:
            print("fail to connect MySQL database in 27.54.227.137:90")
        cur = conn.cursor()
        sql = "INSERT INTO customer(customerID,customer,nickname1,nickname2,nickname3,contact,remark) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        for i in range (0,19):
            cur.execute(sql, (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]))
        conn.commit()  # 提交数据
        cur.close()
# 关闭数据库连接
        conn.close()
        print("done")

    def showIcon(self):
        self.gif = QMovie('tim.gif') #实例化一个QMovie对象，传入GIF图片地址
        self.label_gif.setMovie(self.gif) #使用label的setMovie方法导入QMovie对象
        self.gif.start() #开始播放GIF动画
        time.sleep(1)

    def handle_click(self):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.show()

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_connect.clicked.connect(self.showIcon)
        self.pushButton_cancel.clicked.connect(self.close)

if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    e = MyForm()
    e.show()  #窗口显示
    e.connectMySQL()
    app.exec_() #格式

