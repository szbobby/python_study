
import random

i=1

while i < 11:
    print ("赌大小，请押注：大或小")
    bet = int(input("1-大；2-小:"))
    print ('开')
    point1 = random.randrange( 1, 7)
    point2 = random.randrange( 1, 7)
    point3 = random.randrange( 1, 7)
    result = point1+point2+point3

    if 11 <= result <=18:
        print (str(point1)+","+str(point2)+","+str(point3)+","+str(result)+"点大")
        if bet==1: print("你赢了")
        else: print ("你输了")

    elif 3<=result<=10:
        print (str(point1)+","+str(point2)+","+str(point3)+","+str(result)+"点，小")
        if bet==2: print("你赢了")
        else: print ("你输了")
    i=i+1

print ("游戏结束！")




