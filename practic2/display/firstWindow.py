from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class FirstWindow(QWidget):
    close_signal = pyqtSignal()

    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(FirstWindow, self).__init__(parent)
        self.resize(300, 300)
        self.btn = QPushButton(self)
#        self.btn = QToolButton(self)
        self.btn.setText("click")

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()

