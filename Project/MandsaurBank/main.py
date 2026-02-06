# from util import printMenu
import util as ob
while True:
    ob.printMenu()
    choice=int(input(">> "))
    if choice==6:
        break
    elif choice==1:
        ob.create()
    elif choice==2:
        ob.checkBalance()
    elif choice==3:
        ob.printBook()
    elif choice==4:
        ob.withdraw()
    elif choice==5:
        ob.deposit()
    else:
        print("\n\tInvalid Choice!!")
print("\n** Thank you Guyss!! **")   