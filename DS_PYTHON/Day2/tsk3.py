lst=[2,3,4,4,4,5,2,1,3,4,4,6,7,2,4,1,4,2,3,3]
temp=[]
x=4
i=1
for i in range(len(lst)):
    if lst[i]==lst[i-1]==x:
        temp.append(i-1)
j=0
for j in range(len(temp)):
    lst.remove(lst[temp[j]])
    
print(lst)