from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
import pysftp
import paramiko
import os
import time
from ftplib import FTP

#服务器地址
FTP_SERVER="27.54.195.137" # -- 对应 ftpe服务器地址
USER="nextai.cn"
PWD ="Vk3dxTv0gE"
FTP_PATH="/wwwroot/"
DATE= time.strftime('%Y%m%d',time.localtime(time.time()))
print(DATE)

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

    def showIcon(self):
        self.gif = QMovie('tim.gif') #实例化一个QMovie对象，传入GIF图片地址
        self.label_gif.setMovie(self.gif) #使用label的setMovie方法导入QMovie对象
        self.gif.start() #开始播放GIF动画
        time.sleep(1)

    def ftpconnect(self):
        print("connecting FTP Server, please wait...")
        ftp=FTP()
        try:
            ftp.set_debuglevel(2)
            ftp.connect(FTP_SERVER,21)
            ftp.login(USER,PWD)
        except:
            print("FTP连接失败")
            sys.exit(0)
        return ftp

    def getWelcome(self):
        ftp = self.ftpconnect()
        print(ftp.getwelcome()) #显示ftp服务器欢迎信息
        print("done")
        ftp.set_debuglevel(0) #关闭调试
#        ftp.close()
        print("connect finish!")
        ftp.quit() #退出ftp服务器
        print("quit successfuly")


    def downloadDB(self):
        ftp = self.ftpconnect()
        print(ftp.getwelcome()) #显示ftp服务器欢迎信息
        ftp.cwd('wwwroot')
        aa=ftp.nlst()
        print(aa)
        filename="nextai.db"
        file_handle=open(filename,"wb").write
        ftp.retrbinary("RETR nextai.db",file_handle,1024)
        ftp.set_debuglevel(0) #关闭调试
        ftp.quit() #退出ftp服务器
        print("download succesful !!! now closing the window")
        self.close()

    def uploadDB(self):
        ftp = self.ftpconnect()
        print(ftp.getwelcome()) #显示ftp服务器欢迎信息
        ftp.cwd('wwwroot') #进入需要操作的ftp目录
        bufsize=1024 #设置缓冲区的大小
        allFile=ftp.nlst() #获取ftp目录下所有文件名称
        allDir=ftp.dir()#获取ftp目录下所有目录名称
        print(allFile)
        print(allDir)
        filename="nextai.db"#设定需要下载的文件名称
        file_handle=open(filename,"wb").write
        ftp.retrbinary("RETR nextai.db",file_handle,bufsize)
        ftp.set_debuglevel(0) #关闭调试
        ftp.quit() #退出ftp服务器
        print("quit FTP server !!!")

    def handle_click(self):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.show()
        self.downloadDB()

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_connect.clicked.connect(self.showIcon)
        self.pushButton_connect.clicked.connect(self.downloadDB)
        self.pushButton_cancel.clicked.connect(self.close)

if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    e = MyForm()
    e.show()  #窗口显示

    app.exec_() #格式

