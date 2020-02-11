from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
import os
import time
import _thread
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
        Form.resize(434, 159)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 371, 31))
        self.label.setObjectName("label")
        self.label_gif = QtWidgets.QLabel(Form)
        self.label_gif.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label_gif.setObjectName("label_gif")
        self.pushButton_connect = QtWidgets.QPushButton(Form)
        self.pushButton_connect.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 120, 71, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(90, 40, 371, 31))
        self.label2.setObjectName("label_2")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(90, 70, 371, 31))
        self.label3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "即将连接服务器数据库进行数据更新！"))
        self.label_gif.setText(_translate("Form", "TextLabel"))
        self.pushButton_connect.setText(_translate("Form", "开始同步"))
        self.pushButton_cancel.setText(_translate("Form", "关闭"))
        self.label2.setText(_translate("Form", "中间过程可能程序会停止响应一段时间，请耐心等候！"))
        self.label3.setText(_translate("Form", "点击“开始同步”以启动本功能，点击“关闭”取消同步。"))


    def database1(self):
        print("opening shipment database1...")
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  # 创建游标
        curs.execute("SELECT * from shipment WHERE bit=1 ")
        data = curs.fetchall()  # 将数据库全部内容读入data中
        curs.close()  # 关闭游标
        #        conn.commit() #保存数据库
        conn.close()  # 关闭数据库连接
        return data

    def database2(self):
        print("opening shipment database2...")
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  # 创建游标
        curs.execute("SELECT * from shipment WHERE bit=2 ")
        data = curs.fetchall()  # 将数据库全部内容读入data中
        curs.close()  # 关闭游标
        #        conn.commit() #保存数据库
        conn.close()  # 关闭数据库连接
        return data

    def uploadMySQL(self):
        print("starting uploadMySQL...")
        data1=self.database1()
        data2=self.database2()
# 如果查询到有bit=1与bit=2的条目大于0，则启动上传到网络mySQL，完毕后提示已同步完毕；否则直接提示已同步完毕。
        conn = pymysql.connect(**config)
        cur = conn.cursor()
        print(len(data1),len(data2))
        print(data1)
        print(data2)
        if len(data1) > 0:
            for i in range(len(data1)):
                sql = "INSERT INTO shipment(shipmentID,shipDate,customer, sales, production, model, macID, unitPrice, number, paid, paidRecord, payRemind,shipTo,remark, bit) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data1[i][13],data1[i][14])
                cur.execute(sql,val)
        print("data1 finish")
        if len(data2) > 0:
            for j in range (len(data2)):
                val2=(data2[j][1], data2[j][2], data2[j][3], data2[j][4], data2[j][5], data2[j][6],data2[j][7], data2[j][8], data2[j][9], data2[j][10], data2[j][11], data2[j][12], data2[j][13],data2[j][14],data2[j][0])
                sql2 = "UPDATE shipment set shipDate=%s,customer=%s,sales=%s,production=%s,model=%s,macID=%s,unitPrice=%s,number=%s,paid=%s,paidRecord=%s,payRemind=%s,shipTo=%s,remark=%s,bit=%s WHERE shipmentID=%s"
                print("here now")
                cur.execute(sql2,val2)
                print("here here now")

        conn.commit()  # 提交数据
        cur.close()
        conn.close()


# 上传同步完成后，需要把本地数据库标志位置零
        self.setZero()

    def showIcon(self,threadName,delay):
        self.gif = QMovie('tim.gif') #实例化一个QMovie对象，传入GIF图片地址
        self.label_gif.setMovie(self.gif) #使用label的setMovie方法导入QMovie对象
        self.gif.start() #开始播放GIF动画
        time.sleep(delay)
    def handle_click(self):
        self.show()
#        self.label.setText("正在连接服务器，请稍候...")
#        self.showIcon()
        self._thread.start_new_thread(e.showIcon, ("thread-sub", 1))
        print("done")
        self.uploadMySQL()
    def setZero(self):
        print("starting setZero...")
        sqconn = sqlite3.connect('nextai.db')
        curs = sqconn.cursor()  # 创建游标
        data1=self.database1()
        data2=self.database2()
# 上传同步完成后，需要把本地数据库标志位置零
        print(len(data1),len(data2))
        if len(data1)>0:
            for i in range (len(data1)):
                sql="UPDATE shipment set bit=? WHERE shipmentID=?;"
                val=(0,data1[i][0])
                curs.execute(sql,val)

        if len(data2)>0:
            for j in range (len(data2)):
                sql="UPDATE shipment set bit=? WHERE shipmentID=?;"
                val=(0,data2[j][0])
                curs.execute(sql,val)
        curs.close()  # 关闭游标
        sqconn.commit()  # 保存数据库
        sqconn.close()  # 关闭数据库连接
        print("setZero done!")
        self.label.setText("数据已同步更新完毕！")
        self.label2.setText("")
        self.label3.setText("")

    def print_time( self,threadName,delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_connect.clicked.connect(self.uploadMySQL)
        self.pushButton_cancel.clicked.connect(self.close)


if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    e = MyForm()
    e.show()  #窗口显示
    _thread.start_new_thread(e.showIcon,("thread-sub",1))
#    _thread.start_new_thread(e.print_time,("thread-time",1))
#    e.showIcon()
    time.sleep(0)
#    e.uploadMySQL()
    app.exec_() #格式

"""
mySQL管理：http://27.54.227.137:90/   user: nextai, pass: orTEdd6HQ3
"""
