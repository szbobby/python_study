import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
import NextOffice.shipment.shipment_browser
import NextOffice.shipment.shipment_main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate,   QDateTime , QTime
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.resize(903, 489)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(370, 20, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(610, 210, 59, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(700, 50, 59, 61))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 420, 221, 51))
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
        self.label.setGeometry(QtCore.QRect(40, 70, 51, 31))
        self.label.setObjectName("label")
        self.lineEdit_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_id.setGeometry(QtCore.QRect(100, 70, 81, 31))
        self.lineEdit_id.setReadOnly(False)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 70, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_customer = QtWidgets.QLineEdit(Form)
        self.lineEdit_customer.setGeometry(QtCore.QRect(490, 70, 181, 31))
        self.lineEdit_customer.setObjectName("lineEdit_customer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_sales = QtWidgets.QLineEdit(Form)
        self.lineEdit_sales.setGeometry(QtCore.QRect(760, 70, 81, 31))
        self.lineEdit_sales.setText("")
        self.lineEdit_sales.setObjectName("lineEdit_sales")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 230, 51, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox_production = QtWidgets.QComboBox(Form)
        self.comboBox_production.setGeometry(QtCore.QRect(100, 150, 91, 22))
        self.comboBox_production.setObjectName("comboBox_production")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.comboBox_production.addItem("")
        self.plainTextEdit_payRecord = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_payRecord.setGeometry(QtCore.QRect(670, 210, 171, 61))
        self.plainTextEdit_payRecord.setObjectName("plainTextEdit_payRecord")
        self.lineEdit_number = QtWidgets.QLineEdit(Form)
        self.lineEdit_number.setGeometry(QtCore.QRect(100, 230, 81, 31))
        self.lineEdit_number.setText("")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(230, 70, 61, 31))
        self.label_11.setObjectName("label_11")
        self.comboBox_model = QtWidgets.QComboBox(Form)
        self.comboBox_model.setGeometry(QtCore.QRect(290, 150, 91, 21))
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
        self.label_12.setGeometry(QtCore.QRect(230, 140, 51, 31))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(440, 140, 41, 31))
        self.label_14.setObjectName("label_14")
        self.lineEdit_macID = QtWidgets.QLineEdit(Form)
        self.lineEdit_macID.setGeometry(QtCore.QRect(490, 140, 81, 31))
        self.lineEdit_macID.setText("")
        self.lineEdit_macID.setObjectName("lineEdit_macID")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 180, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(230, 230, 41, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_unitPrice = QtWidgets.QLineEdit(Form)
        self.lineEdit_unitPrice.setGeometry(QtCore.QRect(270, 230, 81, 31))
        self.lineEdit_unitPrice.setText("")
        self.lineEdit_unitPrice.setObjectName("lineEdit_unitPrice")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(440, 210, 41, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_paid = QtWidgets.QLineEdit(Form)
        self.lineEdit_paid.setGeometry(QtCore.QRect(490, 210, 81, 31))
        self.lineEdit_paid.setText("")
        self.lineEdit_paid.setObjectName("lineEdit_paid")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 59, 61))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_shipto = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_shipto.setGeometry(QtCore.QRect(100, 320, 271, 61))
        self.plainTextEdit_shipto.setObjectName("plainTextEdit_shipto")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(450, 320, 31, 61))
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_remark = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_remark.setGeometry(QtCore.QRect(490, 320, 351, 61))
        self.plainTextEdit_remark.setObjectName("plainTextEdit_remark")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(40, 290, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(30, 390, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(400, 250, 81, 31))
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(40, 50, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_production = QtWidgets.QLabel(Form)
        self.label_production.setGeometry(QtCore.QRect(100, 120, 91, 21))
        self.label_production.setObjectName("label_production")
        self.label_model = QtWidgets.QLabel(Form)
        self.label_model.setGeometry(QtCore.QRect(300, 120, 81, 21))
        self.label_model.setObjectName("label_model")
        self.dateEdit_ship = QtWidgets.QDateEdit(Form)
        self.dateEdit_ship.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit_ship.setGeometry(QtCore.QRect(280, 70, 110, 31))
        self.dateEdit_ship.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_ship.setCalendarPopup(True)
        self.dateEdit_ship.setDate(QtCore.QDate(2018, 1, 1))
#        self.dateEdit_ship.setDate(QtCore.QDate(2018,2,1))

        self.dateEdit_ship.setObjectName("dateEdit_ship")
        self.dateEdit_pay = QtWidgets.QDateEdit(Form)
        self.dateEdit_pay.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit_pay.setGeometry(QtCore.QRect(490, 250, 101, 31))
        self.dateEdit_pay.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_pay.setCalendarPopup(True)
        self.dateEdit_pay.setObjectName("dateEdit_pay")

        self.retranslateUi(Form)
        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_cancel.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">产品出货--编辑</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "付款记录"))
        self.label_6.setText(_translate("Form", "业务负责"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "出货单号"))
        self.lineEdit_id.setText(_translate("Form", "20180001"))
        self.label_2.setText(_translate("Form", "客户名称"))
        self.label_3.setText(_translate("Form", "出货产品"))
        self.label_9.setText(_translate("Form", "出货数量"))
        self.comboBox_production.setItemText(0, _translate("Form", "分选机"))
        self.comboBox_production.setItemText(1, _translate("Form", "点焊机"))
        self.comboBox_production.setItemText(2, _translate("Form", "面垫机"))
        self.comboBox_production.setItemText(3, _translate("Form", "PACK自动产线"))
        self.comboBox_production.setItemText(4, _translate("Form", "其他"))
        self.label_11.setText(_translate("Form", "出货日期"))
        self.comboBox_model.setItemText(0, _translate("Form", "无"))
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
        self.label_12.setText(_translate("Form", "规格型号"))
        self.label_14.setText(_translate("Form", "设备号"))
        self.label_16.setText(_translate("Form", "单价"))
        self.label_17.setText(_translate("Form", "已付款"))
        self.label_8.setText(_translate("Form", "出货地址\n"
"与联系人"))
        self.label_10.setText(_translate("Form", "备注"))
        self.label_18.setText(_translate("Form", "下次付款时间"))
        self.label_production.setText(_translate("Form", "产品名称"))
        self.label_model.setText(_translate("Form", "规格型号"))


### 以上是QtDesiger工具生成的代码
### 以下是自己编写的程序
    def database(self): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("pageData()打开数据库成功")
        curs.execute("SELECT * from shipment")
        data= curs.fetchall()
        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return data
    def lineDisplay(self,l): #在edit中显示browser 1-5行的内容
        p=NextOffice.shipment.shipment_main.g*5-4 #获得当前页面的第1行的序号
        data=self.database()
        print("shipment_edit:lineDisplay start")
        if l==1:
            self.lineEdit_id.setText(str(data[p-1][0])) #数据库是从0开始的，所以减1
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            shipdate=data[p-1][1]
            sdate=shipdate.split("-")
            sdate1=int(sdate[0])
            sdate2=int(sdate[1])
            sdate3=int(sdate[2])
            self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#            self.dateEdit_ship.setDate(data[p-1][1])
            self.lineEdit_customer.setText(str(data[p-1][2]))
            self.lineEdit_sales.setText(str(data[p-1][3]))
            self.label_production.setText(str(data[p-1][4]))
            self.label_model.setText(str(data[p-1][5]))
            self.lineEdit_macID.setText(str(data[p-1][6]))
            self.lineEdit_unitPrice.setText(str(data[p-1][7]))
            self.lineEdit_number.setText(str(data[p-1][8]))
            self.lineEdit_paid.setText(str(data[p-1][9]))
            self.plainTextEdit_payRecord.setPlainText(str(data[p-1][10]))
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            paydate=data[p-1][11]
            pdate=paydate.split("-")
            pdate1=int(pdate[0])
            pdate2=int(pdate[1])
            pdate3=int(pdate[2])
            self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#            self.dateEdit_pay.setDate(str(data[p-1][11]))
            self.plainTextEdit_shipto.setPlainText(str(data[p-1][12]))
            self.plainTextEdit_remark.setPlainText(str(data[p-1][13]))

        elif l==2:
            self.lineEdit_id.setText(str(data[p][0])) #数据库是从0开始的，所以减1

###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            shipdate=data[p][1]
            sdate=shipdate.split("-")
            sdate1=int(sdate[0])
            sdate2=int(sdate[1])
            sdate3=int(sdate[2])
            self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#            self.dateEdit_ship.setDate(str(data[p][1]))
            self.lineEdit_customer.setText(str(data[p][2]))
            self.lineEdit_sales.setText(str(data[p][3]))
            self.label_production.setText(str(data[p][4]))
            self.label_model.setText(str(data[p][5]))
            self.lineEdit_macID.setText(str(data[p][6]))
            self.lineEdit_unitPrice.setText(str(data[p][7]))
            self.lineEdit_number.setText(str(data[p][8]))
            self.lineEdit_paid.setText(str(data[p][9]))
            self.plainTextEdit_payRecord.setPlainText(str(data[p][10]))
 ###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            paydate=data[p][11]
            pdate=paydate.split("-")
            pdate1=int(pdate[0])
            pdate2=int(pdate[1])
            pdate3=int(pdate[2])
            self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#            self.dateEdit_pay.setDate(str(data[p-1][11]))
            self.plainTextEdit_shipto.setPlainText(str(data[p][12]))
            self.plainTextEdit_remark.setPlainText(str(data[p][13]))

        elif l==3:
            self.lineEdit_id.setText(str(data[p+1][0])) #数据库是从0开始的，所以减1
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            shipdate=data[p+1][1]
            sdate=shipdate.split("-")
            sdate1=int(sdate[0])
            sdate2=int(sdate[1])
            sdate3=int(sdate[2])
            self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#            self.dateEdit_ship.setDate(str(data[p][1]))
            self.lineEdit_customer.setText(str(data[p+1][2]))
            self.lineEdit_sales.setText(str(data[p+1][3]))
            self.label_production.setText(str(data[p+1][4]))
            self.label_model.setText(str(data[p+1][5]))
            self.lineEdit_macID.setText(str(data[p+1][6]))
            self.lineEdit_unitPrice.setText(str(data[p+1][7]))
            self.lineEdit_number.setText(str(data[p+1][8]))
            self.lineEdit_paid.setText(str(data[p+1][9]))
            self.plainTextEdit_payRecord.setPlainText(str(data[p+1][10]))
 ###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            paydate=data[p+1][11]
            pdate=paydate.split("-")
            pdate1=int(pdate[0])
            pdate2=int(pdate[1])
            pdate3=int(pdate[2])
            self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#            self.dateEdit_pay.setDate(str(data[p-1][11]))
            self.plainTextEdit_shipto.setPlainText(str(data[p+1][12]))
            self.plainTextEdit_remark.setPlainText(str(data[p+1][13]))

        elif l==4:
            self.lineEdit_id.setText(str(data[p+2][0])) #数据库是从0开始的，所以减1
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            shipdate=data[p+2][1]
            sdate=shipdate.split("-")
            sdate1=int(sdate[0])
            sdate2=int(sdate[1])
            sdate3=int(sdate[2])
            self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#            self.dateEdit_ship.setDate(str(data[p][1]))
            self.lineEdit_customer.setText(str(data[p+2][2]))
            self.lineEdit_sales.setText(str(data[p+2][3]))
            self.label_production.setText(str(data[p+2][4]))
            self.label_model.setText(str(data[p+2][5]))
            self.lineEdit_macID.setText(str(data[p+2][6]))
            self.lineEdit_unitPrice.setText(str(data[p+2][7]))
            self.lineEdit_number.setText(str(data[p+2][8]))
            self.lineEdit_paid.setText(str(data[p+2][9]))
            self.plainTextEdit_payRecord.setPlainText(str(data[p+2][10]))
 ###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            paydate=data[p+2][11]
            pdate=paydate.split("-")
            pdate1=int(pdate[0])
            pdate2=int(pdate[1])
            pdate3=int(pdate[2])
            self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#            self.dateEdit_pay.setDate(str(data[p-1][11]))
            self.plainTextEdit_shipto.setPlainText(str(data[p+2][12]))
            self.plainTextEdit_remark.setPlainText(str(data[p+2][13]))

        elif l==5:
            self.lineEdit_id.setText(str(data[p+3][0])) #数据库是从0开始的，所以减1
###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            shipdate=data[p+3][1]
            sdate=shipdate.split("-")
            sdate1=int(sdate[0])
            sdate2=int(sdate[1])
            sdate3=int(sdate[2])
            self.dateEdit_ship.setDate(QDate(sdate1,sdate2,sdate3))
#            self.dateEdit_ship.setDate(str(data[p][1]))
            self.lineEdit_customer.setText(str(data[p+3][2]))
            self.lineEdit_sales.setText(str(data[p+3][3]))
            self.label_production.setText(str(data[p+3][4]))
            self.label_model.setText(str(data[p+3][5]))
            self.lineEdit_macID.setText(str(data[p+3][6]))
            self.lineEdit_unitPrice.setText(str(data[p+3][7]))
            self.lineEdit_number.setText(str(data[p+3][8]))
            self.lineEdit_paid.setText(str(data[p+3][9]))
            self.plainTextEdit_payRecord.setPlainText(str(data[p+3][10]))
 ###下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
            paydate=data[p+3][11]
            pdate=paydate.split("-")
            pdate1=int(pdate[0])
            pdate2=int(pdate[1])
            pdate3=int(pdate[2])
            self.dateEdit_pay.setDate(QDate(pdate1,pdate2,pdate3))
#            self.dateEdit_pay.setDate(str(data[p-1][11]))
            self.plainTextEdit_shipto.setPlainText(str(data[p+3][12]))
            self.plainTextEdit_remark.setPlainText(str(data[p+3][13]))
        else:
            print("customer_edit的lineDisplay")

    def saveToSqlite(self):
        id=int(self.lineEdit_id.text())
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
### 以下开始连接数据库
            conn = sqlite3.connect('nextai.db')
            curs = conn.cursor()  #创建游标
            curs.execute("UPDATE shipment set shipDate=?, customer=?,sales=?,production=?,model=?,macID=?,unitPrice=?,number=?,paid=?,paidRecord=?,payRemind=?,shipTo=?,remark=? WHERE shipmentID=?;",content)
            curs.close()  #关闭游标
            conn.commit() #保存数据库
            conn.close() #关闭数据库连接
            self.close()

### 以下分别处理5个【编辑】按钮的响应事件，这个方法太笨了，需要重新写
    def handle_click1(self):
        self.lineDisplay(1)
        self.show()
    def handle_click2(self):
        self.lineDisplay(2)
        self.show()
    def handle_click3(self):
        self.lineDisplay(3)
        self.show()
    def handle_click4(self):
        self.lineDisplay(4)
        self.show()
    def handle_click5(self):
        self.lineDisplay(5)
        self.show()

class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_production.activated[str].connect(self.label_production.setText)
        self.comboBox_model.activated[str].connect(self.label_model.setText)

        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_save.clicked.connect(self.close)
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
