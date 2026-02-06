class Account:
    def __init__(self):
        self.act_no=None
        self.name=None
        self.mobile=None
        self.balance=None
        self.pin=None
    def input(self):
        self.act_no=input("\nAccount Number : ")
        self.name=input("\nName : ")
        self.mobile=input("\nMobile : ")
        self.balance=input("\nBalance : ")
        self.pin=input("\nPin : ")
    def show(self):
        print(f"\nName : {self.name} ({self.act_no})")
        print(f"Mobile : {self.mobile}")
    def toDict(self):
        return{
        "act_no":self.act_no,
        "name":self.name,
        "mobile":self.mobile,
        "balance":self.balance,
        "pin":self.pin         
        }