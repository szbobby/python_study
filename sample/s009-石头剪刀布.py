import random 


listA = ['你现在看起来很精神哦，有什么喜事？','你现在看起来很神经哦，有什么哀事？','你好漂亮哦','你整个人看起来像是一个快乐的精神病人，不错不错','你看起来有点傻']
wel = random.randint(0,4)

def print_welcome(name):
    print ("欢迎你的到来啊...",name)
    print (listA[wel])

name = input("请输入您的姓名：")

print_welcome(name)
print ("")


print("Cidang大赌场开档了开档了,总共可以玩10次")

list = ['','石头','剪刀','布']

num = 1
ok = 0

while num < 11:
    print ("第",num,"次：")
    secret = random.randint(1,3)
    guess = int(input("""【石头-剪刀-布】游戏现在开始，不许作弊，我们一起出啊，
你选择出哪个？1、石头，2、剪刀，3、布 ："""))
    print ("")  
   
    if guess > 3 or guess == 0 :
        print ("错了错了，我跟你说，要输入1或2或3才行的，哎呀，浪费一次机会了")
        print ("")

    elif guess < secret or (guess ==3 and secret==1):
        print ("你出的是：",guess,list[guess],"我出的是：",secret,list[secret])
        print ("你赢了！！！")
        print ("")
        ok = ok+1

    elif guess > secret  or (guess ==1 and secret==3):
        print ("你出的是：",guess,list[guess],"我出的是：",secret,list[secret])
        print ("你输了...")
        print ("")

    elif guess == secret:
        print ("你出的是：",guess,list[guess],"我出的是：",secret,list[secret])
        print ("大家打平手哦，一团和气嘛！")
        print ("")

    num = num +1

print ("游戏结束了，你总共赢了",ok,"次")

print ("拜拜，记住哦，我是CiDang大排挡")

