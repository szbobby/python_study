import threading
def sayhello():
        print ("hello world")
        global t        #Notice: use global variable!
        t = threading.Timer(1.0, sayhello)
        t.start()

t = threading.Timer(1.0, sayhello)
t.start()
