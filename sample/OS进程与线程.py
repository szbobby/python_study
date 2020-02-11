import os

# 用os模块的system函数来执行命令dir，执行完毕后如果返回值为0则表示执行成功。执行完毕后控制权返回给python进程。
print(os.system("dir"))

# 打开window系统的notpad程序，然后python自身进程被关闭，新建立的notpad进程继续
notepad = "c:\\windows\\notepad.exe"
os.execl(notepad,"notepad.exe")





