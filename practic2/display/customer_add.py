# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 618)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setAutoFillBackground(True)
        self.textBrowser_remark = QtWidgets.QTextBrowser(Form)
        self.textBrowser_remark.setGeometry(QtCore.QRect(300, 490, 181, 111))
        self.textBrowser_remark.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_remark.setLineWidth(0)
        self.textBrowser_remark.setObjectName("textBrowser_remark")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(160, 10, 161, 31))
        self.label_13.setObjectName("label_13")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 61, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 50, 161, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_2.addWidget(self.lineEdit_id)
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 60, 181, 271))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_id = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_id.setObjectName("label_id")
        self.verticalLayout_3.addWidget(self.label_id)
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
        self.textBrowser_contact = QtWidgets.QTextBrowser(Form)
        self.textBrowser_contact.setGeometry(QtCore.QRect(300, 360, 181, 111))
        self.textBrowser_contact.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_contact.setLineWidth(0)
        self.textBrowser_contact.setObjectName("textBrowser_contact")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 480, 59, 52))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 59, 61))
        self.label_6.setObjectName("label_6")
        self.lineEdit_contact = QtWidgets.QLineEdit(Form)
        self.lineEdit_contact.setGeometry(QtCore.QRect(120, 360, 161, 20))
        self.lineEdit_contact.setObjectName("lineEdit_contact")
        self.lineEdit_remark = QtWidgets.QLineEdit(Form)
        self.lineEdit_remark.setGeometry(QtCore.QRect(120, 490, 161, 20))
        self.lineEdit_remark.setObjectName("lineEdit_remark")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 550, 201, 61))
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

        self.retranslateUi(Form)
        self.pushButton_save.clicked.connect(Form.bsumit)
        self.lineEdit_id.textChanged['QString'].connect(self.label_id.setText)
        self.lineEdit_name.textChanged['QString'].connect(self.label_name.setText)
        self.lineEdit_nick1.textChanged['QString'].connect(self.label_nick1.setText)
        self.lineEdit_nick2.textChanged['QString'].connect(self.label_nick2.setText)
        self.lineEdit_nick3.textChanged['QString'].connect(self.label_nick3.setText)
        self.lineEdit_contact.textChanged['QString'].connect(self.textBrowser_contact.setText)
        self.lineEdit_remark.textChanged['QString'].connect(self.textBrowser_remark.setText)
        self.pushButton_cancel.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">新增客户信息</span></p></body></html>"))
        self.label.setText(_translate("Form", "客户ID"))
        self.label_2.setText(_translate("Form", "客户名称"))
        self.label_3.setText(_translate("Form", "别称1"))
        self.label_4.setText(_translate("Form", "别称2"))
        self.label_5.setText(_translate("Form", "别称3"))
        self.lineEdit_id.setText(_translate("Form", "aa"))
        self.label_id.setText(_translate("Form", "id"))
        self.label_name.setText(_translate("Form", "name"))
        self.label_nick1.setText(_translate("Form", "nick1"))
        self.label_nick2.setText(_translate("Form", "nick2"))
        self.label_nick3.setText(_translate("Form", "nick3"))
        self.label_7.setText(_translate("Form", "备注"))
        self.label_6.setText(_translate("Form", "联系方式"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))

