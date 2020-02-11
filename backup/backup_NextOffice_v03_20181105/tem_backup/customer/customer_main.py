import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import NextOffice.customer.customer_browser
import NextOffice.customer.customer_add
import NextOffice.customer.customer_edit


def dblen():
        conn = sqlite3.connect('../nextai.db')
        curs = conn.cursor()  #创建游标
#        print ("打开数据库成功")

        curs.execute("SELECT * from customer")
        data= curs.fetchall()
#        print (data[10])
#        print (data[0][0])
#        print (data[0][1])

        lens=len(data)
        print ("数据库共有记录：",lens)


        curs.close()  #关闭游标
        conn.commit() #保存数据库
        conn.close() #关闭数据库连接
        return lens

global g # 设定当前页面全局变量 g
g=1


def click_showCustomer():
    app=QApplication(sys.argv) #格式
    dblen=dblen()

    b = NextOffice.customer.customer_browser.MyForm()
    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示

    e = NextOffice.customer.customer_edit.MyForm()
    b.pushButton_edit01.clicked.connect(e.handle_click1)
    b.pushButton_edit02.clicked.connect(e.handle_click2)
    b.pushButton_edit03.clicked.connect(e.handle_click3)
    b.pushButton_edit04.clicked.connect(e.handle_click4)
    b.pushButton_edit05.clicked.connect(e.handle_click5)

    app.exec_() #格式

if __name__=='__main__':
    app=QApplication(sys.argv) #格式
    dblen=dblen()

    b = NextOffice.customer.customer_browser.MyForm()
    b.pageDisplay(g) #默认显示第1页
    b.show()  #窗口显示

    e = NextOffice.customer.customer_edit.MyForm()
    b.pushButton_edit01.clicked.connect(e.handle_click1)
    b.pushButton_edit02.clicked.connect(e.handle_click2)
    b.pushButton_edit03.clicked.connect(e.handle_click3)
    b.pushButton_edit04.clicked.connect(e.handle_click4)
    b.pushButton_edit05.clicked.connect(e.handle_click5)

    # 点击切换 售后服务记录/客户信息/产品出货界面



    app.exec_() #格式



"""
UIC之后，将以下2个语句中的Main修改为self即可
self.pushButton_next.clicked.connect(self.reloadWidgetAdd)
self.pushButton_previous.clicked.connect(self.reloadWidgetDec)

"""