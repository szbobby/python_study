import random 

print("Cidang大赌场开档了开档了,总共可以玩10次")

num = 1
ok = 0
while num < 11:
    print ("第",num,"次：")
    secret = random.randint(1,3)
    temp = input("现在开始猜我抽取的是哪个数字: ") 
    guess = int(temp)
    if guess != secret:
        print ("不对不对，我抽取的数字是：",secret)
    else:
        print("猜对了！难道你有预知能力？")
        ok=ok+1
    num = num +1

print ("游戏结束了，你总共猜对了",ok,"次")
print ("拜拜，记住哦，我是CiDang大排挡")

