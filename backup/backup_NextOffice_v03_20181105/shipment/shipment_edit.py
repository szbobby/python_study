import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
import NextOffice.shipment.shipment_browser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate,   QDateTime , QTime
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.resize(870, 593)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(350, 20, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 59, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(680, 100, 59, 21))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 530, 221, 51))
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 100, 51, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_customer = QtWidgets.QLineEdit(Form)
        self.lineEdit_customer.setGeometry(QtCore.QRect(470, 90, 181, 31))
        self.lineEdit_customer.setObjectName("lineEdit_customer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_sales = QtWidgets.QLineEdit(Form)
        self.lineEdit_sales.setGeometry(QtCore.QRect(740, 90, 81, 31))
        self.lineEdit_sales.setText("")
        self.lineEdit_sales.setObjectName("lineEdit_sales")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 51, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox_production = QtWidgets.QComboBox(Form)
        self.comboBox_production.setGeometry(QtCore.QRect(80, 180, 91, 22))
        self.comboBox_production.setObjectName("comboBox_production")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.plainTextEdit_payRecord = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_payRecord.setGeometry(QtCore.QRect(80, 280, 741, 91))
        self.plainTextEdit_payRecord.setObjectName("plainTextEdit_payRecord")
        self.lineEdit_number = QtWidgets.QLineEdit(Form)
        self.lineEdit_number.setGeometry(QtCore.QRect(80, 230, 81, 31))
        self.lineEdit_number.setText("")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(200, 90, 51, 31))
        self.label_11.setObjectName("label_11")
        self.comboBox_model = QtWidgets.QComboBox(Form)
        self.comboBox_model.setGeometry(QtCore.QRect(270, 180, 91, 21))
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
        self.label_12.setGeometry(QtCore.QRect(210, 150, 51, 21))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(420, 160, 41, 31))
        self.label_14.setObjectName("label_14")
        self.lineEdit_macID = QtWidgets.QLineEdit(Form)
        self.lineEdit_macID.setGeometry(QtCore.QRect(470, 160, 81, 31))
        self.lineEdit_macID.setText("")
        self.lineEdit_macID.setObjectName("lineEdit_macID")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 210, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(210, 230, 41, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_unitPrice = QtWidgets.QLineEdit(Form)
        self.lineEdit_unitPrice.setGeometry(QtCore.QRect(250, 230, 81, 31))
        self.lineEdit_unitPrice.setText("")
        self.lineEdit_unitPrice.setObjectName("lineEdit_unitPrice")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(400, 230, 41, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_paid = QtWidgets.QLineEdit(Form)
        self.lineEdit_paid.setGeometry(QtCore.QRect(450, 230, 81, 31))
        self.lineEdit_paid.setText("")
        self.lineEdit_paid.setObjectName("lineEdit_paid")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(18, 390, 61, 61))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_shipto = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_shipto.setGeometry(QtCore.QRect(80, 390, 321, 111))
        self.plainTextEdit_shipto.setObjectName("plainTextEdit_shipto")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(430, 390, 31, 61))
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_remark = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_remark.setGeometry(QtCore.QRect(470, 390, 351, 121))
        self.plainTextEdit_remark.setObjectName("plainTextEdit_remark")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 370, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 510, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(550, 230, 81, 31))
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(20, 60, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_production = QtWidgets.QLabel(Form)
        self.label_production.setGeometry(QtCore.QRect(80, 150, 91, 21))
        self.label_production.setObjectName("label_production")
        self.label_model = QtWidgets.QLabel(Form)
        self.label_model.setGeometry(QtCore.QRect(280, 150, 81, 21))
        self.label_model.setObjectName("label_model")
        self.dateEdit_ship = QtWidgets.QDateEdit(Form)
        self.dateEdit_ship.setGeometry(QtCore.QRect(260, 90, 110, 31))
        self.dateEdit_ship.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_ship.setCalendarPopup(True)
        self.dateEdit_ship.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit_ship.setObjectName("dateEdit_ship")
        self.dateEdit_pay = QtWidgets.QDateEdit(Form)
        self.dateEdit_pay.setGeometry(QtCore.QRect(650, 230, 101, 31))
        self.dateEdit_pay.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_pay.setCalendarPopup(True)
        self.dateEdit_pay.setObjectName("dateEdit_pay")
        self.lineEdit_passcode = QtWidgets.QLineEdit(Form)
        self.lineEdit_passcode.setGeometry(QtCore.QRect(770, 550, 51, 21))
        self.lineEdit_passcode.setText("")
        self.lineEdit_passcode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passcode.setObjectName("lineEdit_passcode")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(720, 550, 51, 20))
        self.label_15.setObjectName("label_15")
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setGeometry(QtCore.QRect(110, 90, 51, 31))
        self.label_id.setObjectName("label_id")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">详细信息&amp;编辑</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">付款记录</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">业务负责</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">shipmentID</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">客户名称</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">出货产品</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">出货数量</span></p></body></html>"))
        self.comboBox_production.setItemText(0, _translate("Form", "（请选择）"))
        self.comboBox_production.setItemText(1, _translate("Form", "分选机"))
        self.comboBox_production.setItemText(2, _translate("Form", "点焊机"))
        self.comboBox_production.setItemText(3, _translate("Form", "面垫机"))
        self.comboBox_production.setItemText(4, _translate("Form", "PACK自动产线"))
        self.comboBox_production.setItemText(5, _translate("Form", "其他"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">出货日期</span></p></body></html>"))
        self.comboBox_model.setItemText(0, _translate("Form", "（请选择）"))
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
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">规格型号</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">设备号</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">单价</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">已付款</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">出货地址</span></p><p><span style=\" font-weight:600;\">与联系人</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">备注</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">下次付款时间</span></p></body></html>"))
        self.label_production.setText(_translate("Form", "（无）"))
        self.label_model.setText(_translate("Form", "（无）"))
        self.dateEdit_ship.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.dateEdit_pay.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p>功能码</p></body></html>"))
        self.label_id.setText(_translate("Form", "0000"))

### 以上是QtDesiger工具生成的代码
### 以下是自己编写的程序
    def database(self,b): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("pageData()打开数据库成功")
        curs.execute("SELECT * from shipment WHERE shipmentID=?;",(b,)) #b必须加括号，并且要加一个逗号，以表示同一个数字，
        data= curs.fetchone()
        curs.close()  #关闭游标
        conn.close() #关闭数据库连接
        return data

    def lineDisplay(self,b): #在edit中显示browser 1-5行的内容
        data=self.database(b)

        self.label_id.setText(str(data[0])) #数据库是从0开始的，所以减1
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
        shipdate=data[1]
        sdate=shipdate.split("-")
        sdate1=int(sdate[0])
        sdate2=int(sdate[1])
        sdate3=int(sdate[2])
        self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#       self.dateEdit_ship.setDate(data[p-1][1])
        self.lineEdit_customer.setText(str(data[2]))
        self.lineEdit_sales.setText(str(data[3]))
        self.label_production.setText(str(data[4]))
        self.label_model.setText(str(data[5]))
        self.lineEdit_macID.setText(str(data[6]))
        self.lineEdit_unitPrice.setText(str(data[7]))
        self.lineEdit_number.setText(str(data[8]))
        self.lineEdit_paid.setText(str(data[9]))
        self.plainTextEdit_payRecord.setPlainText(str(data[10]))
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
        paydate=data[11]
        pdate=paydate.split("-")
        pdate1=int(pdate[0])
        pdate2=int(pdate[1])
        pdate3=int(pdate[2])
        self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#         self.dateEdit_pay.setDate(str(data[p-1][11]))
        self.plainTextEdit_shipto.setPlainText(str(data[12]))
        self.plainTextEdit_remark.setPlainText(str(data[13]))

    def saveToSqlite(self):
        id=int(self.label_id.text())
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
        content=[shipDate,customer,sales,production,model,macID,unitPrice,number,paid,paidRecord,payRemind,shipTo,remark,id]
        if macID.isdigit()== False:
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
# 保存之前，先确认passcode是否正确，如果不正确则表示没有保存权限
            passcode=str(self.lineEdit_passcode.text())
            if passcode=="83830369":
### 以下开始连接数据库
                conn = sqlite3.connect('nextai.db')
                curs = conn.cursor()  #创建游标
                curs.execute("UPDATE shipment set shipDate=?, customer=?,sales=?,production=?,model=?,macID=?,unitPrice=?,number=?,paid=?,paidRecord=?,payRemind=?,shipTo=?,remark=? WHERE shipmentID=?;",content)
                curs.close()  #关闭游标
                conn.commit() #保存数据库
                conn.close() #关闭数据库连接
                self.close()
            else:
                QMessageBox.critical(self, "注意：不能保存", "您没有编辑保存的权限，或输入的功能码错误！")

### 以下分别处理5个【编辑】按钮的响应事件，这个方法太笨了，需要重新写

    def handle_click1(self,b1):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b1)
        self.show()
    def handle_click2(self,b2):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b2)
        self.show()
    def handle_click3(self,b3):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b3)
        self.show()
    def handle_click4(self,b4):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b4)
        self.show()
    def handle_click5(self,b5):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b5)
        self.show()
    def handle_click6(self,b6):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b6)
        self.show()
    def handle_click7(self,b7):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b7)
        self.show()
    def handle_click8(self,b8):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b8)
        self.show()
    def handle_click9(self,b9):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b9)
        self.show()
    def handle_click10(self,b10):#点击编辑1按钮，从数据库中查找并把cusotmerID=a1的条目显示出来
        self.lineDisplay(b10)
        self.show()


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
    app=QApplication(sys.argv) #格式
    e = MyForm()
    e.show()  #窗口显示



#    e.dateEdit_ship.setDate(QDate(2018,11,12))

#    e.dateEdit_ship.setDate(QDate(2018,11,15))


#    e.dateEdit_ship.setDate(QDate="2018-11-11")
#        self.dateEdit_ship.setDate(QtCore.QDate(2018,2,1))
#    e.pushButton_cancel.clicked.connect(b.reload)
#    e.pushButton_cancel.clicked.connect(b.showBrowser)
#    e.pushButton_cancel.clicked.connect(e.close)
#    e.pushButton_cancel.clicked.connect(NextOffice.shipment.shipment_browser.reload)
#    NextOffice.shipment.shipment_browser.reload()
    app.exec_() #格式