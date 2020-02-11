import random 
secret = random.randint(1,10)

print("———-我爱鱼c工作室———-")

num = 1 
temp = input("不妨猜下小甲鱼心里想的是哪个数字: ") 
guess = int(temp) 
while guess != secret and num < 3: 
if guess > secret: 
print ("大了大了—") 
else: 
print ("小了小了—") 
temp = input("哎呀，猜错了,请重新输入吧: ") 
guess = int(temp) 
num = num + 1

if num >= 3 and guess != secret: 
print(“很遗憾，猜错次数太多哦!”) 
print(“正确结果: ” + str(secret)) 
if guess == secret: 
print(“恭喜你，猜中了！”) 
print(“哼，猜中也没有奖励！”) 
print(“游戏结束，不玩啦^_^”)
