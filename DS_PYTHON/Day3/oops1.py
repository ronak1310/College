class Employee:
    def __init__(self,name=None,age=None,mobile=None,salary=None,city=None):
        self.name=name
        self.age=age
        self.mobile=mobile
        self.salary=salary
        self.city=city
    def inputEmp(self):
        self.name=input("Name: ")
        self.age=input("Age: ")
        self.mobile=input("Mobile: ")
        self.salary=float(input("Salary: "))
        self.city=input("City: ")
    def show(self):
        print("\nName : ",self.name)
        print("Age : ",self.age)
        print("Mobile : ",self.mobile)
        print("Salary : ",self.salary)
        print("City: ",self.city)
# emps=[]
# size=int(input("How many employees: "))
# for i in range(size):
#     e=Employee()
#     e.inputEmp()
#     emps.append(e)
# for e in emps:
#     e.show()

emps=[
    Employee("Vikas",25,"9876543210",25500,"indore"),
    Employee("Gopal",22,"8786756758",16500,"ujjain"),
    Employee("Menna",24,"2343565754",11000,"indore"),
    Employee("Lokesh",21,"6754867584",28900,"indore"),
    Employee("Rajesh",29,"0987654321",24500,"ujjain")
]
# for e in emps:
#     if e.city=="indore" and e.salary>25000:
#         e.show()
e2=list(filter(emps,lambda e:e.salary>25000 and e.city=="indore"))