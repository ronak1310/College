import os

base = os.path.dirname(__file__)
path = os.path.join(base, "data.txt")
 
with open(path,mode= "w") as f1:
    f1.write("Hello,")

with open(path,mode= "r") as f1:
    data=f1.read()
    print(data)
    
with open(path,mode= "a") as f1:
    f1.write(" Mandsaur University")
    
with open(path,mode= "r") as f1:
    data=f1.read()
    print(data)
    