from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import practic2.display.secondWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(410, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setGeometry(QtCore.QRect(280, 470, 75, 23))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(390, 470, 75, 23))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_edit01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit01.setGeometry(QtCore.QRect(880, 130, 75, 23))
        self.pushButton_edit01.setObjectName("pushButton_edit01")
        self.pushButton_edit02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit02.setGeometry(QtCore.QRect(880, 190, 75, 23))
        self.pushButton_edit02.setObjectName("pushButton_edit02")
        self.pushButton_edit03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit03.setGeometry(QtCore.QRect(880, 270, 75, 23))
        self.pushButton_edit03.setObjectName("pushButton_edit03")
        self.pushButton_edit04 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit04.setGeometry(QtCore.QRect(880, 330, 75, 23))
        self.pushButton_edit04.setObjectName("pushButton_edit04")
        self.pushButton_edit05 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit05.setGeometry(QtCore.QRect(880, 410, 75, 23))
        self.pushButton_edit05.setObjectName("pushButton_edit05")
        self.pushButton_SwitchShipment = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SwitchShipment.setGeometry(QtCore.QRect(680, 10, 111, 23))
        self.pushButton_SwitchShipment.setObjectName("pushButton_SwitchShipment")
        self.pushButton_SwitchSevice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SwitchSevice.setGeometry(QtCore.QRect(800, 10, 111, 23))
        self.pushButton_SwitchSevice.setObjectName("pushButton_SwitchSevice")
        self.label_id1 = QtWidgets.QLabel(self.centralwidget)
        self.label_id1.setGeometry(QtCore.QRect(60, 120, 51, 21))
        self.label_id1.setObjectName("label_id1")
        self.label_name1 = QtWidgets.QLabel(self.centralwidget)
        self.label_name1.setGeometry(QtCore.QRect(130, 120, 141, 21))
        self.label_name1.setObjectName("label_name1")
        self.label_nick1_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick1_1.setGeometry(QtCore.QRect(280, 110, 61, 31))
        self.label_nick1_1.setObjectName("label_nick1_1")
        self.label_nick2_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick2_1.setGeometry(QtCore.QRect(360, 110, 71, 31))
        self.label_nick2_1.setObjectName("label_nick2_1")
        self.label_nick3_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick3_1.setGeometry(QtCore.QRect(440, 110, 81, 31))
        self.label_nick3_1.setObjectName("label_nick3_1")
        self.textBrowser_contact1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_contact1.setGeometry(QtCore.QRect(530, 110, 181, 51))
        self.textBrowser_contact1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact1.setLineWidth(0)
        self.textBrowser_contact1.setObjectName("textBrowser_contact1")
        self.textBrowser_remark1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_remark1.setGeometry(QtCore.QRect(720, 110, 151, 51))
        self.textBrowser_remark1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark1.setLineWidth(0)
        self.textBrowser_remark1.setObjectName("textBrowser_remark1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 61, 39))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 121, 39))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 61, 39))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 60, 61, 39))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 60, 61, 39))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 60, 71, 39))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(740, 60, 51, 39))
        self.label_7.setObjectName("label_7")
        self.textBrowser_remark2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_remark2.setGeometry(QtCore.QRect(720, 180, 151, 51))
        self.textBrowser_remark2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark2.setLineWidth(0)
        self.textBrowser_remark2.setObjectName("textBrowser_remark2")
        self.textBrowser_contact2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_contact2.setGeometry(QtCore.QRect(530, 180, 181, 51))
        self.textBrowser_contact2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact2.setLineWidth(0)
        self.textBrowser_contact2.setObjectName("textBrowser_contact2")
        self.label_nick1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick1_2.setGeometry(QtCore.QRect(280, 180, 51, 31))
        self.label_nick1_2.setObjectName("label_nick1_2")
        self.label_name2 = QtWidgets.QLabel(self.centralwidget)
        self.label_name2.setGeometry(QtCore.QRect(130, 190, 141, 21))
        self.label_name2.setObjectName("label_name2")
        self.label_nick2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick2_2.setGeometry(QtCore.QRect(360, 180, 71, 31))
        self.label_nick2_2.setObjectName("label_nick2_2")
        self.label_nick3_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick3_2.setGeometry(QtCore.QRect(440, 180, 81, 31))
        self.label_nick3_2.setObjectName("label_nick3_2")
        self.label_id2 = QtWidgets.QLabel(self.centralwidget)
        self.label_id2.setGeometry(QtCore.QRect(60, 190, 51, 21))
        self.label_id2.setObjectName("label_id2")
        self.textBrowser_remark3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_remark3.setGeometry(QtCore.QRect(720, 250, 151, 51))
        self.textBrowser_remark3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark3.setLineWidth(0)
        self.textBrowser_remark3.setObjectName("textBrowser_remark3")
        self.textBrowser_contact3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_contact3.setGeometry(QtCore.QRect(530, 250, 181, 51))
        self.textBrowser_contact3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact3.setLineWidth(0)
        self.textBrowser_contact3.setObjectName("textBrowser_contact3")
        self.label_id4 = QtWidgets.QLabel(self.centralwidget)
        self.label_id4.setGeometry(QtCore.QRect(60, 330, 51, 21))
        self.label_id4.setObjectName("label_id4")
        self.label_nick1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick1_3.setGeometry(QtCore.QRect(280, 250, 61, 31))
        self.label_nick1_3.setObjectName("label_nick1_3")
        self.label_nick3_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick3_4.setGeometry(QtCore.QRect(440, 320, 81, 31))
        self.label_nick3_4.setObjectName("label_nick3_4")
        self.label_name3 = QtWidgets.QLabel(self.centralwidget)
        self.label_name3.setGeometry(QtCore.QRect(130, 260, 141, 21))
        self.label_name3.setObjectName("label_name3")
        self.textBrowser_contact4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_contact4.setGeometry(QtCore.QRect(530, 320, 181, 51))
        self.textBrowser_contact4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact4.setLineWidth(0)
        self.textBrowser_contact4.setObjectName("textBrowser_contact4")
        self.textBrowser_remark4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_remark4.setGeometry(QtCore.QRect(720, 320, 151, 51))
        self.textBrowser_remark4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark4.setLineWidth(0)
        self.textBrowser_remark4.setObjectName("textBrowser_remark4")
        self.label_nick2_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick2_4.setGeometry(QtCore.QRect(360, 320, 71, 31))
        self.label_nick2_4.setObjectName("label_nick2_4")
        self.label_nick1_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick1_4.setGeometry(QtCore.QRect(280, 320, 81, 31))
        self.label_nick1_4.setObjectName("label_nick1_4")
        self.label_nick2_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick2_3.setGeometry(QtCore.QRect(360, 250, 71, 31))
        self.label_nick2_3.setObjectName("label_nick2_3")
        self.label_name4 = QtWidgets.QLabel(self.centralwidget)
        self.label_name4.setGeometry(QtCore.QRect(130, 330, 141, 21))
        self.label_name4.setObjectName("label_name4")
        self.label_nick3_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick3_3.setGeometry(QtCore.QRect(440, 250, 81, 31))
        self.label_nick3_3.setObjectName("label_nick3_3")
        self.label_id3 = QtWidgets.QLabel(self.centralwidget)
        self.label_id3.setGeometry(QtCore.QRect(60, 260, 51, 21))
        self.label_id3.setObjectName("label_id3")
        self.textBrowser_remark5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_remark5.setGeometry(QtCore.QRect(720, 390, 151, 51))
        self.textBrowser_remark5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark5.setLineWidth(0)
        self.textBrowser_remark5.setObjectName("textBrowser_remark5")
        self.textBrowser_contact5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_contact5.setGeometry(QtCore.QRect(530, 390, 181, 51))
        self.textBrowser_contact5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact5.setLineWidth(0)
        self.textBrowser_contact5.setObjectName("textBrowser_contact5")
        self.label_nick1_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick1_5.setGeometry(QtCore.QRect(280, 390, 81, 31))
        self.label_nick1_5.setObjectName("label_nick1_5")
        self.label_name5 = QtWidgets.QLabel(self.centralwidget)
        self.label_name5.setGeometry(QtCore.QRect(130, 400, 141, 21))
        self.label_name5.setObjectName("label_name5")
        self.label_nick2_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick2_5.setGeometry(QtCore.QRect(360, 390, 71, 31))
        self.label_nick2_5.setObjectName("label_nick2_5")
        self.label_nick3_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_nick3_5.setGeometry(QtCore.QRect(440, 390, 81, 31))
        self.label_nick3_5.setObjectName("label_nick3_5")
        self.label_id5 = QtWidgets.QLabel(self.centralwidget)
        self.label_id5.setGeometry(QtCore.QRect(60, 400, 51, 21))
        self.label_id5.setObjectName("label_id5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 100, 38, 341))
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
        self.toolButton_connect = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_connect.setGeometry(QtCore.QRect(920, 10, 41, 31))
        self.toolButton_connect.setObjectName("toolButton_connect")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 981, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 160, 981, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 230, 981, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 300, 981, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 370, 981, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 440, 981, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 50, 981, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.toolButton_search = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_search.setGeometry(QtCore.QRect(170, 0, 41, 31))
        self.toolButton_search.setObjectName("toolButton_search")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(50, 10, 113, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 12, 31, 20))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionabout_AI_office = QtWidgets.QAction(MainWindow)
        self.actionabout_AI_office.setObjectName("actionabout_AI_office")
        self.menu.addAction(self.actionabout_AI_office)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
        self.pushButton_previous.clicked.connect(self.reloadWidgetDec)
#        self.pushButton_edit01.clicked.connect(practic2.display.secondWindow.sec.handle_click())
#        self.pushButton_edit02.clicked.connect(MainWindow.show)
#        self.pushButton_edit03.clicked.connect(MainWindow.show)
#        self.pushButton_edit04.clicked.connect(MainWindow.show)
#        self.pushButton_edit05.clicked.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0b3da8;\">客户信息浏览</span></p></body></html>"))
        self.pushButton_previous.setText(_translate("MainWindow", "上一页"))
        self.pushButton_next.setText(_translate("MainWindow", "下一页"))
        self.pushButton_edit01.setText(_translate("MainWindow", "编辑"))
        self.pushButton_edit02.setText(_translate("MainWindow", "编辑"))
        self.pushButton_edit03.setText(_translate("MainWindow", "编辑"))
        self.pushButton_edit04.setText(_translate("MainWindow", "编辑"))
        self.pushButton_edit05.setText(_translate("MainWindow", "编辑"))
        self.pushButton_SwitchShipment.setText(_translate("MainWindow", "产品出货界面"))
        self.pushButton_SwitchSevice.setText(_translate("MainWindow", "售后服务界面"))
        self.label_id1.setText(_translate("MainWindow", "id"))
        self.label_name1.setText(_translate("MainWindow", "name"))
        self.label_nick1_1.setText(_translate("MainWindow", "nick1"))
        self.label_nick2_1.setText(_translate("MainWindow", "nick2"))
        self.label_nick3_1.setText(_translate("MainWindow", "nick3"))
        self.textBrowser_contact1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact1</p></body></html>"))
        self.textBrowser_remark1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark1</p></body></html>"))
        self.label.setText(_translate("MainWindow", "客户ID"))
        self.label_2.setText(_translate("MainWindow", "客户名称"))
        self.label_3.setText(_translate("MainWindow", "别称1"))
        self.label_4.setText(_translate("MainWindow", "别称2"))
        self.label_5.setText(_translate("MainWindow", "别称3"))
        self.label_6.setText(_translate("MainWindow", "联系方式"))
        self.label_7.setText(_translate("MainWindow", "备注"))
        self.textBrowser_remark2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark2</p></body></html>"))
        self.textBrowser_contact2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact2</p></body></html>"))
        self.label_nick1_2.setText(_translate("MainWindow", "nick1"))
        self.label_name2.setText(_translate("MainWindow", "name"))
        self.label_nick2_2.setText(_translate("MainWindow", "nick2"))
        self.label_nick3_2.setText(_translate("MainWindow", "nick3"))
        self.label_id2.setText(_translate("MainWindow", "id"))
        self.textBrowser_remark3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark3</p></body></html>"))
        self.textBrowser_contact3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact3</p></body></html>"))
        self.label_id4.setText(_translate("MainWindow", "id"))
        self.label_nick1_3.setText(_translate("MainWindow", "nick1"))
        self.label_nick3_4.setText(_translate("MainWindow", "nick3"))
        self.label_name3.setText(_translate("MainWindow", "name"))
        self.textBrowser_contact4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact4</p></body></html>"))
        self.textBrowser_remark4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark4</p></body></html>"))
        self.label_nick2_4.setText(_translate("MainWindow", "nick2"))
        self.label_nick1_4.setText(_translate("MainWindow", "nick1"))
        self.label_nick2_3.setText(_translate("MainWindow", "nick2"))
        self.label_name4.setText(_translate("MainWindow", "name"))
        self.label_nick3_3.setText(_translate("MainWindow", "nick3"))
        self.label_id3.setText(_translate("MainWindow", "id"))
        self.textBrowser_remark5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_remark5</p></body></html>"))
        self.textBrowser_contact5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">textBrowser_contact5</p></body></html>"))
        self.label_nick1_5.setText(_translate("MainWindow", "nick1"))
        self.label_name5.setText(_translate("MainWindow", "name"))
        self.label_nick2_5.setText(_translate("MainWindow", "nick2"))
        self.label_nick3_5.setText(_translate("MainWindow", "nick3"))
        self.label_id5.setText(_translate("MainWindow", "id"))
        self.label_order1.setText(_translate("MainWindow", "1"))
        self.label_order2.setText(_translate("MainWindow", "2"))
        self.label_order3.setText(_translate("MainWindow", "3"))
        self.label_order4.setText(_translate("MainWindow", "4"))
        self.label_order5.setText(_translate("MainWindow", "5"))
        self.toolButton_connect.setText(_translate("MainWindow", "..."))
        self.toolButton_search.setText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "搜索"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.actionabout_AI_office.setText(_translate("MainWindow", "about AI.office"))

####以上为QTDesiger自动生成代码
###以下为自己写的代码

    def reloadWidgetAdd(self,i): #点击下一页触发
        print ("reloadWidgeAdd")
        i= int(self.label_order5.text())
        if i < dblen: #dblen():
            global g
            g=g+1 #全局变量P页数+1
            self.pageDisplay(g)
        else:
            print("remain")
    def reloadWidgetDec(self,i): #点击上一页触发
        print ("reloadWidgeDec")
        i= int(self.label_order5.text())
        if i > 5:
            global g
            g=g-1 #全局变量P页数-1
            self.pageDisplay(g)
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
        print("here")

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

import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import practic2.display.customer_edit

if __name__ == '__main__':
    global g #全局变量p——当前页面
    g=1
    dblen=dblen() #获取数据库的总长度，赋值给变量dblen，这样就不需要每次去获取了
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.pageDisplay(g)
#    ui.reloadWidget()
#   lo.logit()  # 运行lo.py文件中的logit()函数
    mainWindow.show()
#    sec = practic2.secondWindow.SecondWindow() #调用secondWidow中的SecondWindow类，生成一个实例sec
    a = practic2.display.customer_edit.MyForm()
    ui.pushButton_edit01.clicked.connect(a.handle_click)

    sys.exit(app.exec_())






"""
UIC之后，将以下2个语句中的Main修改为self即可
self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""