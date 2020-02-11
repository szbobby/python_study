import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
#import NextOffice.service.service_main
import NextOffice.service.service_edit
import NextOffice.service.service_add

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1365, 641)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(520, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_id1 = QtWidgets.QLabel(Form)
        self.label_id1.setGeometry(QtCore.QRect(70, 160, 51, 21))
        self.label_id1.setObjectName("label_id1")
        self.lineEdit_search = QtWidgets.QLineEdit(Form)
        self.lineEdit_search.setGeometry(QtCore.QRect(50, 40, 113, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.label_name1 = QtWidgets.QLabel(Form)
        self.label_name1.setGeometry(QtCore.QRect(120, 160, 141, 21))
        self.label_name1.setObjectName("label_name1")
        self.textBrowser_problem1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_problem1.setGeometry(QtCore.QRect(280, 130, 161, 71))
        self.textBrowser_problem1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_problem1.setLineWidth(0)
        self.textBrowser_problem1.setObjectName("textBrowser_problem1")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(20, 70, 1211, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(20, 560, 1271, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_SwitchCustomer = QtWidgets.QPushButton(Form)
        self.pushButton_SwitchCustomer.setGeometry(QtCore.QRect(1070, 40, 111, 23))
        self.pushButton_SwitchCustomer.setObjectName("pushButton_SwitchCustomer")
        self.pushButton_edit1 = QtWidgets.QPushButton(Form)
        self.pushButton_edit1.setGeometry(QtCore.QRect(1270, 150, 75, 23))
        self.pushButton_edit1.setObjectName("pushButton_edit1")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(670, 80, 71, 39))
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 200, 1291, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 80, 61, 39))
        self.label_4.setObjectName("label_4")
        self.label_staff1 = QtWidgets.QLabel(Form)
        self.label_staff1.setGeometry(QtCore.QRect(670, 140, 41, 31))
        self.label_staff1.setObjectName("label_staff1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 110, 1291, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_SwitchShipment = QtWidgets.QPushButton(Form)
        self.pushButton_SwitchShipment.setGeometry(QtCore.QRect(950, 40, 111, 23))
        self.pushButton_SwitchShipment.setObjectName("pushButton_SwitchShipment")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 42, 31, 20))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(580, 80, 61, 39))
        self.label_5.setObjectName("label_5")
        self.textBrowser_solution1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_solution1.setGeometry(QtCore.QRect(720, 130, 171, 71))
        self.textBrowser_solution1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_solution1.setLineWidth(0)
        self.textBrowser_solution1.setObjectName("textBrowser_solution1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 121, 39))
        self.label_2.setObjectName("label_2")
        self.toolButton_connect = QtWidgets.QToolButton(Form)
        self.toolButton_connect.setGeometry(QtCore.QRect(1190, 40, 41, 31))
        self.toolButton_connect.setObjectName("toolButton_connect")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(750, 80, 51, 39))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 101, 39))
        self.label_3.setObjectName("label_3")
        self.toolButton_search = QtWidgets.QToolButton(Form)
        self.toolButton_search.setGeometry(QtCore.QRect(170, 30, 41, 31))
        self.toolButton_search.setObjectName("toolButton_search")
        self.pushButton_previous = QtWidgets.QPushButton(Form)
        self.pushButton_previous.setGeometry(QtCore.QRect(110, 590, 75, 23))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 61, 39))
        self.label.setObjectName("label")
        self.pushButton_next = QtWidgets.QPushButton(Form)
        self.pushButton_next.setGeometry(QtCore.QRect(220, 590, 75, 23))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_new = QtWidgets.QPushButton(Form)
        self.pushButton_new.setGeometry(QtCore.QRect(560, 590, 91, 23))
        self.pushButton_new.setObjectName("pushButton_new")
        self.lineEdit_search2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_search2.setGeometry(QtCore.QRect(390, 590, 31, 20))
        self.lineEdit_search2.setObjectName("lineEdit_search2")
        self.toolButton_search2 = QtWidgets.QToolButton(Form)
        self.toolButton_search2.setGeometry(QtCore.QRect(460, 580, 41, 31))
        self.toolButton_search2.setObjectName("toolButton_search2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(350, 580, 91, 39))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(920, 80, 51, 39))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(990, 80, 51, 39))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(1130, 80, 51, 39))
        self.label_12.setObjectName("label_12")
        self.textBrowser_remark1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark1.setGeometry(QtCore.QRect(1070, 130, 141, 71))
        self.textBrowser_remark1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark1.setLineWidth(0)
        self.textBrowser_remark1.setObjectName("textBrowser_remark1")
        self.label_order1 = QtWidgets.QLabel(Form)
        self.label_order1.setGeometry(QtCore.QRect(20, 160, 36, 21))
        self.label_order1.setObjectName("label_order1")
        self.label_order2 = QtWidgets.QLabel(Form)
        self.label_order2.setGeometry(QtCore.QRect(20, 250, 36, 21))
        self.label_order2.setObjectName("label_order2")
        self.label_order3 = QtWidgets.QLabel(Form)
        self.label_order3.setGeometry(QtCore.QRect(20, 330, 36, 31))
        self.label_order3.setObjectName("label_order3")
        self.label_order4 = QtWidgets.QLabel(Form)
        self.label_order4.setGeometry(QtCore.QRect(20, 420, 36, 41))
        self.label_order4.setObjectName("label_order4")
        self.label_order5 = QtWidgets.QLabel(Form)
        self.label_order5.setGeometry(QtCore.QRect(20, 510, 36, 31))
        self.label_order5.setObjectName("label_order5")
        self.textBrowser_problem2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_problem2.setGeometry(QtCore.QRect(280, 220, 161, 71))
        self.textBrowser_problem2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_problem2.setLineWidth(0)
        self.textBrowser_problem2.setObjectName("textBrowser_problem2")
        self.label_name2 = QtWidgets.QLabel(Form)
        self.label_name2.setGeometry(QtCore.QRect(120, 250, 141, 21))
        self.label_name2.setObjectName("label_name2")
        self.textBrowser_remark2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark2.setGeometry(QtCore.QRect(1070, 220, 141, 71))
        self.textBrowser_remark2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark2.setLineWidth(0)
        self.textBrowser_remark2.setObjectName("textBrowser_remark2")
        self.textBrowser_solution2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_solution2.setGeometry(QtCore.QRect(720, 220, 171, 71))
        self.textBrowser_solution2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_solution2.setLineWidth(0)
        self.textBrowser_solution2.setObjectName("textBrowser_solution2")
        self.label_staff2 = QtWidgets.QLabel(Form)
        self.label_staff2.setGeometry(QtCore.QRect(670, 230, 41, 31))
        self.label_staff2.setObjectName("label_staff2")
        self.label_id2 = QtWidgets.QLabel(Form)
        self.label_id2.setGeometry(QtCore.QRect(70, 250, 51, 21))
        self.label_id2.setObjectName("label_id2")
        self.pushButton_edit2 = QtWidgets.QPushButton(Form)
        self.pushButton_edit2.setGeometry(QtCore.QRect(1270, 240, 75, 23))
        self.pushButton_edit2.setObjectName("pushButton_edit2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 290, 1281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_name3 = QtWidgets.QLabel(Form)
        self.label_name3.setGeometry(QtCore.QRect(120, 340, 141, 21))
        self.label_name3.setObjectName("label_name3")
        self.label_id3 = QtWidgets.QLabel(Form)
        self.label_id3.setGeometry(QtCore.QRect(70, 340, 51, 21))
        self.label_id3.setObjectName("label_id3")
        self.pushButton_edit3 = QtWidgets.QPushButton(Form)
        self.pushButton_edit3.setGeometry(QtCore.QRect(1270, 330, 75, 23))
        self.pushButton_edit3.setObjectName("pushButton_edit3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(20, 380, 1281, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.textBrowser_problem3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_problem3.setGeometry(QtCore.QRect(280, 310, 161, 71))
        self.textBrowser_problem3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_problem3.setLineWidth(0)
        self.textBrowser_problem3.setObjectName("textBrowser_problem3")
        self.textBrowser_remark3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark3.setGeometry(QtCore.QRect(1070, 310, 141, 71))
        self.textBrowser_remark3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark3.setLineWidth(0)
        self.textBrowser_remark3.setObjectName("textBrowser_remark3")
        self.textBrowser_solution3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_solution3.setGeometry(QtCore.QRect(720, 310, 171, 71))
        self.textBrowser_solution3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_solution3.setLineWidth(0)
        self.textBrowser_solution3.setObjectName("textBrowser_solution3")
        self.label_staff3 = QtWidgets.QLabel(Form)
        self.label_staff3.setGeometry(QtCore.QRect(670, 320, 41, 31))
        self.label_staff3.setObjectName("label_staff3")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 470, 1271, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_name4 = QtWidgets.QLabel(Form)
        self.label_name4.setGeometry(QtCore.QRect(120, 430, 141, 21))
        self.label_name4.setObjectName("label_name4")
        self.label_id4 = QtWidgets.QLabel(Form)
        self.label_id4.setGeometry(QtCore.QRect(70, 430, 51, 21))
        self.label_id4.setObjectName("label_id4")
        self.textBrowser_problem4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_problem4.setGeometry(QtCore.QRect(280, 400, 161, 71))
        self.textBrowser_problem4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_problem4.setLineWidth(0)
        self.textBrowser_problem4.setObjectName("textBrowser_problem4")
        self.textBrowser_remark4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark4.setGeometry(QtCore.QRect(1070, 400, 141, 71))
        self.textBrowser_remark4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark4.setLineWidth(0)
        self.textBrowser_remark4.setObjectName("textBrowser_remark4")
        self.textBrowser_solution4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_solution4.setGeometry(QtCore.QRect(720, 400, 171, 71))
        self.textBrowser_solution4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_solution4.setLineWidth(0)
        self.textBrowser_solution4.setObjectName("textBrowser_solution4")
        self.pushButton_edit4 = QtWidgets.QPushButton(Form)
        self.pushButton_edit4.setGeometry(QtCore.QRect(1270, 420, 75, 23))
        self.pushButton_edit4.setObjectName("pushButton_edit4")
        self.label_staff4 = QtWidgets.QLabel(Form)
        self.label_staff4.setGeometry(QtCore.QRect(670, 410, 41, 31))
        self.label_staff4.setObjectName("label_staff4")
        self.label_id5 = QtWidgets.QLabel(Form)
        self.label_id5.setGeometry(QtCore.QRect(70, 520, 51, 21))
        self.label_id5.setObjectName("label_id5")
        self.textBrowser_problem5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_problem5.setGeometry(QtCore.QRect(280, 490, 161, 71))
        self.textBrowser_problem5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_problem5.setLineWidth(0)
        self.textBrowser_problem5.setObjectName("textBrowser_problem5")
        self.textBrowser_remark5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark5.setGeometry(QtCore.QRect(1070, 490, 141, 71))
        self.textBrowser_remark5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark5.setLineWidth(0)
        self.textBrowser_remark5.setObjectName("textBrowser_remark5")
        self.label_name5 = QtWidgets.QLabel(Form)
        self.label_name5.setGeometry(QtCore.QRect(120, 520, 141, 21))
        self.label_name5.setObjectName("label_name5")
        self.textBrowser_solution5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_solution5.setGeometry(QtCore.QRect(720, 490, 171, 71))
        self.textBrowser_solution5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_solution5.setLineWidth(0)
        self.textBrowser_solution5.setObjectName("textBrowser_solution5")
        self.label_staff5 = QtWidgets.QLabel(Form)
        self.label_staff5.setGeometry(QtCore.QRect(670, 510, 41, 31))
        self.label_staff5.setObjectName("label_staff5")
        self.pushButton_edit5 = QtWidgets.QPushButton(Form)
        self.pushButton_edit5.setGeometry(QtCore.QRect(1270, 510, 75, 23))
        self.pushButton_edit5.setObjectName("pushButton_edit5")
        self.label_handlingTime1 = QtWidgets.QLabel(Form)
        self.label_handlingTime1.setGeometry(QtCore.QRect(560, 140, 101, 31))
        self.label_handlingTime1.setObjectName("label_handlingTime1")
        self.label_handlingTime2 = QtWidgets.QLabel(Form)
        self.label_handlingTime2.setGeometry(QtCore.QRect(560, 230, 101, 31))
        self.label_handlingTime2.setObjectName("label_handlingTime2")
        self.label_handlingTime3 = QtWidgets.QLabel(Form)
        self.label_handlingTime3.setGeometry(QtCore.QRect(560, 320, 101, 31))
        self.label_handlingTime3.setObjectName("label_handlingTime3")
        self.label_handlingTime4 = QtWidgets.QLabel(Form)
        self.label_handlingTime4.setGeometry(QtCore.QRect(560, 410, 101, 31))
        self.label_handlingTime4.setObjectName("label_handlingTime4")
        self.label_handlingTime5 = QtWidgets.QLabel(Form)
        self.label_handlingTime5.setGeometry(QtCore.QRect(560, 510, 101, 31))
        self.label_handlingTime5.setObjectName("label_handlingTime5")
        self.label_method1 = QtWidgets.QLabel(Form)
        self.label_method1.setGeometry(QtCore.QRect(460, 140, 81, 31))
        self.label_method1.setObjectName("label_method1")
        self.label_method2 = QtWidgets.QLabel(Form)
        self.label_method2.setGeometry(QtCore.QRect(460, 240, 81, 31))
        self.label_method2.setObjectName("label_method2")
        self.label_method3 = QtWidgets.QLabel(Form)
        self.label_method3.setGeometry(QtCore.QRect(460, 320, 81, 31))
        self.label_method3.setObjectName("label_method3")
        self.label_method4 = QtWidgets.QLabel(Form)
        self.label_method4.setGeometry(QtCore.QRect(460, 410, 81, 31))
        self.label_method4.setObjectName("label_method4")
        self.label_method5 = QtWidgets.QLabel(Form)
        self.label_method5.setGeometry(QtCore.QRect(470, 510, 81, 31))
        self.label_method5.setObjectName("label_method5")
        self.label_classify1 = QtWidgets.QLabel(Form)
        self.label_classify1.setGeometry(QtCore.QRect(980, 140, 81, 31))
        self.label_classify1.setObjectName("label_classify1")
        self.label_classify2 = QtWidgets.QLabel(Form)
        self.label_classify2.setGeometry(QtCore.QRect(980, 230, 81, 31))
        self.label_classify2.setObjectName("label_classify2")
        self.label_classify3 = QtWidgets.QLabel(Form)
        self.label_classify3.setGeometry(QtCore.QRect(980, 320, 81, 31))
        self.label_classify3.setObjectName("label_classify3")
        self.label_classify4 = QtWidgets.QLabel(Form)
        self.label_classify4.setGeometry(QtCore.QRect(980, 410, 81, 31))
        self.label_classify4.setObjectName("label_classify4")
        self.label_classify5 = QtWidgets.QLabel(Form)
        self.label_classify5.setGeometry(QtCore.QRect(980, 500, 81, 31))
        self.label_classify5.setObjectName("label_classify5")
        self.label_charge1 = QtWidgets.QLabel(Form)
        self.label_charge1.setGeometry(QtCore.QRect(920, 140, 51, 31))
        self.label_charge1.setObjectName("label_charge1")
        self.label_charge2 = QtWidgets.QLabel(Form)
        self.label_charge2.setGeometry(QtCore.QRect(920, 230, 51, 31))
        self.label_charge2.setObjectName("label_charge2")
        self.label_charge3 = QtWidgets.QLabel(Form)
        self.label_charge3.setGeometry(QtCore.QRect(920, 320, 51, 31))
        self.label_charge3.setObjectName("label_charge3")
        self.label_charge4 = QtWidgets.QLabel(Form)
        self.label_charge4.setGeometry(QtCore.QRect(920, 410, 51, 31))
        self.label_charge4.setObjectName("label_charge4")
        self.label_charge5 = QtWidgets.QLabel(Form)
        self.label_charge5.setGeometry(QtCore.QRect(920, 500, 51, 31))
        self.label_charge5.setObjectName("label_charge5")
        self.label_13.raise_()
        self.label_id1.raise_()
        self.lineEdit_search.raise_()
        self.label_name1.raise_()
        self.textBrowser_problem1.raise_()
        self.line_7.raise_()
        self.line_6.raise_()
        self.pushButton_SwitchCustomer.raise_()
        self.pushButton_edit1.raise_()
        self.label_6.raise_()
        self.line_2.raise_()
        self.label_4.raise_()
        self.label_staff1.raise_()
        self.line.raise_()
        self.pushButton_SwitchShipment.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.textBrowser_solution1.raise_()
        self.label_2.raise_()
        self.toolButton_connect.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.toolButton_search.raise_()
        self.pushButton_previous.raise_()
        self.label.raise_()
        self.pushButton_next.raise_()
        self.pushButton_new.raise_()
        self.toolButton_search2.raise_()
        self.label_9.raise_()
        self.lineEdit_search2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.textBrowser_remark1.raise_()
        self.label_order1.raise_()
        self.label_order2.raise_()
        self.label_order3.raise_()
        self.label_order4.raise_()
        self.label_order5.raise_()
        self.textBrowser_problem2.raise_()
        self.label_name2.raise_()
        self.textBrowser_remark2.raise_()
        self.textBrowser_solution2.raise_()
        self.label_staff2.raise_()
        self.label_id2.raise_()
        self.pushButton_edit2.raise_()
        self.line_3.raise_()
        self.label_name3.raise_()
        self.label_id3.raise_()
        self.pushButton_edit3.raise_()
        self.line_4.raise_()
        self.textBrowser_problem3.raise_()
        self.textBrowser_remark3.raise_()
        self.textBrowser_solution3.raise_()
        self.label_staff3.raise_()
        self.line_5.raise_()
        self.label_name4.raise_()
        self.label_id4.raise_()
        self.textBrowser_problem4.raise_()
        self.textBrowser_remark4.raise_()
        self.textBrowser_solution4.raise_()
        self.pushButton_edit4.raise_()
        self.label_staff4.raise_()
        self.label_id5.raise_()
        self.textBrowser_problem5.raise_()
        self.textBrowser_remark5.raise_()
        self.label_name5.raise_()
        self.textBrowser_solution5.raise_()
        self.label_staff5.raise_()
        self.pushButton_edit5.raise_()
        self.label_handlingTime1.raise_()
        self.label_handlingTime2.raise_()
        self.label_handlingTime3.raise_()
        self.label_handlingTime4.raise_()
        self.label_handlingTime5.raise_()
        self.label_method1.raise_()
        self.label_method2.raise_()
        self.label_method3.raise_()
        self.label_method4.raise_()
        self.label_method5.raise_()
        self.label_classify1.raise_()
        self.label_classify2.raise_()
        self.label_classify3.raise_()
        self.label_classify4.raise_()
        self.label_classify5.raise_()
        self.label_charge1.raise_()
        self.label_charge2.raise_()
        self.label_charge3.raise_()
        self.label_charge4.raise_()
        self.label_charge5.raise_()

        self.retranslateUi(Form)
        self.pushButton_previous.clicked.connect(self.reloadWidgetDec)
        self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
#        self.pushButton_new.clicked.connect(Form.handle_click)
#        self.label_9.linkActivated['QString'].connect(Form.handle_click)
#        self.pushButton_SwitchShipment.clicked.connect(Form.handle_show)
#        self.pushButton_SwitchCustomer.clicked.connect(Form.handle_show)
#        self.pushButton_edit1.clicked.connect(Form.handle_click)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0b3da8;\">售后信息浏览</span></p></body></html>"))
        self.label_id1.setText(_translate("Form", "id"))
        self.label_name1.setText(_translate("Form", "name"))
        self.textBrowser_problem1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.pushButton_SwitchCustomer.setText(_translate("Form", "客户信息界面"))
        self.pushButton_edit1.setText(_translate("Form", "编辑"))
        self.label_6.setText(_translate("Form", "处理人员"))
        self.label_4.setText(_translate("Form", "处理方式"))
        self.label_staff1.setText(_translate("Form", "staff"))
        self.pushButton_SwitchShipment.setText(_translate("Form", "产品出货界面"))
        self.label_8.setText(_translate("Form", "搜索"))
        self.label_5.setText(_translate("Form", "处理时间"))
        self.textBrowser_solution1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_solution</p></body></html>"))
        self.label_2.setText(_translate("Form", "客户名称"))
        self.toolButton_connect.setText(_translate("Form", "..."))
        self.label_7.setText(_translate("Form", "解决方法"))
        self.label_3.setText(_translate("Form", "客户反馈问题"))
        self.toolButton_search.setText(_translate("Form", "..."))
        self.pushButton_previous.setText(_translate("Form", "上一页"))
        self.label.setText(_translate("Form", "售后ID"))
        self.pushButton_next.setText(_translate("Form", "下一页"))
        self.pushButton_new.setText(_translate("Form", "新增售后信息"))
        self.toolButton_search2.setText(_translate("Form", "..."))
        self.label_9.setText(_translate("Form", "跳到第       页"))
        self.label_10.setText(_translate("Form", "收费金额"))
        self.label_11.setText(_translate("Form", "问题归类"))
        self.label_12.setText(_translate("Form", "备注"))
        self.textBrowser_remark1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.label_order1.setText(_translate("Form", "1"))
        self.label_order2.setText(_translate("Form", "2"))
        self.label_order3.setText(_translate("Form", "3"))
        self.label_order4.setText(_translate("Form", "4"))
        self.label_order5.setText(_translate("Form", "5"))
        self.textBrowser_problem2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.label_name2.setText(_translate("Form", "name"))
        self.textBrowser_remark2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.textBrowser_solution2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_solution</p></body></html>"))
        self.label_staff2.setText(_translate("Form", "staff"))
        self.label_id2.setText(_translate("Form", "id"))
        self.pushButton_edit2.setText(_translate("Form", "编辑"))
        self.label_name3.setText(_translate("Form", "name"))
        self.label_id3.setText(_translate("Form", "id"))
        self.pushButton_edit3.setText(_translate("Form", "编辑"))
        self.textBrowser_problem3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.textBrowser_remark3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.textBrowser_solution3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_solution</p></body></html>"))
        self.label_staff3.setText(_translate("Form", "staff"))
        self.label_name4.setText(_translate("Form", "name"))
        self.label_id4.setText(_translate("Form", "id"))
        self.textBrowser_problem4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.textBrowser_remark4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.textBrowser_solution4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_solution</p></body></html>"))
        self.pushButton_edit4.setText(_translate("Form", "编辑"))
        self.label_staff4.setText(_translate("Form", "staff"))
        self.label_id5.setText(_translate("Form", "id"))
        self.textBrowser_problem5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.textBrowser_remark5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.label_name5.setText(_translate("Form", "name"))
        self.textBrowser_solution5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_solution</p></body></html>"))
        self.label_staff5.setText(_translate("Form", "staff"))
        self.pushButton_edit5.setText(_translate("Form", "编辑"))
        self.label_handlingTime1.setText(_translate("Form", "handlingTime"))
        self.label_handlingTime2.setText(_translate("Form", "handlingTime"))
        self.label_handlingTime3.setText(_translate("Form", "handlingTime"))
        self.label_handlingTime4.setText(_translate("Form", "handlingTime"))
        self.label_handlingTime5.setText(_translate("Form", "handlingTime"))
        self.label_method1.setText(_translate("Form", "method"))
        self.label_method2.setText(_translate("Form", "method"))
        self.label_method3.setText(_translate("Form", "method"))
        self.label_method4.setText(_translate("Form", "method"))
        self.label_method5.setText(_translate("Form", "method"))
        self.label_classify1.setText(_translate("Form", "classify"))
        self.label_classify2.setText(_translate("Form", "classify"))
        self.label_classify3.setText(_translate("Form", "classify"))
        self.label_classify4.setText(_translate("Form", "classify"))
        self.label_classify5.setText(_translate("Form", "classify"))
        self.label_charge1.setText(_translate("Form", "charge"))
        self.label_charge2.setText(_translate("Form", "charge"))
        self.label_charge3.setText(_translate("Form", "charge"))
        self.label_charge4.setText(_translate("Form", "charge"))
        self.label_charge5.setText(_translate("Form", "charge"))

####以上为QTDesiger自动生成代码
###以下为自己写的代码
    def closeEvent(self, event):        #关闭窗口触发以下事件
        reply = QMessageBox.question(self, '消息提示', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        #接受关闭事件
        else:
            event.ignore()        #忽略关闭事件

    def reloadWidgetAdd(self,i): #点击下一页触发
        print ("reloadWidgeAdd")
        i= int(self.label_order5.text())
        if i < dblen: #dblen():
#            global g
            NextOffice.service.service_main.g=NextOffice.service.service_main.g+1 #全局变量P页数+1
            self.pageDisplay(NextOffice.service.service_main.g)
            print("service_main的g是",NextOffice.service.service_main.g)

        else:
            print("remain")
    def reloadWidgetDec(self,i): #点击上一页触发
        print ("reloadWidgeDec")
        i= int(self.label_order5.text())
        if i > 5:
            global g
            NextOffice.service.service_main.g=NextOffice.service.service_main.g-1 #全局变量P页数+1
#            g=g-1 #全局变量P页数-1
            self.pageDisplay(NextOffice.service.service_main.g)
        else:
            print("remain")
    def pageDisplay(self,g):  #本函数显示g页的数据
        print("pageDisplay",g)
        orderE=g*5
        orderD=orderE-1
        orderC=orderE-2
        orderB=orderE-3
        orderA=orderE-4
        self.label_order1.setText(str(orderA))
        self.label_order2.setText(str(orderB))
        self.label_order3.setText(str(orderC))
        self.label_order4.setText(str(orderD))
        self.label_order5.setText(str(orderE))

        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("pageData()打开数据库成功")
        curs.execute("SELECT * from service")
        data= curs.fetchall()

        p=g*5-4  #获得当前页面的第1行

        blank=["","","","","","","","","",""]
        a=dblen%5 #计算最后一页总共有几行？
        b=5-a  #计算空白的有几行
        c=0
        while c<b:#将当前页面的空白记录行填充N/A，以免data赋值的时候不够5行导致出错
            data.append(blank)
            c=c+1

        print("here")

#以下将数据库中获取的内容分别对应显示在5行内
        self.label_id1.setText(str(data[p-1][0])) #数据库是从0开始的，所以减1
        self.label_name1.setText(str(data[p-1][1]))
        self.textBrowser_problem1.setText(str(data[p-1][2]))
        self.label_method1.setText(str(data[p-1][3]))
        self.label_handlingTime1.setText(str(data[p-1][4]))
        self.label_staff1.setText(str(data[p-1][5]))
        self.textBrowser_solution1.setText(str(data[p-1][6]))
        self.label_charge1.setText(str(data[p-1][7]))
        self.label_classify1.setText(str(data[p-1][8]))
        self.textBrowser_remark1.setText(str(data[p-1][9]))

        self.label_id2.setText(str(data[p][0]))
        self.label_name2.setText(str(data[p][1]))
        self.textBrowser_problem2.setText(str(data[p][2]))
        self.label_method2.setText(str(data[p][3]))
        self.label_handlingTime2.setText(str(data[p][4]))
        self.label_staff2.setText(str(data[p][5]))
        self.textBrowser_solution2.setText(str(data[p][6]))
        self.label_charge2.setText(str(data[p][7]))
        self.label_classify2.setText(str(data[p][8]))
        self.textBrowser_remark2.setText(str(data[p][9]))

        self.label_id3.setText(str(data[p+1][0]))
        self.label_name3.setText(str(data[p+1][1]))
        self.textBrowser_problem3.setText(str(data[p+1][2]))
        self.label_method3.setText(str(data[p+1][3]))
        self.label_handlingTime3.setText(str(data[p+1][4]))
        self.label_staff3.setText(str(data[p+1][5]))
        self.textBrowser_solution3.setText(str(data[p+1][6]))
        self.label_charge3.setText(str(data[p+1][7]))
        self.label_classify3.setText(str(data[p+1][8]))
        self.textBrowser_remark3.setText(str(data[p+1][9]))

        self.label_id4.setText(str(data[p+2][0]))
        self.label_name4.setText(str(data[p+2][1]))
        self.textBrowser_problem4.setText(str(data[p+2][2]))
        self.label_method4.setText(str(data[p+2][3]))
        self.label_handlingTime4.setText(str(data[p+2][4]))
        self.label_staff4.setText(str(data[p+2][5]))
        self.textBrowser_solution4.setText(str(data[p+2][6]))
        self.label_charge4.setText(str(data[p+2][7]))
        self.label_classify4.setText(str(data[p+2][8]))
        self.textBrowser_remark4.setText(str(data[p+2][9]))

        self.label_id5.setText(str(data[p+3][0]))
        self.label_name5.setText(str(data[p+3][1]))
        self.textBrowser_problem5.setText(str(data[p+3][2]))
        self.label_method5.setText(str(data[p+3][3]))
        self.label_handlingTime5.setText(str(data[p+3][4]))
        self.label_staff5.setText(str(data[p+3][5]))
        self.textBrowser_solution5.setText(str(data[p+3][6]))
        self.label_charge5.setText(str(data[p+3][7]))
        self.label_classify5.setText(str(data[p+3][8]))
        self.textBrowser_remark5.setText(str(data[p+3][9]))

        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
    def page(self):
        global g
        g=g+0
        return g
    def reload(self):
        print("browser:reload start")
        print("g=",NextOffice.service.service_main.g)
        print("???")
        self.pageDisplay(NextOffice.service.service_main.g)
        print("browser:reload finish")

def dblen():
        conn = sqlite3.connect('nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("打开数据库成功")

        curs.execute("SELECT * from service")
        data= curs.fetchall()
#        print (data[10])
        print (data[0][7])
#        print (data[0][1])

        lens=len(data)
        print ("开始运行数据库共有记录：",lens)

        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return lens


class MyForm ( QWidget, Ui_Form ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
#       g=NextOffice.customer.customer_main.g

dblen=dblen() #获取数据库的总长度，赋值给变量dblen，这样就不需要每次去获取了


if __name__=='__main__':
#    global g #全局变量p——当前页面
    g=1
#    dblen=dblen() #获取数据库的总长度，赋值给变量dblen，这样就不需要每次去获取了
    app=QApplication(sys.argv)
    w = MyForm()
    w.pageDisplay(1)
    w.show()
    a = NextOffice.service.service_edit.MyForm()
    w.pushButton_edit1.clicked.connect(a.handle_click1)
    w.pushButton_edit2.clicked.connect(a.handle_click2)
    w.pushButton_edit3.clicked.connect(a.handle_click3)
    w.pushButton_edit4.clicked.connect(a.handle_click4)
    w.pushButton_edit5.clicked.connect(a.handle_click5)

    app.exec_()



"""
UIC之后，将以下2个语句中的Main修改为self即可
self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""
