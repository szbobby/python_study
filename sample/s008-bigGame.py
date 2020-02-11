def area(width,height):
    return width*height




def print_welcome(name):
    print ("欢迎你的到来啊...",name)

name = input("请输入您的姓名：")

print_welcome(name)
print ("")

import random 

print("Cidang大赌场开档了开档了,总共可以玩10次")

num = 1
ok = 0

while num < 11:
    print ("第",num,"次：")
    secret = random.randint(1,3)
    guess = int(input("""总共有1，2,3三个数字，
现在开始猜我抽取的是哪个数字: """)) 
  
    if guess > 3 or guess < 0:
        print ("错了错了，我跟你说，要输入1或2或3才行的，你浪费一次机会了")
        print ("")
        
    elif guess != secret:
        print ("不对不对，我抽取的数字是：",secret)
        print ("")
        
    else:
        print("猜对了！难道你有预知能力？")
        print ("")
        ok=ok+1
    num = num +1

print ("游戏结束了，你总共猜对了",ok,"次")
print ("拜拜，记住哦，我是CiDang大排挡")

