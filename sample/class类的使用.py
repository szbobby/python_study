class Fruit:
    def __init__( self):
        print(" initialize Fruit")

    def grow( self): # 定义grow() 方法06
        print ("grow ...")

class Vegetable( object):
    def __init__( self):
        print(" initialize Vegetable")
    def plant( self): # 定义plant 方法13
        print("plant ...")

class Watermelon(Vegetable, Fruit): # 多重继承，同时继承Vegetable 和Fruit 16
    pass #


if __name__ == "__main__":
    w = Watermelon() # 多重继承的子类，拥有父类的一切公有属性；本语句执行时即运行Vergetable中的__init__，不再执行Fruit中的__init__
    w.grow()
    w.plant()