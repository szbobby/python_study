import lo  # 引入Log文件，引入的同时就会运行lo.py程序

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

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=myform()
    w.show()
    app.exec_()


"""


# 启动1
# 以下是PYQT5 MainWindow类型的启动
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstPyQt5 import *

if __name__ == "__main__":
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
#   lo.logit()  # 运行lo.py文件中的logit()函数
    mainWindow.show()
    sys.exit(app.exec_())



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

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=myform()
    w.show()
    app.exec_()

"""