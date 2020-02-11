import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QTableWidget,QHBoxLayout, QTableWidgetItem, QComboBox,QFrame
from PyQt5.QtGui import QFont,QColor,QBrush,QPixmap
class TableSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        horizontalHeader = ["工号","姓名","性别","年龄","职称"]

        self.table = QTableWidget() # 也可以QTableWidget(5,2)
        self.table.setColumnCount(5) # 5列

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 348)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 131, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 321, 211))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "测试一下"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "第1行"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "第2行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "第一列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "第二列"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "第三列"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1-1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1-2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "1-3"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "2-1"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "2-2"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "2-3"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    table = TableSheet()
    table.setWindowTitle('表格标头')
    table.resize(700,300)
    table.show()
    sys.exit(app.exec_())

