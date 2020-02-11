import os ## for os.path.isfile()

def dealline(line) :
    print(line) ## 针对line我可以做很多事情

def getfilename() :
    return input('请输入文件名称(输入 exit() 退出):').strip()

while True :
    try :
        filename = getfilename()

        if filename.lower() == 'exit()' : ## 退出
            break

        if os.path.isfile(filename) : ## 判断文件是否存在

            f = open(filename)
            try :
                lines = f.readlines()

                for line in lines:
                    dealline(line)
            
                ## input()
            finally :
                f.close()

        else :
            print('File does not exist.')
            ##input()
    except :
        print('Input Error!')
