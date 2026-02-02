# print("Starting...")
# x=1;#start
# while x<=10:#condition
#     print(x)
#     x+=1#steps
# print("Ending...")

size=int(input("How many numbers "))
total=0
i=1
while i<=size:
    x=int(input("Enter number:"))
    total+=x;
    i+=1
print(f"Sum of {size} numbers = {total}")
# print(f"Average of {size} numbers = {total//size}")
print(f"Average of {size} numbers = {total/size}")
