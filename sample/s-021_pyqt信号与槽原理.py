import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSignal

class EmitSignal (QWidget):
    signal_empty = pyqtSignal(name='signal_empty')
    signal_one=pyqtSignal(int, name = 'signal_one')
    signal_two=pyqtSignal(int,str,name='signal_two')

    def __init__(self):
        super(EmitSignal,self).__init__()

    def handle_trigger_empty(self):
        print ('signal_empty be emit')

    def handle_trigger_one(self,value):
        print ('signal_one be emit,value is: %d' %value)

    def handle_trigger_two(self, int_value, str_value):
        print ('signal_one be emit,int_value is: %d, str_value is %s' %(int_value,str_value))


    def emit_signal_empty(self):
        self.signal_empty.connect(self.handle_trigger_empty)
        self.signal_empty.emit()

    def emit_signal_one(self,int_value):
        self.signal_one.connect(self.handle_trigger_one)
        self.signal_one.emit(int_value)

    def emit_signal_two(self,int_value,str_value):
        self.signal_two.connect(self.handle_trigger_two)
        self.signal_two.emit(int_value, str_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = EmitSignal()
    e.emit_signal_empty()
    e.emit_signal_one(132)
    e.emit_signal_two(479548645,"安杰小生：欢迎参加我们的party")
    sys.exit(app.exec_())