lst1=[1,2,3,4,5,6,7]
# lst2=[]
# for i in lst1:
#     if(i%2==0):
#         lst2.append(i)
# print(lst2)

# def check(num):
#     return num%2==0

# ft=filter(check,lst1)
# lst2=list(ft)

# print(lst1)
# print(lst2)

lst2=list(filter(lambda x:x%2==0,lst1))
print(lst1)
print(lst2)

#for modification, map is used
lst2=list(map(lambda x:x*10,lst1))
print(lst1)
print(lst2)

lst2=list(filter(lambda x:x>50,map(lambda x:x*10,lst1)))
print(lst1)
print(lst2)