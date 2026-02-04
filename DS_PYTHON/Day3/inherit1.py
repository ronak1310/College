class Person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def inputPer(self):
        self.name=input("Name:")
        self.age=int(input("Age:"))
    def show(self):
        print(self.name,self.age)
    def canVote(self):
        if self.age>=18:
            print("You can vote!")
        else:
            print("You can't vote")

class Student(Person):
    def __init__(self,roll=None,age=None,name=None,marks=None):
        super().__init__(name,age)
        self.roll=roll
        self.marks=marks
    def inputStu(self):
        super().inputPer()
        self.roll=input("Roll:")
        self.marks=input("Marks:")
    def show(self):
        super().show()
        print(self.roll,self.marks)
    

class Faculty(Person):
    def __init__(self,name=None,age=None,facid=None,salary=None):
        super().__init__(name,age)
        self.facid=facid
        self.salary=salary
    def inputFac(self):
        super().inputPer()
        self.facid=input("facid:")
        self.salary=input("salary:")      
    def show(self):
        super().show()
        print(self.facid,self.salary) 

    
ob1=Student()
ob1.inputStu()
ob1.show()
ob1.canVote()
ob2=Faculty()
ob2.inputFac()
ob2.show()
ob2.canVote()


    