a = 0

for n in range(2,10):
    x = int(input("一起来玩猜数游戏吧，猜一猜我现在心里面正在想的是哪个数字？请输入 0—9之间的任意一个数字："))
    if x == 5:
        print('猜对了，你真是我肚子里面的蛔虫？谢谢你的参与哦')
    elif x > 7:
        print('大了大了，数字没这么大')
    elif x < 3:
        print('小了小了，数字没这么小')
    else:
        print('不对不对，非常接近了')
      
else:
    print("游戏结束")
