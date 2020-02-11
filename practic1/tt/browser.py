import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import NextOffice.tt.add
import NextOffice.tt.edit
import NextOffice.tt.main

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1262, 656)
        self.label_nick1_3 = QtWidgets.QLabel(Form)
        self.label_nick1_3.setGeometry(QtCore.QRect(350, 330, 111, 31))
        self.label_nick1_3.setObjectName("label_nick1_3")
        self.label_id2 = QtWidgets.QLabel(Form)
        self.label_id2.setGeometry(QtCore.QRect(70, 250, 51, 21))
        self.label_id2.setObjectName("label_id2")
        self.label_nick2_4 = QtWidgets.QLabel(Form)
        self.label_nick2_4.setGeometry(QtCore.QRect(470, 420, 91, 31))
        self.label_nick2_4.setObjectName("label_nick2_4")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(500, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_nick2_3 = QtWidgets.QLabel(Form)
        self.label_nick2_3.setGeometry(QtCore.QRect(470, 330, 91, 31))
        self.label_nick2_3.setObjectName("label_nick2_3")
        self.label_nick1_5 = QtWidgets.QLabel(Form)
        self.label_nick1_5.setGeometry(QtCore.QRect(350, 500, 111, 31))
        self.label_nick1_5.setObjectName("label_nick1_5")
        self.textBrowser_contact4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact4.setGeometry(QtCore.QRect(690, 400, 211, 71))
        self.textBrowser_contact4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact4.setLineWidth(0)
        self.textBrowser_contact4.setObjectName("textBrowser_contact4")
        self.label_id5 = QtWidgets.QLabel(Form)
        self.label_id5.setGeometry(QtCore.QRect(70, 510, 51, 21))
        self.label_id5.setObjectName("label_id5")
        self.label_nick3_1 = QtWidgets.QLabel(Form)
        self.label_nick3_1.setGeometry(QtCore.QRect(570, 150, 111, 31))
        self.label_nick3_1.setObjectName("label_nick3_1")
        self.label_id1 = QtWidgets.QLabel(Form)
        self.label_id1.setGeometry(QtCore.QRect(70, 160, 51, 21))
        self.label_id1.setObjectName("label_id1")
        self.label_id3 = QtWidgets.QLabel(Form)
        self.label_id3.setGeometry(QtCore.QRect(70, 340, 51, 21))
        self.label_id3.setObjectName("label_id3")
        self.textBrowser_contact3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact3.setGeometry(QtCore.QRect(690, 310, 211, 71))
        self.textBrowser_contact3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact3.setLineWidth(0)
        self.textBrowser_contact3.setObjectName("textBrowser_contact3")
        self.pushButton_edit02 = QtWidgets.QPushButton(Form)
        self.pushButton_edit02.setGeometry(QtCore.QRect(1140, 240, 75, 23))
        self.pushButton_edit02.setObjectName("pushButton_edit02")
        self.lineEdit_search = QtWidgets.QLineEdit(Form)
        self.lineEdit_search.setGeometry(QtCore.QRect(50, 40, 113, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.label_name1 = QtWidgets.QLabel(Form)
        self.label_name1.setGeometry(QtCore.QRect(140, 160, 191, 21))
        self.label_name1.setObjectName("label_name1")
        self.label_nick2_5 = QtWidgets.QLabel(Form)
        self.label_nick2_5.setGeometry(QtCore.QRect(470, 500, 91, 31))
        self.label_nick2_5.setObjectName("label_nick2_5")
        self.label_id4 = QtWidgets.QLabel(Form)
        self.label_id4.setGeometry(QtCore.QRect(70, 420, 51, 21))
        self.label_id4.setObjectName("label_id4")
        self.pushButton_edit04 = QtWidgets.QPushButton(Form)
        self.pushButton_edit04.setGeometry(QtCore.QRect(1140, 420, 75, 23))
        self.pushButton_edit04.setObjectName("pushButton_edit04")
        self.textBrowser_contact1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact1.setGeometry(QtCore.QRect(690, 130, 211, 71))
        self.textBrowser_contact1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact1.setLineWidth(0)
        self.textBrowser_contact1.setObjectName("textBrowser_contact1")
        self.label_name4 = QtWidgets.QLabel(Form)
        self.label_name4.setGeometry(QtCore.QRect(140, 430, 191, 21))
        self.label_name4.setObjectName("label_name4")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(20, 70, 1211, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(20, 560, 1211, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_SwitchSevice = QtWidgets.QPushButton(Form)
        self.pushButton_SwitchSevice.setGeometry(QtCore.QRect(1070, 40, 111, 23))
        self.pushButton_SwitchSevice.setObjectName("pushButton_SwitchSevice")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 38, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_order1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_order1.setObjectName("label_order1")
        self.verticalLayout.addWidget(self.label_order1)
        self.label_order2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_order2.setObjectName("label_order2")
        self.verticalLayout.addWidget(self.label_order2)
        self.label_order3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_order3.setObjectName("label_order3")
        self.verticalLayout.addWidget(self.label_order3)
        self.label_order4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_order4.setObjectName("label_order4")
        self.verticalLayout.addWidget(self.label_order4)
        self.label_order5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_order5.setObjectName("label_order5")
        self.verticalLayout.addWidget(self.label_order5)
        self.label_nick1_4 = QtWidgets.QLabel(Form)
        self.label_nick1_4.setGeometry(QtCore.QRect(350, 420, 111, 31))
        self.label_nick1_4.setObjectName("label_nick1_4")
        self.label_nick3_2 = QtWidgets.QLabel(Form)
        self.label_nick3_2.setGeometry(QtCore.QRect(570, 240, 111, 31))
        self.label_nick3_2.setObjectName("label_nick3_2")
        self.pushButton_edit01 = QtWidgets.QPushButton(Form)
        self.pushButton_edit01.setGeometry(QtCore.QRect(1140, 160, 75, 23))
        self.pushButton_edit01.setObjectName("pushButton_edit01")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(770, 80, 71, 39))
        self.label_6.setObjectName("label_6")
        self.textBrowser_contact2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact2.setGeometry(QtCore.QRect(690, 220, 211, 71))
        self.textBrowser_contact2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact2.setLineWidth(0)
        self.textBrowser_contact2.setObjectName("textBrowser_contact2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 200, 1211, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(20, 380, 1211, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 80, 61, 39))
        self.label_4.setObjectName("label_4")
        self.label_nick1_2 = QtWidgets.QLabel(Form)
        self.label_nick1_2.setGeometry(QtCore.QRect(350, 240, 111, 31))
        self.label_nick1_2.setObjectName("label_nick1_2")
        self.textBrowser_remark4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark4.setGeometry(QtCore.QRect(920, 400, 201, 71))
        self.textBrowser_remark4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark4.setLineWidth(0)
        self.textBrowser_remark4.setObjectName("textBrowser_remark4")
        self.label_nick1_1 = QtWidgets.QLabel(Form)
        self.label_nick1_1.setGeometry(QtCore.QRect(350, 150, 111, 31))
        self.label_nick1_1.setObjectName("label_nick1_1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 110, 1211, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_SwitchShipment = QtWidgets.QPushButton(Form)
        self.pushButton_SwitchShipment.setGeometry(QtCore.QRect(950, 40, 111, 23))
        self.pushButton_SwitchShipment.setObjectName("pushButton_SwitchShipment")
        self.label_nick2_2 = QtWidgets.QLabel(Form)
        self.label_nick2_2.setGeometry(QtCore.QRect(470, 240, 91, 31))
        self.label_nick2_2.setObjectName("label_nick2_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 42, 31, 20))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(580, 80, 61, 39))
        self.label_5.setObjectName("label_5")
        self.pushButton_edit05 = QtWidgets.QPushButton(Form)
        self.pushButton_edit05.setGeometry(QtCore.QRect(1140, 510, 75, 23))
        self.pushButton_edit05.setObjectName("pushButton_edit05")
        self.textBrowser_remark1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark1.setGeometry(QtCore.QRect(920, 130, 201, 71))
        self.textBrowser_remark1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark1.setLineWidth(0)
        self.textBrowser_remark1.setObjectName("textBrowser_remark1")
        self.textBrowser_contact5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact5.setGeometry(QtCore.QRect(690, 490, 211, 71))
        self.textBrowser_contact5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact5.setLineWidth(0)
        self.textBrowser_contact5.setObjectName("textBrowser_contact5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 121, 39))
        self.label_2.setObjectName("label_2")
        self.toolButton_connect = QtWidgets.QToolButton(Form)
        self.toolButton_connect.setGeometry(QtCore.QRect(1190, 40, 41, 31))
        self.toolButton_connect.setObjectName("toolButton_connect")
        self.label_name3 = QtWidgets.QLabel(Form)
        self.label_name3.setGeometry(QtCore.QRect(140, 340, 191, 21))
        self.label_name3.setObjectName("label_name3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(1000, 80, 51, 39))
        self.label_7.setObjectName("label_7")
        self.textBrowser_remark3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark3.setGeometry(QtCore.QRect(920, 310, 201, 71))
        self.textBrowser_remark3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark3.setLineWidth(0)
        self.textBrowser_remark3.setObjectName("textBrowser_remark3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 80, 61, 39))
        self.label_3.setObjectName("label_3")
        self.label_name2 = QtWidgets.QLabel(Form)
        self.label_name2.setGeometry(QtCore.QRect(140, 250, 191, 21))
        self.label_name2.setObjectName("label_name2")
        self.toolButton_search = QtWidgets.QToolButton(Form)
        self.toolButton_search.setGeometry(QtCore.QRect(170, 30, 41, 31))
        self.toolButton_search.setObjectName("toolButton_search")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 290, 1211, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_previous = QtWidgets.QPushButton(Form)
        self.pushButton_previous.setGeometry(QtCore.QRect(130, 590, 75, 23))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 470, 1211, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_name5 = QtWidgets.QLabel(Form)
        self.label_name5.setGeometry(QtCore.QRect(140, 510, 191, 21))
        self.label_name5.setObjectName("label_name5")
        self.textBrowser_remark5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark5.setGeometry(QtCore.QRect(920, 490, 201, 71))
        self.textBrowser_remark5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark5.setLineWidth(0)
        self.textBrowser_remark5.setObjectName("textBrowser_remark5")
        self.label_nick2_1 = QtWidgets.QLabel(Form)
        self.label_nick2_1.setGeometry(QtCore.QRect(470, 150, 91, 31))
        self.label_nick2_1.setObjectName("label_nick2_1")
        self.label_nick3_5 = QtWidgets.QLabel(Form)
        self.label_nick3_5.setGeometry(QtCore.QRect(570, 500, 111, 31))
        self.label_nick3_5.setObjectName("label_nick3_5")
        self.pushButton_edit03 = QtWidgets.QPushButton(Form)
        self.pushButton_edit03.setGeometry(QtCore.QRect(1140, 330, 75, 23))
        self.pushButton_edit03.setObjectName("pushButton_edit03")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 61, 39))
        self.label.setObjectName("label")
        self.label_nick3_4 = QtWidgets.QLabel(Form)
        self.label_nick3_4.setGeometry(QtCore.QRect(570, 420, 111, 31))
        self.label_nick3_4.setObjectName("label_nick3_4")
        self.label_nick3_3 = QtWidgets.QLabel(Form)
        self.label_nick3_3.setGeometry(QtCore.QRect(570, 330, 111, 31))
        self.label_nick3_3.setObjectName("label_nick3_3")
        self.textBrowser_remark2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark2.setGeometry(QtCore.QRect(920, 220, 201, 71))
        self.textBrowser_remark2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark2.setLineWidth(0)
        self.textBrowser_remark2.setObjectName("textBrowser_remark2")
        self.pushButton_next = QtWidgets.QPushButton(Form)
        self.pushButton_next.setGeometry(QtCore.QRect(240, 590, 75, 23))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_next_2 = QtWidgets.QPushButton(Form)
        self.pushButton_next_2.setGeometry(QtCore.QRect(580, 590, 91, 23))
        self.pushButton_next_2.setObjectName("pushButton_next_2")
        self.lineEdit_search_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_search_2.setGeometry(QtCore.QRect(410, 590, 31, 20))
        self.lineEdit_search_2.setObjectName("lineEdit_search_2")
        self.toolButton_search_2 = QtWidgets.QToolButton(Form)
        self.toolButton_search_2.setGeometry(QtCore.QRect(480, 580, 41, 31))
        self.toolButton_search_2.setObjectName("toolButton_search_2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(370, 580, 181, 39))
        self.label_9.setObjectName("label_9")
        self.label_nick1_3.raise_()
        self.label_id2.raise_()
        self.label_nick2_4.raise_()
        self.label_13.raise_()
        self.label_nick2_3.raise_()
        self.label_nick1_5.raise_()
        self.textBrowser_contact4.raise_()
        self.label_id5.raise_()
        self.label_nick3_1.raise_()
        self.label_id1.raise_()
        self.label_id3.raise_()
        self.textBrowser_contact3.raise_()
        self.pushButton_edit02.raise_()
        self.lineEdit_search.raise_()
        self.label_name1.raise_()
        self.label_nick2_5.raise_()
        self.label_id4.raise_()
        self.pushButton_edit04.raise_()
        self.textBrowser_contact1.raise_()
        self.label_name4.raise_()
        self.line_7.raise_()
        self.line_6.raise_()
        self.pushButton_SwitchSevice.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_nick1_4.raise_()
        self.label_nick3_2.raise_()
        self.pushButton_edit01.raise_()
        self.label_6.raise_()
        self.textBrowser_contact2.raise_()
        self.line_2.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.label_nick1_2.raise_()
        self.textBrowser_remark4.raise_()
        self.label_nick1_1.raise_()
        self.line.raise_()
        self.pushButton_SwitchShipment.raise_()
        self.label_nick2_2.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.pushButton_edit05.raise_()
        self.textBrowser_remark1.raise_()
        self.textBrowser_contact5.raise_()
        self.label_2.raise_()
        self.toolButton_connect.raise_()
        self.label_name3.raise_()
        self.label_7.raise_()
        self.textBrowser_remark3.raise_()
        self.label_3.raise_()
        self.label_name2.raise_()
        self.toolButton_search.raise_()
        self.line_3.raise_()
        self.pushButton_previous.raise_()
        self.line_5.raise_()
        self.label_name5.raise_()
        self.textBrowser_remark5.raise_()
        self.label_nick2_1.raise_()
        self.label_nick3_5.raise_()
        self.pushButton_edit03.raise_()
        self.label.raise_()
        self.label_nick3_4.raise_()
        self.label_nick3_3.raise_()
        self.textBrowser_remark2.raise_()
        self.pushButton_next.raise_()
        self.pushButton_next_2.raise_()
        self.toolButton_search_2.raise_()
        self.label_9.raise_()
        self.lineEdit_search_2.raise_()

        self.retranslateUi(Form)
        self.pushButton_previous.clicked.connect(self.reloadWidgetDec)
        self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
#        self.pushButton_edit01.clicked.connect(Form.handle_click)
#        self.pushButton_edit02.clicked.connect(Form.handle_click)
#        self.pushButton_edit03.clicked.connect(Form.handle_click)
#        self.pushButton_edit04.clicked.connect(Form.handle_click)
#        self.pushButton_edit05.clicked.connect(Form.handle_click)
#        self.pushButton_next_2.clicked.connect(Form.handle_click)
#        self.label_9.linkActivated['QString'].connect(Form.handle_click)
#        self.pushButton_SwitchShipment.clicked.connect(Form.handle_show)
#        self.pushButton_SwitchSevice.clicked.connect(Form.handle_show)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_nick1_3.setText(_translate("Form", "nick1"))
        self.label_id2.setText(_translate("Form", "id"))
        self.label_nick2_4.setText(_translate("Form", "nick2"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0b3da8;\">客户信息浏览</span></p></body></html>"))
        self.label_nick2_3.setText(_translate("Form", "nick2"))
        self.label_nick1_5.setText(_translate("Form", "nick1"))
        self.textBrowser_contact4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact4</p></body></html>"))
        self.label_id5.setText(_translate("Form", "id"))
        self.label_nick3_1.setText(_translate("Form", "nick3"))
        self.label_id1.setText(_translate("Form", "id"))
        self.label_id3.setText(_translate("Form", "id"))
        self.textBrowser_contact3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact3</p></body></html>"))
        self.pushButton_edit02.setText(_translate("Form", "编辑"))
        self.label_name1.setText(_translate("Form", "name"))
        self.label_nick2_5.setText(_translate("Form", "nick2"))
        self.label_id4.setText(_translate("Form", "id"))
        self.pushButton_edit04.setText(_translate("Form", "编辑"))
        self.textBrowser_contact1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.label_name4.setText(_translate("Form", "name"))
        self.pushButton_SwitchSevice.setText(_translate("Form", "售后服务界面"))
        self.label_order1.setText(_translate("Form", "1"))
        self.label_order2.setText(_translate("Form", "2"))
        self.label_order3.setText(_translate("Form", "3"))
        self.label_order4.setText(_translate("Form", "4"))
        self.label_order5.setText(_translate("Form", "5"))
        self.label_nick1_4.setText(_translate("Form", "nick1"))
        self.label_nick3_2.setText(_translate("Form", "nick3"))
        self.pushButton_edit01.setText(_translate("Form", "编辑"))
        self.label_6.setText(_translate("Form", "联系方式"))
        self.textBrowser_contact2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact2</p></body></html>"))
        self.label_4.setText(_translate("Form", "别称2"))
        self.label_nick1_2.setText(_translate("Form", "nick1"))
        self.textBrowser_remark4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark4</p></body></html>"))
        self.label_nick1_1.setText(_translate("Form", "nick1"))
        self.pushButton_SwitchShipment.setText(_translate("Form", "产品出货界面"))
        self.label_nick2_2.setText(_translate("Form", "nick2"))
        self.label_8.setText(_translate("Form", "搜索"))
        self.label_5.setText(_translate("Form", "别称3"))
        self.pushButton_edit05.setText(_translate("Form", "编辑"))
        self.textBrowser_remark1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.textBrowser_contact5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact5</p></body></html>"))
        self.label_2.setText(_translate("Form", "客户名称"))
        self.toolButton_connect.setText(_translate("Form", "..."))
        self.label_name3.setText(_translate("Form", "name"))
        self.label_7.setText(_translate("Form", "备注"))
        self.textBrowser_remark3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark3</p></body></html>"))
        self.label_3.setText(_translate("Form", "别称1"))
        self.label_name2.setText(_translate("Form", "name"))
        self.toolButton_search.setText(_translate("Form", "..."))
        self.pushButton_previous.setText(_translate("Form", "上一页"))
        self.label_name5.setText(_translate("Form", "name"))
        self.textBrowser_remark5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark5</p></body></html>"))
        self.label_nick2_1.setText(_translate("Form", "nick2"))
        self.label_nick3_5.setText(_translate("Form", "nick3"))
        self.pushButton_edit03.setText(_translate("Form", "编辑"))
        self.label.setText(_translate("Form", "客户ID"))
        self.label_nick3_4.setText(_translate("Form", "nick3"))
        self.label_nick3_3.setText(_translate("Form", "nick3"))
        self.textBrowser_remark2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark2</p></body></html>"))
        self.pushButton_next.setText(_translate("Form", "下一页"))
        self.pushButton_next_2.setText(_translate("Form", "新增客户信息"))
        self.toolButton_search_2.setText(_translate("Form", "..."))
        self.label_9.setText(_translate("Form", "跳到第       页"))

####以上为QTDesiger自动生成代码
###以下为自己写的代码

    def reloadWidgetAdd(self,i): #点击下一页触发
        print ("reloadWidgeAdd")
        i= int(self.label_order5.text())
        if i < dblen: #dblen():
#            global g
            NextOffice.tt.main.g=NextOffice.tt.main.g+1 #全局变量P页数+1
            self.pageDisplay(NextOffice.tt.main.g)
            print("customer_main的g是",NextOffice.tt.main.g)

        else:
            print("remain")
    def reloadWidgetDec(self,i): #点击上一页触发
        print ("reloadWidgeDec")
        i= int(self.label_order5.text())
        if i > 5:
            global g
            NextOffice.tt.main.g=NextOffice.tt.main.g-1 #全局变量P页数+1
#            g=g-1 #全局变量P页数-1
            self.pageDisplay(NextOffice.tt.main.g)
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

        conn = sqlite3.connect('../nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("pageData()打开数据库成功")
        curs.execute("SELECT * from customer")
        data= curs.fetchall()
#        print("here")

        p=g*5-4  #获得当前页面的第1行

        blank=["","","","","","",""]
        a=dblen%5 #计算最后一页总共有几行？
        b=5-a  #计算空白的有几行
        c=0
        while c<b:#将当前页面的空白记录行填充N/A，以免data赋值的时候不够5行导致出错
            data.append(blank)
            c=c+1

#以下将数据库中获取的内容分别对应显示在5行内
        self.label_id1.setText(str(data[p-1][0])) #数据库是从0开始的，所以减1
        self.label_name1.setText(str(data[p-1][1]))
        self.label_nick1_1.setText(str(data[p-1][2]))
        self.label_nick2_1.setText(str(data[p-1][3]))
        self.label_nick3_1.setText(str(data[p-1][4]))
        self.textBrowser_contact1.setText(str(data[p-1][5]))
        self.textBrowser_remark1.setText(str(data[p-1][6]))

        self.label_id2.setText(str(data[p][0]))
        self.label_name2.setText(str(data[p][1]))
        self.label_nick1_2.setText(str(data[p][2]))
        self.label_nick2_2.setText(str(data[p][3]))
        self.label_nick3_2.setText(str(data[p][4]))
        self.textBrowser_contact2.setText(str(data[p][5]))
        self.textBrowser_remark2.setText(str(data[p][6]))

        self.label_id3.setText(str(data[p+1][0]))
        self.label_name3.setText(str(data[p+1][1]))
        self.label_nick1_3.setText(str(data[p+1][2]))
        self.label_nick2_3.setText(str(data[p+1][3]))
        self.label_nick3_3.setText(str(data[p+1][4]))
        self.textBrowser_contact3.setText(str(data[p+1][5]))
        self.textBrowser_remark3.setText(str(data[p+1][6]))

        self.label_id4.setText(str(data[p+2][0]))
        self.label_name4.setText(str(data[p+2][1]))
        self.label_nick1_4.setText(str(data[p+2][2]))
        self.label_nick2_4.setText(str(data[p+2][3]))
        self.label_nick3_4.setText(str(data[p+2][4]))
        self.textBrowser_contact4.setText(str(data[p+2][5]))
        self.textBrowser_remark4.setText(str(data[p+2][6]))

        self.label_id5.setText(str(data[p+3][0]))
        self.label_name5.setText(str(data[p+3][1]))
        self.label_nick1_5.setText(str(data[p+3][2]))
        self.label_nick2_5.setText(str(data[p+3][3]))
        self.label_nick3_5.setText(str(data[p+3][4]))
        self.textBrowser_contact5.setText(str(data[p+3][5]))
        self.textBrowser_remark5.setText(str(data[p+3][6]))

        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
    def page(self):
        global g
        g=g+0
        return g
    def reload(self):
        self.pageDisplay(NextOffice.tt.main.g)


def dblen():
        conn = sqlite3.connect('../nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("打开数据库成功")

        curs.execute("SELECT * from customer")
        data= curs.fetchall()
#        print (data[10])
#        print (data[0][0])
#        print (data[0][1])

        lens=len(data)
        print ("数据库共有记录：",lens)


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
    e = NextOffice.tt.edit.MyForm()
    w.pushButton_edit01.clicked.connect(e.handle_click1)
    w.pushButton_edit02.clicked.connect(e.handle_click2)
    w.pushButton_edit03.clicked.connect(e.handle_click3)
    w.pushButton_edit04.clicked.connect(e.handle_click4)
    w.pushButton_edit05.clicked.connect(e.handle_click5)


    app.exec_()



"""
UIC之后，将以下2个语句中的Main修改为self即可
self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""