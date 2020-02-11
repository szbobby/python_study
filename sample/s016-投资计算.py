def invest():
    amount = int(input("请输入您的资金量："))
    #rate = int(input("请输入每年的预期回报率：")
    rate = 0.05

    time = int(input("请输入您计划投资多少年："))
    result = amount
    i=1
    print ("principal amount:"+str(amount))
    while i <= time:
        result = result*(1+rate)
        print ("year {}:".format(i)+str(result))
        i = i+1
    print ("done")

invest()




             
             

                 
                 
