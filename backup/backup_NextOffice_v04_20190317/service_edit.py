import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.resize(687, 624)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(460, 290, 59, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(460, 140, 59, 31))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 560, 221, 51))
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
        self.label_8.setGeometry(QtCore.QRect(38, 340, 71, 61))
        self.label_8.setObjectName("label_8")
        self.comboBox_method = QtWidgets.QComboBox(Form)
        self.comboBox_method.setGeometry(QtCore.QRect(460, 100, 151, 22))
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 61, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 90, 321, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(11, 120, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(460, 80, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_staff = QtWidgets.QLineEdit(Form)
        self.lineEdit_staff.setGeometry(QtCore.QRect(530, 140, 81, 31))
        self.lineEdit_staff.setText("")
        self.lineEdit_staff.setObjectName("lineEdit_staff")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(460, 190, 59, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox_classify = QtWidgets.QComboBox(Form)
        self.comboBox_classify.setGeometry(QtCore.QRect(460, 250, 151, 21))
        self.comboBox_classify.setObjectName("comboBox_classify")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.comboBox_classify.addItem("")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(460, 220, 61, 31))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(430, 90, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit_problem = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_problem.setGeometry(QtCore.QRect(110, 130, 321, 141))
        self.plainTextEdit_problem.setObjectName("plainTextEdit_problem")
        self.plainTextEdit_solution = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_solution.setGeometry(QtCore.QRect(110, 320, 321, 221))
        self.plainTextEdit_solution.setObjectName("plainTextEdit_solution")
        self.plainTextEdit_remark = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_remark.setGeometry(QtCore.QRect(460, 320, 211, 221))
        self.plainTextEdit_remark.setObjectName("plainTextEdit_remark")
        self.label_classify = QtWidgets.QLabel(Form)
        self.label_classify.setGeometry(QtCore.QRect(530, 220, 141, 31))
        self.label_classify.setObjectName("label_classify")
        self.label_method = QtWidgets.QLabel(Form)
        self.label_method.setGeometry(QtCore.QRect(530, 80, 131, 21))
        self.label_method.setObjectName("label_method")
        self.lineEdit_charge = QtWidgets.QLineEdit(Form)
        self.lineEdit_charge.setGeometry(QtCore.QRect(530, 190, 81, 31))
        self.lineEdit_charge.setObjectName("lineEdit_charge")
        self.dateEdit_handle = QtWidgets.QDateEdit(Form)
        self.dateEdit_handle.setGeometry(QtCore.QRect(110, 280, 110, 31))
        self.dateEdit_handle.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_handle.setCalendarPopup(True)
        self.dateEdit_handle.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit_handle.setObjectName("dateEdit_handle")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(570, 590, 51, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_passcode = QtWidgets.QLineEdit(Form)
        self.lineEdit_passcode.setGeometry(QtCore.QRect(620, 590, 51, 21))
        self.lineEdit_passcode.setText("")
        self.lineEdit_passcode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passcode.setObjectName("lineEdit_passcode")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(270, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setGeometry(QtCore.QRect(110, 50, 51, 31))
        self.label_id.setObjectName("label_id")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">备注</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">处理人员</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">解决方法</span></p></body></html>"))
        self.comboBox_method.setItemText(0, _translate("Form", "（未选择）"))
        self.comboBox_method.setItemText(1, _translate("Form", "远程处理"))
        self.comboBox_method.setItemText(2, _translate("Form", "上门服务"))
        self.label.setText(_translate("Form", "<html><head/><body><p>PrimaryKey</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">客户名称</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">客户反馈问题</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">处理方式</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">处理时间</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">收费金额</span></p></body></html>"))
        self.comboBox_classify.setItemText(0, _translate("Form", "（未选择）"))
        self.comboBox_classify.setItemText(1, _translate("Form", "装配问题"))
        self.comboBox_classify.setItemText(2, _translate("Form", "零件质量问题"))
        self.comboBox_classify.setItemText(3, _translate("Form", "产品设计问题"))
        self.comboBox_classify.setItemText(4, _translate("Form", "使用不当"))
        self.comboBox_classify.setItemText(5, _translate("Form", "其他类型"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">问题归类</span></p></body></html>"))
        self.label_classify.setText(_translate("Form", "（未选择）"))
        self.label_method.setText(_translate("Form", "（未选择）"))
        self.lineEdit_charge.setText(_translate("Form", "0"))
        self.dateEdit_handle.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p>功能码</p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0f3978;\">详细信息&amp;编辑</span></p></body></html>"))
        self.label_id.setText(_translate("Form", "0000"))

### 以上是QtDesiger工具生成的代码
### 以下是自己编写的程序
    def database(self,b): #获得customer数据库中的所有数据，并赋值给data[]
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
        print("starting select")
        curs.execute("SELECT * from service WHERE serviceID=?;",(b,)) #b必须加括号，并且要加一个逗号，以表示同一个数字，
        print("finish select")
        data= curs.fetchone()
        print(data)
        curs.close()  #关闭游标
        conn.close() #关闭数据库连接
        return data

    def lineDisplay(self,b): #在edit中显示browser 1-5行的内容
        data=self.database(b)

        self.label_id.setText(str(data[0])) #数据库是从0开始的，所以减1
        self.lineEdit_name.setText(str(data[1]))
        self.plainTextEdit_problem.setPlainText(str(data[2]))
        self.label_method.setText(str(data[3]))
###handlingTime-下面是从数据库中读取日期（字符串），然后分割字符串，再转成可以setData的格式
        handle=data[4]
        sdate=handle.split("-")
        sdate1=int(sdate[0])
        sdate2=int(sdate[1])
        sdate3=int(sdate[2])
        self.dateEdit_handle.setDate(QDate(sdate1,sdate2,sdate3))
#            self.lineEdit_handlingTime.setText(str(data[p-1][4]))
        self.plainTextEdit_solution.setPlainText(str(data[5]))
        self.lineEdit_staff.setText(str(data[6]))
        self.lineEdit_charge.setText(str(data[7]))
        self.label_classify.setText(str(data[8]))
        self.plainTextEdit_remark.setPlainText(str(data[9]))

    def saveToSqlite(self):
        id=int(self.label_id.text())
        customer=str(self.lineEdit_name.text())
        problem=str(self.plainTextEdit_problem.toPlainText())
        method=str(self.label_method.text())
        handlingTime=str(self.dateEdit_handle.text())
        staff=str(self.lineEdit_staff.text())
        solution=str(self.plainTextEdit_solution.toPlainText())
        charge=str(self.lineEdit_charge.text())
        classify=str(self.label_classify.text())
        remark=str(self.plainTextEdit_remark.toPlainText())
        content=[customer,problem,method,handlingTime,staff,solution,charge,classify,remark,id]

# 保存之前，先确认passcode是否正确，如果不正确则表示没有保存权限
        passcode=str(self.lineEdit_passcode.text())
        if passcode=="83830369":
### 以下开始连接数据库
            conn = sqlite3.connect('nextai.db')
            curs = conn.cursor()  #创建游标
            curs.execute("UPDATE service set customer=?, problem=?,method=?,handlingTime=?,staff=?,solution=?,charge=?,classify=?,remark=? WHERE serviceID=?;",content)
            curs.close()  #关闭游标
            conn.commit() #保存数据库
            conn.close() #关闭数据库连接
            print ("保存数据库成功")
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
        self.comboBox_method.activated[str].connect(self.label_method.setText)
        self.comboBox_classify.activated[str].connect(self.label_classify.setText)
        self.pushButton_save.clicked.connect(self.saveToSqlite)
        self.pushButton_cancel.clicked.connect(self.close)


if __name__=='__main__':
    app=QApplication(sys.argv)
    w = MyForm()
    w.show()
    app.exec_()