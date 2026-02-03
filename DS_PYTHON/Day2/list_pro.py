lst=[23,33,44,55,11,55,33,22,11,55,66,23,33,44,55]
user=int(input("Enter value to be popped out "))
n=lst.count(user)
print(f"value occured : {n} times")
i=0
while i<n:
    lst.remove(user)
    i+=1
print(lst)