import sqlite3, sys

conn = sqlite3.connect('nextai.db')
c = conn.cursor()
print ("Opened database successfully")

cur = c.execute("SELECT customerID, customer, nickname1, nickname2,nickname3,contact,remark  from customer")


for row in cur:
   print ("客户ID = ", row[0])
   print ("客户名称 = ", row[1])
   print ("别称1 = ", row[2])
   print ("别称2 = ", row[3])
   print ("别称3 = ", row[4])
   print ("联系方式 = ", row[5])
   print ("备注 = ", row[6], "\n")

print ("Operation done successfully")

cur =c.execute("select * from customer where customerID=20180002 ")
print (cur)

for row in cur:
   print (row[0])
   print (row[1])
   print (row[2])
   print (row[3])
   print (row[4])
   print (row[5])
   print (row[6], "\n")


conn.close()