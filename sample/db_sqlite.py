import sqlite3, sys

#连接数据库,也可以把数据库名称复制为特定的名称 :memory:，这样就会在 RAM 中创建一个数据库
conn = sqlite3.connect('nextai.db')

curs = conn.cursor()  #创建游标
print ("打开数据库成功")

curs.execute('create table shipment \
(id integer primary key, \
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
(id integer primary key, \
customer char(20), \
nickname1 char(20),\
nickname2 char(20),\
nickname3 char(20),\
contact text,\
remark text) ')



curs.execute('create table crm \
(id integer primary key, \
customer char(20), \
nickname1 char(20),\
nickname2 char(20),\
nickname3 char(20),\
contact text,\
remark text) ')



"""
curs.execute('CREATE TABLE company2 (ID INT PRIMARY KEY, NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY CHAR(20))')
"""
#SQL语句：查找ID=2的记录
"""
sql = """SELECT * FROM shipment WHERE id=1;"""  #SQL语句：查找ID=2的记录
curs.execute(sql) #执行SQL语句
value = curs.fetchall()
print(value)
"""

curs.close()  #关闭游标
conn.close() #关闭数据库连接


