import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import NextOffice.service.service_browser
import NextOffice.service.service_add
import NextOffice.service.service_edit
import NextOffice.shipment.shipment_main
import NextOffice.customer.tt


def dblen():
        conn = sqlite3.connect('../nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("打开数据库成功")

        curs.execute("SELECT * from service")
        data= curs.fetchall()
#        print (data[10])
#        print (data[0][0])
#        print (data[0][1])

        lens=len(data)
        print ("main数据库共有记录：",lens)


        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return lens

global g # 设定当前页面全局变量 g
g=1


def click_showTRANS():

    app=QApplication(sys.argv) #格式
#    dblen=dblen()

# 引入3个页面
    b = NextOffice.service.service_browser.MyForm()
    e = NextOffice.service.service_edit.MyForm()
    a = NextOffice.service.service_add.MyForm()
    s = NextOffice.customer.tt.ShowForm()


    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示
# 点击“编辑”弹出编辑窗口
    b.pushButton_edit1.clicked.connect(e.handle_click1)
    b.pushButton_edit2.clicked.connect(e.handle_click2)
    b.pushButton_edit3.clicked.connect(e.handle_click3)
    b.pushButton_edit4.clicked.connect(e.handle_click4)
    b.pushButton_edit5.clicked.connect(e.handle_click5)

# 点击“新增售后信息”弹出窗口
#    b.pushButton_new.clicked.connect(NextOffice.customer.tt.click_showTT)
    b.pushButton_new.clicked.connect(s.showTT)

#  点击切换产品出货界面/客户信息界面/售后服务界面
    b.pushButton_SwitchShipment.clicked.connect(NextOffice.shipment.shipment_main.click_showShipment())
#    b.pushButton_SwitchShipment.clicked.connect(b.close())

    app.exec_() #格式


if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    dblen=dblen()

# 引入3个页面
    b = NextOffice.service.service_browser.MyForm()
    e = NextOffice.service.service_edit.MyForm()
    a = NextOffice.service.service_add.MyForm()
    s = NextOffice.customer.tt.ShowForm()

    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示
# 点击“编辑”弹出编辑窗口
    b.pushButton_edit1.clicked.connect(e.handle_click1)
    b.pushButton_edit2.clicked.connect(e.handle_click2)
    b.pushButton_edit3.clicked.connect(e.handle_click3)
    b.pushButton_edit4.clicked.connect(e.handle_click4)
    b.pushButton_edit5.clicked.connect(e.handle_click5)

    b.pushButton_new.clicked.connect(b.close)
    b.pushButton_new.clicked.connect(s.showTT)

#  点击切换产品出货界面/客户信息界面/售后服务界面
#    b.pushButton_SwitchShipment.clicked.connect(NextOffice.shipment.shipment_main.click_showShipment())
#    b.pushButton_SwitchShipment.clicked.connect(b.close)
    e.pushButton_save.clicked.connect(b.reload)
    a.pushButton_save.clicked.connect(b.reload)

    app.exec_() #格式


"""
UIC之后，将以下2个语句中的Main修改为self即可
self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""