# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import practic1.firstWindow
import practic1.secondWindow

if __name__ == "__main__":     ### 此为框架结构
    App = QApplication(sys.argv) ###此为框架结构
    fir = practic1.firstWindow.FirstWindow() # 调用firstWindow中的FirstWindow类，生成一个实例fir
    sec = practic1.secondWindow.SecondWindow() #调用secondWidow中的SecondWindow类，生成一个实例sec
    fir.btn.clicked.connect(sec.handle_click) #fir中的按钮btn的click，触发sec中的handle_click函数
#    fir.btn.clicked.connect(fir.hide) #fir中的btn按钮的click，触发fir的hide方法（hide是fir窗体自带的方法，无需定义）
    fir.close_signal.connect(fir.close) #fir中的close信号，触发fir的close方法（close是fir窗体自带的方法，无需定义）
    fir.show() #调用fir窗体的show方法（窗体自带，无需定义），显示fir窗口
    sys.exit(App.exec_()) ### 此为框架结构

