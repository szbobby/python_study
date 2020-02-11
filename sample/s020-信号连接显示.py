import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

# 以下：滚动条与数值显示关联
    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 200,250,150)
        self.setWindowTitle('Signal & slot')
        self.show()



# 以下：如果按ESC键就直接退出
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


# 以下：程序运行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())