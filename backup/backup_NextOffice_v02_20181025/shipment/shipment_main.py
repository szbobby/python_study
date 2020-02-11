import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import NextOffice.shipment.shipment_browser
import NextOffice.shipment.shipment_add
import NextOffice.shipment.shipment_edit



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

def click_showShipment():
    app=QApplication(sys.argv) #格式
    print("today is Sunday")
#    dblen=NextOffice.shipment.shipment_browser.dblen()

# 引入3个页面
    b = NextOffice.shipment.shipment_browser.MyForm()
    e = NextOffice.shipment.shipment_edit.MyForm()
    a = NextOffice.shipment.shipment_add.MyForm()

    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示
# 点击“编辑”弹出编辑窗口
    b.pushButton_edit1.clicked.connect(e.handle_click1)
    b.pushButton_edit2.clicked.connect(e.handle_click2)
    b.pushButton_edit3.clicked.connect(e.handle_click3)
    b.pushButton_edit4.clicked.connect(e.handle_click4)
    b.pushButton_edit5.clicked.connect(e.handle_click5)

# 点击“新增售后信息”弹出窗口
    b.pushButton_new.clicked.connect(a.handle_click)


# 点击切换 售后服务记录/客户信息/产品出货界面


    app.exec_() #格式


if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    dblen=dblen()

# 引入3个页面
    b = NextOffice.shipment.shipment_browser.MyForm()
    e = NextOffice.shipment.shipment_edit.MyForm()
    a = NextOffice.shipment.shipment_add.MyForm()

    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示
# 点击“编辑”弹出编辑窗口
    b.pushButton_edit1.clicked.connect(e.handle_click1)
    b.pushButton_edit2.clicked.connect(e.handle_click2)
    b.pushButton_edit3.clicked.connect(e.handle_click3)
    b.pushButton_edit4.clicked.connect(e.handle_click4)
    b.pushButton_edit5.clicked.connect(e.handle_click5)

# 点击“新增售后信息”弹出窗口
    b.pushButton_new.clicked.connect(a.handle_click)

# 编辑或新增信息后，刷新窗口
    e.pushButton_save.clicked.connect(b.reload)
    a.pushButton_save.clicked.connect(b.reload)

# 点击切换到“售后服务记录“与“客户信息””窗口


    app.exec_() #格式


"""
UIC之后，将以下2个语句中的Main修改为self即可
se
if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    dblen=dblen()

# 引入3个页面
    b = NextOffice.service.service_browser.MyForm()
    e = NextOffice.service.service_edit.MyForm()
    a = NextOffice.service.service_add.MyForm()

    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示
# 点击“编辑”弹出编辑窗口
    b.pushButton_edit1.clicked.connect(e.handle_click1)
    b.pushButton_edit2.clicked.connect(e.handle_click2)
    b.pushButton_edit3.clicked.connect(e.handle_click3)
    b.pushButton_edit4.clicked.connect(e.handle_click4)
    b.pushButton_edit5.clicked.connect(e.handle_click5)

# 点击“新增售后信息”弹出窗口
    b.pushButton_new.clicked.connect(a.handle_click)
#    b.QApplication.processEvents()


    app.exec_() #格式
0lf.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""