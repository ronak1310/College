# lst=[2,3,4,4,4,5,2,1,3,4,4,6,7,2,4,1,4,2,3,3]
# x=4
# i=0
# while(i<len(lst)-1):
#     j=i+1
#     if(lst[i]==lst[j] and lst[i]==x):
#         lst.pop(j)
#         lst.pop(i)
#     elif(lst[i]==x):
#         lst.pop(i)
#     else:
#         i+=1
# print(lst)

lst=[2,3,4,4,4,5,2,1,3,4,4,6,7,2,4,1,4,2,3,3]
i=0
while i<len(lst)-1:
    if(lst[i]==4 and lst[i+1]==4):
        while lst[i]==4 and lst[i+1]==4:
            lst.pop(i)
        lst.pop(i)
    else:
        i+=1
print(lst) 