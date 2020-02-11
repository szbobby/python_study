# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(200, 200)
        self.setStyleSheet("background: black")

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


