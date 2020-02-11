from PyQt5 import QtCore, QtGui, QtWidgets #这一条是PYQT5的ui文件自动生成的代码

import sys

#这里以下是PYQT5的ui文件自动生成的代码

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#2066a3;\">这是我的第一个窗体</span></p></body></html>"))

# 这里以上是PYQT5的ui文件自动生成的代码


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
