class Subject:
    def __init__(self,sname,sid):
        self.sname=sname
        self.sid=sid
    def show(self):
        print(f"Subject Name : {self.sname} - Subject ID : {self.sid}")

class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def show(self):
        print("\nRoll : ",self.roll)
        print("Name : ",self.name)

class Lecture:
    def __init__(self):
        self.title=None
        self.fname=None
        self.sub=None
        self.time=None
        self.students=None
    def addStudent(self,student):
        self.students.append(student)
    def removeStudent(self,roll):
        pass