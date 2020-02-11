import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import NextOffice.display.customer_display
import NextOffice.display.customer_edit

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = NextOffice.display.customer_display.Ui_MainWindow()
    ui.setupUi(mainWindow)
#    global g
#    g=1
#    ui.pageDisplay(g)
#    ui.reloadWidget()
#   lo.logit()  # 运行lo.py文件中的logit()函数
    mainWindow.show()
    sys.exit(app.exec_())