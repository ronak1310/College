from models.account import Account
import FileOperation as fp
accounts=fp.getAllAccounts()
print(accounts)
def printMenu():
    print("\n***Mandsaur Bank Options \n")
    print("1.Create Account")
    print("2.Balance Check")
    print("3.Passbook Print")
    print("4.Withdraw")
    print("5.Deposit")
    print("6.Exit")

def checkAccount():
    actNo=input("\nAccount Number : ")
    pin=input("Pin Number : ")
    for act in accounts:
        if actNo == act['act_no'] and pin == act['pin']:
            return act
def create():
    act=Account()
    act.input()
    accounts.insert(0,act.toDict())
    fp.saveAccount(accounts)
    
def checkBalance():
    actNo=checkAccount()
    if actNo is not None:
        pass
def printBook():
    pass
def withdraw():
    pass
def deposit():
    pass