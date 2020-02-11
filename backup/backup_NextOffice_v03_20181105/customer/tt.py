import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import NextOffice.customer.customer_browser
import NextOffice.customer.customer_add
from PyQt5.QtWidgets import QMessageBox
import NextOffice.main

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Dialog.resize(590, 688)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 61, 31))
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 110, 371, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_3.addWidget(self.label_name)
        self.label_nick1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_nick1.setObjectName("label_nick1")
        self.verticalLayout_3.addWidget(self.label_nick1)
        self.label_nick2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_nick2.setObjectName("label_nick2")
        self.verticalLayout_3.addWidget(self.label_nick2)
        self.label_nick3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_nick3.setObjectName("label_nick3")
        self.verticalLayout_3.addWidget(self.label_nick3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 610, 201, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.lineEdit_passcode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_passcode.setGeometry(QtCore.QRect(520, 640, 51, 21))
        self.lineEdit_passcode.setText("")
        self.lineEdit_passcode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passcode.setObjectName("lineEdit_passcode")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(190, 80, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_remark = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_remark.setGeometry(QtCore.QRect(100, 480, 91, 20))
        self.lineEdit_remark.setObjectName("lineEdit_remark")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(470, 640, 51, 20))
        self.label_15.setObjectName("label_15")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 59, 61))
        self.label_6.setObjectName("label_6")
        self.lineEdit_contact = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_contact.setGeometry(QtCore.QRect(100, 350, 91, 20))
        self.lineEdit_contact.setObjectName("lineEdit_contact")
        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setGeometry(QtCore.QRect(100, 60, 51, 31))
        self.label_id.setObjectName("label_id")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 61, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(200, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 100, 91, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_2.addWidget(self.lineEdit_name)
        self.lineEdit_nick1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nick1.setObjectName("lineEdit_nick1")
        self.verticalLayout_2.addWidget(self.lineEdit_nick1)
        self.lineEdit_nick2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nick2.setObjectName("lineEdit_nick2")
        self.verticalLayout_2.addWidget(self.lineEdit_nick2)
        self.lineEdit_nick3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nick3.setObjectName("lineEdit_nick3")
        self.verticalLayout_2.addWidget(self.lineEdit_nick3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 480, 59, 21))
        self.label_7.setObjectName("label_7")
        self.textBrowser_contact = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_contact.setGeometry(QtCore.QRect(210, 350, 371, 111))
        self.textBrowser_contact.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact.setLineWidth(0)
        self.textBrowser_contact.setObjectName("textBrowser_contact")
        self.textBrowser_remark = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_remark.setGeometry(QtCore.QRect(210, 480, 371, 111))
        self.textBrowser_remark.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark.setLineWidth(0)
        self.textBrowser_remark.setObjectName("textBrowser_remark")

        self.retranslateUi(Dialog)
        self.lineEdit_name.textChanged['QString'].connect(self.label_name.setText)
        self.lineEdit_nick1.textChanged['QString'].connect(self.label_nick1.setText)
        self.lineEdit_nick2.textChanged['QString'].connect(self.label_nick2.setText)
        self.lineEdit_nick3.textChanged['QString'].connect(self.label_nick3.setText)
        self.lineEdit_contact.textChanged['QString'].connect(self.textBrowser_contact.setText)
        self.lineEdit_remark.textChanged['QString'].connect(self.textBrowser_remark.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>PrimaryKey</p></body></html>"))
        self.label_name.setText(_translate("Dialog", "name"))
        self.label_nick1.setText(_translate("Dialog", "nick1"))
        self.label_nick2.setText(_translate("Dialog", "nick2"))
        self.label_nick3.setText(_translate("Dialog", "nick3"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>功能码</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "联系方式"))
        self.label_id.setText(_translate("Dialog", "0000"))
        self.label_2.setText(_translate("Dialog", "客户名称"))
        self.label_3.setText(_translate("Dialog", "简称1"))
        self.label_4.setText(_translate("Dialog", "简称2"))
        self.label_5.setText(_translate("Dialog", "简称3"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">详细信息&amp;编辑</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "备注"))

### 以上是QtDesiger工具生成的代码
### 以下是自己编写的程序
    def database1(self): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('tt1.db')
        curs = conn.cursor()  #创建游标
        print ("pageData()打开数据库成功")
#        curs.execute("SELECT * from customer;") #b必须加括号，并且要加一个逗号，以表示同一个数字，
        sql="SELECT * from customer WHERE customer LIKE '江苏';"
        sql="SELECT * from service WHERE customer LIKE"+" "+"\'%"+江苏+"%\'"
        curs.execute(sql) #sql语句只能为字符串，所以在上一行将sql的字符串添加整齐
        data= curs.fetall()
        curs.close()  #关闭游标
        conn.close() #关闭数据库连接
        return data

    def database2(self): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('tt2.db')
        curs = conn.cursor()  #创建游标
        print ("pageData()打开数据库成功")
        curs.execute("SELECT * from customer;") #b必须加括号，并且要加一个逗号，以表示同一个数字，
        data= curs.fetchone()
        curs.close()  #关闭游标
        conn.close() #关闭数据库连接
        return data



    def lineDisplay(self): #在edit中显示browser 1-5行的内容
        data1=self.database1()
        data2=self.datbase2()
        print(data1)

        self.label_id.setText(str(data[0]))
        self.lineEdit_name.setText(str(data[1]))
        self.lineEdit_nick1.setText(str(data[2]))
        self.lineEdit_nick2.setText(str(data[3]))
        self.lineEdit_nick3.setText(str(data[4]))
        self.lineEdit_contact.setText(str(data[5]))
        self.lineEdit_remark.setText(str(data[6]))

    def saveToSqlite(self):
        id=int(self.label_id.text())
        name=str(self.lineEdit_name.text())
        nick1=str(self.lineEdit_nick1.text())
        nick2=str(self.lineEdit_nick2.text())
        nick3=str(self.lineEdit_nick3.text())
        contact=self.textBrowser_contact.toPlainText()
        remark=self.textBrowser_remark.toPlainText()
        content=[name,nick1,nick2,nick3,contact,remark,id]

# 保存之前，先确认passcode是否正确，如果不正确则表示没有保存权限
        passcode=str(self.lineEdit_passcode.text())
        if passcode=="83830369":
### 以下开始连接数据库
            conn = sqlite3.connect('nextai.db')
            curs = conn.cursor()  #创建游标
            print ("打开数据库成功")
            print(id,name,nick1,nick2,nick3,contact,remark)
            curs.execute("UPDATE customer set customer=?, nickname1=?, nickname2=?,nickname3=?,contact=?,remark=? WHERE customerID=?;",content)
            curs.close()  #关闭游标
            conn.commit() #保存数据库
            conn.close() #关闭数据库连接
            self.close()
        else:
            QMessageBox.critical(self, "注意：不能保存", "您没有编辑保存的权限，或输入的功能码错误！")


class MyDialog ( QWidget, Ui_Dialog ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_cancel.clicked.connect(self.lineDisplay)


if __name__=='__main__':
    app=QApplication(sys.argv)
    w = MyDialog()
#    w.lineDisplay()
    w.show()
    app.exec_()
