# n=int(input("Number "))
# cnt=True
# i=2
# while(i<n):
#     if(n%i==0):
#         print("Not prime")
#         cnt=False
#         break
#     i+=1
# if(cnt):
#     print("prime")
        
# n=int(input("Number "))
# i=2
# while(i<n):
#     if(n%i==0):
#         print("Not prime")
#         break
#     i+=1
# if i==n:
#     print("prime")
   
n=int(input("Number "))
i=2
while(i<n//2):
    if(n%i==0):
        print("Not prime")
        break
    i+=1
else:
    print("Prime")