import time  # 引入时间模块

print(time.strftime("%Y-%m-%d %I:%M:%S"))  # 打印当前日期与时间，格式：年-月-日 时:分:秒

def logit():
    f = open('f:/log.txt', 'r+')  # 打开f盘temp目录下的log文件，可以是txt也可以是其他后缀格式
    count = f.readline()
    f.seek(0,0) #将指针定位到第1行第1个位置
    countA= int(count)+1  #读出来的数字是字符串，转为int并加1
    f.write(str(countA)) #将+1后的数字覆盖原来的第一行数字
    f.seek(0, 2) #将指针定位到文件的最后
    f.write(time.strftime("%Y-%m-%d %I:%M:%S")) #写入当前时间，不回行
    f.write("这是第{}次写Log文件\n".format(countA))  #\n 回行

    f.close()


def co():
    f = open('f:/log.txt', 'r+')  # 打开f盘temp目录下的log文件，可以是txt也可以是其他后缀格式
    data = f.readlines()
    coo = data [0] #获取Log文件的第一行
    return coo
    f.close()

def do():
    f = open('f:/log.txt', 'r+')  # 打开f盘temp目录下的log文件，可以是txt也可以是其他后缀格式
    data = f.readlines()
    doo=data[-1] #获取Log文件的最后一行
    return doo
    f.close()


