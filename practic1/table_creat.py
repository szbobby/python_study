import sqlite3, sys

"""
#连接数据库,也可以把数据库名称复制为特定的名称 :memory:，这样就会在 RAM 中创建一个数据库
conn = sqlite3.connect('nextai.db')
curs = conn.cursor()  #创建游标
print ("打开数据库成功")

curs.execute('create table shipment \
(shipmentID integer primary key, \
shipDate char(20), \
customer char(50),\
salesman char(20),\
production char(20),\
model char(10),\
macID integer, \
number integer, \
unitPrice real, \
amount real, \
paid real, \
deducton real, \
receivable real, \
paid1 real, pRemark1 text, \
paid2 real, pRemark2 text, \
paid3 real, pRemark3 text,\
paid4 real, pRemark4 text,\
paid5 real, pRemark5 text,\
payTerm text, \
shipto text, \
remark text) ')


curs.execute('create table crm \
(customerID integer primary key, \
customer char(20), \
nickname1 char(20),\
nickname2 char(20),\
nickname3 char(20),\
contact text,\
remark text) ')



curs.execute('create table service \
(serviceID integer primary key, \
customer char(20), \
problem text,\
processing_method char(20),\
handingTime text,\
staff text,\
processing text,\
charge text,\
classify char(20),\
remark text) ')

"""

#SQL语句：查找ID=2的记录
"""
curs.execute(sql) #执行SQL语句
value = curs.fetchall()
print(value)
"""
"""
curs.close()  #关闭游标
conn.close() #关闭数据库连接
"""
########

conn = sqlite3.connect('nextai.db')
curs = conn.cursor()  #创建游标
print ("第2次打开数据库成功")

curs.execute('insert into crm (customerID, customer, nickname1, nickname2,nickname3,contact,remark ) values (20180004,"集团","cd","cici","dangdang","13692894229灵非","这个是备注")');

#####

cur = conn.execute("SELECT customerID, customer, nickname1, nickname2,nickname3,contact,remark  from crm")

for row in cur:
   print ("客户ID = ", row[0])
   print ("客户名称 = ", row[1])
   print ("别称1 = ", row[2])
   print ("别称2 = ", row[3])
   print ("别称3 = ", row[4])
   print ("联系方式 = ", row[5])
   print ("备注 = ", row[6], "\n")

curs.close()  #关闭游标

conn.commit()
conn.close() #关闭数据库连接
