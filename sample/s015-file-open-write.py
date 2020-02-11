i = 0
while i < 10:
    file = open('f:/temp/{}.txt','a'.format(i)) #在f盘temp目录下建立3个文件，可以是文本也可以是其他后缀格式
    file.write('this is the {} file\n'.format(i)) #加\n，换行
    print ('ok {}'.format(i))
    file.close()
    i = i+1
print ("done")





                
