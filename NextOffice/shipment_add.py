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
        Form.resize(748, 517)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(260, 20, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 59, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(540, 130, 59, 31))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 450, 221, 51))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 61, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_customer = QtWidgets.QLineEdit(Form)
        self.lineEdit_customer.setGeometry(QtCore.QRect(260, 70, 261, 31))
        self.lineEdit_customer.setObjectName("lineEdit_customer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_sales = QtWidgets.QLineEdit(Form)
        self.lineEdit_sales.setGeometry(QtCore.QRect(600, 130, 91, 31))
        self.lineEdit_sales.setText("")
        self.lineEdit_sales.setObjectName("lineEdit_sales")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 210, 61, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox_production = QtWidgets.QComboBox(Form)
        self.comboBox_production.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.comboBox_production.setObjectName("comboBox_production")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.plainTextEdit_payRecord = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_payRecord.setGeometry(QtCore.QRect(80, 250, 611, 81))
        self.plainTextEdit_payRecord.setObjectName("plainTextEdit_payRecord")
        self.lineEdit_number = QtWidgets.QLineEdit(Form)
        self.lineEdit_number.setGeometry(QtCore.QRect(80, 210, 61, 31))
        self.lineEdit_number.setText("")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 61, 31))
        self.label_11.setObjectName("label_11")
        self.comboBox_model = QtWidgets.QComboBox(Form)
        self.comboBox_model.setGeometry(QtCore.QRect(190, 160, 121, 21))
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(190, 120, 61, 41))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(360, 130, 41, 31))
        self.label_14.setObjectName("label_14")
        self.lineEdit_macID = QtWidgets.QLineEdit(Form)
        self.lineEdit_macID.setGeometry(QtCore.QRect(420, 130, 81, 31))
        self.lineEdit_macID.setText("")
        self.lineEdit_macID.setObjectName("lineEdit_macID")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 190, 681, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(180, 210, 41, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_unitPrice = QtWidgets.QLineEdit(Form)
        self.lineEdit_unitPrice.setGeometry(QtCore.QRect(220, 210, 71, 31))
        self.lineEdit_unitPrice.setText("")
        self.lineEdit_unitPrice.setObjectName("lineEdit_unitPrice")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(330, 210, 41, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_paid = QtWidgets.QLineEdit(Form)
        self.lineEdit_paid.setGeometry(QtCore.QRect(380, 210, 91, 31))
        self.lineEdit_paid.setText("")
        self.lineEdit_paid.setObjectName("lineEdit_paid")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 360, 59, 61))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_shipto = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_shipto.setGeometry(QtCore.QRect(80, 350, 331, 81))
        self.plainTextEdit_shipto.setObjectName("plainTextEdit_shipto")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(430, 360, 31, 61))
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_remark = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_remark.setGeometry(QtCore.QRect(460, 350, 231, 81))
        self.plainTextEdit_remark.setObjectName("plainTextEdit_remark")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 330, 681, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 430, 701, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(520, 210, 61, 31))
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(20, 50, 681, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_production = QtWidgets.QLabel(Form)
        self.label_production.setGeometry(QtCore.QRect(90, 130, 91, 21))
        self.label_production.setObjectName("label_production")
        self.label_model = QtWidgets.QLabel(Form)
        self.label_model.setGeometry(QtCore.QRect(260, 130, 81, 21))
        self.label_model.setObjectName("label_model")
        self.dateEdit_ship = QtWidgets.QDateEdit(Form)
        self.dateEdit_ship.setGeometry(QtCore.QRect(80, 70, 81, 31))
        self.dateEdit_ship.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_ship.setCalendarPopup(True)
        self.dateEdit_ship.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit_ship.setObjectName("dateEdit_ship")
        self.dateEdit_pay = QtWidgets.QDateEdit(Form)
        self.dateEdit_pay.setGeometry(QtCore.QRect(590, 210, 101, 31))
        self.dateEdit_pay.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_pay.setCalendarPopup(True)
        self.dateEdit_pay.setObjectName("dateEdit_pay")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(540, 70, 61, 31))
        self.label_15.setObjectName("label_15")
        self.comboBox_model_2 = QtWidgets.QComboBox(Form)
        self.comboBox_model_2.setGeometry(QtCore.QRect(600, 70, 91, 31))
        self.comboBox_model_2.setObjectName("comboBox_model_2")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")
        self.comboBox_model_2.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">新增产品出货</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">付款记录</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">业务负责</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">客户名称</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">出货产品</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">出货数量</span></p></body></html>"))
        self.comboBox_production.setItemText(0, _translate("Form", "（未选择）"))
        self.comboBox_production.setItemText(1, _translate("Form", "分选机"))
        self.comboBox_production.setItemText(2, _translate("Form", "点焊机"))
        self.comboBox_production.setItemText(3, _translate("Form", "面垫机"))
        self.comboBox_production.setItemText(4, _translate("Form", "自动产线"))
        self.comboBox_production.setItemText(5, _translate("Form", "其他"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">出货日期</span></p></body></html>"))
        self.comboBox_model.setItemText(0, _translate("Form", "（未选择）"))
        self.comboBox_model.setItemText(1, _translate("Form", "AIBAT-204"))
        self.comboBox_model.setItemText(2, _translate("Form", "AIBAT-105"))
        self.comboBox_model.setItemText(3, _translate("Form", "AIBAT-107"))
        self.comboBox_model.setItemText(4, _translate("Form", "AIBAT-111"))
        self.comboBox_model.setItemText(5, _translate("Form", "MD300"))
        self.comboBox_model.setItemText(6, _translate("Form", "MD500"))
        self.comboBox_model.setItemText(7, _translate("Form", "WM3"))
        self.comboBox_model.setItemText(8, _translate("Form", "WD300"))
        self.comboBox_model.setItemText(9, _translate("Form", "WD500"))
        self.comboBox_model.setItemText(10, _translate("Form", "WD700"))
        self.comboBox_model.setItemText(11, _translate("Form", "WS600"))
        self.comboBox_model.setItemText(12, _translate("Form", "WS800"))
        self.comboBox_model.setItemText(13, _translate("Form", "X200"))
        self.comboBox_model.setItemText(14, _translate("Form", "X500"))
        self.comboBox_model.setItemText(15, _translate("Form", "X800"))
        self.comboBox_model.setItemText(16, _translate("Form", "其他"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">规格型号</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">设备号</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">单价</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">已付款</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">出货地址</span></p><p><span style=\" font-size:10pt; font-weight:600;\">与联系人</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">备注</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">下次付款</span></p></body></html>"))
        self.label_production.setText(_translate("Form", "（未选择）"))
        self.label_model.setText(_translate("Form", "（未选择）"))
        self.dateEdit_ship.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.dateEdit_pay.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">所属地区</span></p></body></html>"))
        self.comboBox_model_2.setItemText(0, _translate("Form", "（未选择）"))
        self.comboBox_model_2.setItemText(1, _translate("Form", "广东"))
        self.comboBox_model_2.setItemText(2, _translate("Form", "浙江"))
        self.comboBox_model_2.setItemText(3, _translate("Form", "江苏"))
        self.comboBox_model_2.setItemText(4, _translate("Form", "山东"))
        self.comboBox_model_2.setItemText(5, _translate("Form", "江西"))
        self.comboBox_model_2.setItemText(6, _translate("Form", "河北"))
        self.comboBox_model_2.setItemText(7, _translate("Form", "安徽"))
        self.comboBox_model_2.setItemText(8, _translate("Form", "四川"))
        self.comboBox_model_2.setItemText(9, _translate("Form", "天津"))
        self.comboBox_model_2.setItemText(10, _translate("Form", "其他"))


### 以上是QtDesiger工具生成的代码
### 以下是自己编写的程序

    def saveToSqlite(self):
#        shipmentID=int(self.label_shipmentID.text())
        shipDate=str(self.dateEdit_ship.text())
        customer=str(self.lineEdit_customer.text())
        sales=str(self.lineEdit_sales.text())
        production=str(self.label_production.text())
        model=str(self.label_model.text())
        macID=str(self.lineEdit_macID.text())
        unitPrice=str(self.lineEdit_unitPrice.text())
        number=str(self.lineEdit_number.text())
        paid=str(self.lineEdit_paid.text())
        paidRecord=str(self.plainTextEdit_payRecord.toPlainText())
        payRemind=str(self.dateEdit_pay.text())
        shipTo=str(self.plainTextEdit_shipto.toPlainText())
        remark=str(self.plainTextEdit_remark.toPlainText())
        bit=1

### 输入格式检查，以下开始判断输入框中的单价、数量、已付款是否为空，如果为空则自动赋值为0，以防止计算出错
        if macID=="":
            macID= "0"
        if unitPrice=="":
            unitPrice="0"
        if number== "":
            number="0"
        if paid=="":
            paid="0"
#        content=[shipmentID,shipDate,customer,sales,production,model,macID,unitPrice,number,paid,paidRecord,payRemind,shipTo,remark]
        content=[shipDate,customer,sales,production,model,macID,unitPrice,number,paid,paidRecord,payRemind,shipTo,remark,bit]



###以下开始判断输入框中的项目是否符合规范，只有全部符合规范才执行else，进行保存
        if customer== "":
            QMessageBox.critical(self, "注意：客户名缺失", "请输入出货客户的名称或相应联系人以便于核对！")
            pass
        elif production== "产品名称":
            QMessageBox.critical(self, "注意：客户名缺失", "请选择出货产品名称以便于核对，如果没有合适的则选择【其他】！")
            pass
        elif macID.isdigit()== False:
            QMessageBox.critical(self, "注意：输入格式错误", "设备号应该是数字，请重新输入并注意检查后再保存")
            pass
        elif unitPrice.isdigit()==False:
            QMessageBox.critical(self, "注意：输入格式错误", "单价应该是数字，请重新输入并注意检查后再保存")
            pass
        elif number.isdigit()==False:
            QMessageBox.critical(self, "注意：输入格式错误", "数量应该是数字，请重新输入并注意检查后再保存")
            pass
        elif paid.isdigit()==False:
            QMessageBox.critical(self, "注意：输入格式错误", "已付款应该是数字，请重新输入并注意检查后再保存")
            pass
        else:
### 以下开始连接数据库
            conn = sqlite3.connect('nextai.db')
            curs = conn.cursor()  #创建游标
#            curs.execute("insert into shipment(shipmentID,shipDate,customer,sales,production,model,macID,unitPrice,number,paid,paidRecord,payRemind,shipTo,remark) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",content)
            curs.execute("insert into shipment(shipDate,customer,sales,production,model,macID,unitPrice,number,paid,paidRecord,payRemind,shipTo,remark,bit) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",content)
            print("here now")
            curs.close()  #关闭游标
            conn.commit() #保存数据库
            conn.close() #关闭数据库连接
            print ("保存数据库成功")
            self.close()


### 以下处理【新增】按钮的响应事件
    def handle_click(self):
        lens=self.dblen()
#        self.label_shipmentID.setText(str(lens+1))
        self.show()
    def dblen(self):
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
        curs.execute("SELECT * from shipment")
        data= curs.fetchall()
        lens=len(data)
        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return lens

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_production.activated[str].connect(self.label_production.setText)
        self.comboBox_model.activated[str].connect(self.label_model.setText)
        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_cancel.clicked.connect(self.close)

import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__=='__main__':
    app=QApplication(sys.argv)
    w = MyForm()
#    w.lineDisplay()
    w.show()
#    shipDate=str(w.dateEdit_ship.date())
    shipDate=str(w.dateEdit_ship.text())
    print(shipDate)

    app.exec_()

"""
    def database(self): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
        curs.execute("SELECT * from shipment")
        data= curs.fetchall()
        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return data

"""

