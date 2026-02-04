class ABC:
    def fun1(self):
        print("ABC'S FUN1")

class XYZ(ABC):
    def hello(self):
        print("XYZ'S HELLO")

ob=XYZ()
ob.fun1()#inherited function
ob.hello()#self function
#super 