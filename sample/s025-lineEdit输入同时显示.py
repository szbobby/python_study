# 启动2
# 以下是PYQT5 Widge类型的启动 (form)

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from pyqt5_01 import Ui_Form


class myform(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.textBrowser.setText)
        a=self.textBrowser.setText
        print(a)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=myform()
    w.show()
    app.exec_()
