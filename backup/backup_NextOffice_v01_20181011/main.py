from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import NextOffice.service.service_browser
import NextOffice.service.service_add
import NextOffice.service.service_edit
import NextOffice.shipment.shipment_browser
import NextOffice.shipment.shipment_edit
import NextOffice.shipment.shipment_add
import NextOffice.customer.customer_browser
import NextOffice.customer.customer_edit
import NextOffice.customer.customer_add


if __name__=='__main__':
    app=QApplication(sys.argv) #格式

### 引入3个brower页面
    customerB = NextOffice.customer.customer_browser.MyForm()
    shipmentB = NextOffice.shipment.shipment_browser.MyForm()
    serviceB = NextOffice.service.service_browser.MyForm()

    customerB.pageDisplay(1) #默认显示第1页
    shipmentB.pageDisplay(1) #默认显示第1页
    serviceB.pageDisplay(1) #默认显示第1页
    shipmentB.show()  #默认显示产品出货页面


### 引入3个edit页面
    shipmentE = NextOffice.shipment.shipment_edit.MyForm()
    serviceE = NextOffice.service.service_edit.MyForm()
    customerE = NextOffice.customer.customer_edit.MyForm()


### 引入3个add页面
    shipmentA = NextOffice.shipment.shipment_add.MyForm()
    serviceA = NextOffice.service.service_add.MyForm()
    customerA = NextOffice.customer.customer_add.MyForm()


# browser页面点击切换不同窗口：产品出货/售后服务/客户信息
    customerB.pushButton_SwitchShipment.clicked.connect(shipmentB.show)
    customerB.pushButton_SwitchShipment.clicked.connect(customerB.hide)
    serviceB.pushButton_SwitchShipment.clicked.connect(shipmentB.show)
    serviceB.pushButton_SwitchShipment.clicked.connect(serviceB.hide)

    shipmentB.pushButton_SwitchCustomer.clicked.connect(customerB.show)
    shipmentB.pushButton_SwitchCustomer.clicked.connect(shipmentB.hide)
    serviceB.pushButton_SwitchCustomer.clicked.connect(customerB.show)
    serviceB.pushButton_SwitchCustomer.clicked.connect(serviceB.hide)

    shipmentB.pushButton_SwitchService.clicked.connect(serviceB.show)
    shipmentB.pushButton_SwitchService.clicked.connect(shipmentB.hide)
    customerB.pushButton_SwitchSevice.clicked.connect(serviceB.show)
    customerB.pushButton_SwitchSevice.clicked.connect(customerB.hide)

# browser页面点击“编辑”弹出编辑窗口
    customerB.pushButton_edit01.clicked.connect(customerE.handle_click1)
    customerB.pushButton_edit02.clicked.connect(customerE.handle_click2)
    customerB.pushButton_edit03.clicked.connect(customerE.handle_click3)
    customerB.pushButton_edit04.clicked.connect(customerE.handle_click4)
    customerB.pushButton_edit05.clicked.connect(customerE.handle_click5)

    shipmentB.pushButton_edit1.clicked.connect(shipmentE.handle_click1)
    shipmentB.pushButton_edit2.clicked.connect(shipmentE.handle_click2)
    shipmentB.pushButton_edit3.clicked.connect(shipmentE.handle_click3)
    shipmentB.pushButton_edit4.clicked.connect(shipmentE.handle_click4)
    shipmentB.pushButton_edit5.clicked.connect(shipmentE.handle_click5)

    serviceB.pushButton_edit1.clicked.connect(serviceE.handle_click1)
    serviceB.pushButton_edit2.clicked.connect(serviceE.handle_click2)
    serviceB.pushButton_edit3.clicked.connect(serviceE.handle_click3)
    serviceB.pushButton_edit4.clicked.connect(serviceE.handle_click4)
    serviceB.pushButton_edit5.clicked.connect(serviceE.handle_click5)


# browser页面点击“新增”弹出新增窗口
    customerB.pushButton_new.clicked.connect(customerA.handle_click)
    serviceB.pushButton_new.clicked.connect(serviceA.handle_click)
    shipmentB.pushButton_new.clicked.connect(shipmentA.handle_click)


# edit编辑或add新增信息后，刷新browser窗口
    customerE.pushButton_save.clicked.connect(customerB.reload)
    customerA.pushButton_save.clicked.connect(customerB.reload)
    serviceE.pushButton_save.clicked.connect(serviceB.reload)
    serviceA.pushButton_save.clicked.connect(serviceB.reload)
    shipmentE.pushButton_save.clicked.connect(shipmentB.reload)
    shipmentA.pushButton_save.clicked.connect(shipmentB.reload)


    app.exec_() #格式



