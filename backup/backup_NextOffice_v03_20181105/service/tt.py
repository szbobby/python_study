# -*- coding: utf-8 -*-
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.resize(566, 516)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(220, 20, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(320, 260, 59, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 70, 59, 61))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 450, 221, 51))
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 340, 59, 61))
        self.label_8.setObjectName("label_8")
        self.comboBox_method = QtWidgets.QComboBox(Form)
        self.comboBox_method.setGeometry(QtCore.QRect(100, 250, 151, 22))
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(100, 90, 181, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 72, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 51, 41))
        self.label_5.setObjectName("label_5")
        self.lineEdit_staff = QtWidgets.QLineEdit(Form)
        self.lineEdit_staff.setGeometry(QtCore.QRect(390, 90, 81, 31))
        self.lineEdit_staff.setText("")
        self.lineEdit_staff.setObjectName("lineEdit_staff")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(320, 130, 59, 61))
        self.label_9.setObjectName("label_9")
        self.comboBox_classify = QtWidgets.QComboBox(Form)
        self.comboBox_classify.setGeometry(QtCore.QRect(390, 230, 91, 22))
        self.comboBox_classify.setObjectName("comboBox_classify")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(320, 200, 51, 31))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(290, 90, 20, 321))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit_problem = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_problem.setGeometry(QtCore.QRect(100, 130, 181, 81))
        self.plainTextEdit_problem.setObjectName("plainTextEdit_problem")
        self.plainTextEdit_solution = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_solution.setGeometry(QtCore.QRect(100, 320, 181, 101))
        self.plainTextEdit_solution.setObjectName("plainTextEdit_solution")
        self.plainTextEdit_remark = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_remark.setGeometry(QtCore.QRect(320, 290, 211, 131))
        self.plainTextEdit_remark.setObjectName("plainTextEdit_remark")
        self.label_classify = QtWidgets.QLabel(Form)
        self.label_classify.setGeometry(QtCore.QRect(390, 200, 71, 31))
        self.label_classify.setObjectName("label_classify")
        self.label_method = QtWidgets.QLabel(Form)
        self.label_method.setGeometry(QtCore.QRect(100, 220, 161, 31))
        self.label_method.setObjectName("label_method")
        self.lineEdit_charge = QtWidgets.QLineEdit(Form)
        self.lineEdit_charge.setGeometry(QtCore.QRect(390, 150, 81, 31))
        self.lineEdit_charge.setText("")
        self.lineEdit_charge.setObjectName("lineEdit_charge")
        self.dateEdit_handle = QtWidgets.QDateEdit(Form)
        self.dateEdit_handle.setGeometry(QtCore.QRect(100, 280, 110, 31))
        self.dateEdit_handle.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_handle.setCalendarPopup(True)
        self.dateEdit_handle.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit_handle.setObjectName("dateEdit_handle")
        self.label_serviceID = QtWidgets.QLabel(Form)
        self.label_serviceID.setGeometry(QtCore.QRect(100, 50, 101, 31))
        self.label_serviceID.setObjectName("label_serviceID")

        self.retranslateUi(Form)
        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_cancel.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">新增售后信息</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "备注"))
        self.label_6.setText(_translate("Form", "处理人员"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.label_8.setText(_translate("Form", "解决方法"))
        self.comboBox_method.setItemText(0, _translate("Form", "远程处理（电话/微信）"))
        self.comboBox_method.setItemText(1, _translate("Form", "上门服务"))
        self.label.setText(_translate("Form", "售后ID"))
        self.label_2.setText(_translate("Form", "客户名称"))
        self.label_3.setText(_translate("Form", "客户反馈问题"))
        self.label_4.setText(_translate("Form", "处理方式"))
        self.label_5.setText(_translate("Form", "处理时间"))
        self.label_9.setText(_translate("Form", "收费金额"))
        self.comboBox_classify.setItemText(0, _translate("Form", "装配问题"))
        self.comboBox_classify.setItemText(1, _translate("Form", "零件质量问题"))
        self.comboBox_classify.setItemText(2, _translate("Form", "产品设计问题"))
        self.comboBox_classify.setItemText(3, _translate("Form", "使用不当"))
        self.label_10.setText(_translate("Form", "问题归类"))
        self.label_classify.setText(_translate("Form", "问题归类"))
        self.label_method.setText(_translate("Form", "处理时间"))
        self.dateEdit_handle.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_serviceID.setText(_translate("Form", "0000"))


    def saveToSqlite(self):
#        serviceID=int(self.label_serviceID.text())
        customer=str(self.lineEdit_name.text())
        problem=str(self.plainTextEdit_problem.toPlainText())
        method=str(self.label_method.text())
        handlingTime=str(self.dateEdit_handle.text())
        staff=str(self.lineEdit_staff.text())
        solution=str(self.plainTextEdit_solution.toPlainText())
        charge=str(self.lineEdit_charge.text())
        classify=str(self.label_classify.text())
        remark=str(self.plainTextEdit_remark.toPlainText())

###以下开始判断输入框中的费用是否为空，如果为空则自动赋值为0，以防止计算出错
        if charge=="":
            charge= "0"
        content=[customer,problem,method,handlingTime,staff,solution,charge,classify,remark]
#        content=[serviceID,customer,problem,method,handlingTime,staff,solution,charge,classify,remark]

###以下开始判断输入框中的项目是否符合规范，只有全部符合规范才执行else，进行保存
        if charge.isdigit()== False:
            QMessageBox.critical(self, "注意：输入格式错误", "设备号应该是数字，请重新输入并注意检查后再保存")
#            pass
        else:
### 以下开始连接数据库
            conn = sqlite3.connect('nextai.db')
            curs = conn.cursor()  #创建游标
            curs.execute("insert into service(customer, problem, method,handlingTime,staff,solution,charge,classify,remark) values (?,?,?,?,?,?,?,?,?)",content)
#        curs.execute("UPDATE service set customer=?, problem=?,method=?,handlingTime=?,staff=?,solution=?,charge=?,classify=?,remark=? WHERE serviceID=?;",content)
            curs.close()  #关闭游标
            conn.commit() #保存数据库
            conn.close() #关闭数据库连接
            print ("写入数据库成功") #此项要用try出错控制语句重写，如果写入有问题就提示。
            self.close()


    def dblen(self):
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
        curs.execute("SELECT * from service")
        data= curs.fetchall()
        lens=len(data)
        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return lens


    def handle_click(self):
        lens=self.dblen()
        self.label_serviceID.setText(str(lens+1))
        self.show()

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_method.activated[str].connect(self.label_method.setText)
        self.comboBox_classify.activated[str].connect(self.label_classify.setText)
     #   self.lineEdit.textChanged.connect(self.textBrowser.setText)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w = MyForm()
    w.show()
    app.exec_()