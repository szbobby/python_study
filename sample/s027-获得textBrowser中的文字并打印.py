# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_01.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 20, 256, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.lineEdit.textEdited['QString'].connect(self.textBrowser.setText)
        self.pushButton.clicked.connect(Form.bsumit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "点我啊"))

    def bsumit(self):
        boo=self.textBrowser.toPlainText()
        print(boo)


import sys
from PyQt5.QtWidgets import QApplication,QWidget


class myform(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.textBrowser.setText)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=myform()
    w.show()
    app.exec_()
