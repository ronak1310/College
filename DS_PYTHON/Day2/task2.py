lst=[33,21,45,56,22,44,32,18,51]
j=0
i=0
while i<len(lst):
    if lst[i]%2==0:
        lst[i],lst[j]=lst[j],lst[i]
        j+=1
    i+=1
print(lst)