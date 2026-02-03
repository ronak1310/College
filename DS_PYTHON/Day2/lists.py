#lst=[23,44,54,23,33]
# for x in lst:
#     print(x)
# print()
# i=0
# while(i<5):
#     print(lst[i])
#     i+=1

# print(len(lst))

#Operations or Functions in list:-
lst=[23,33,44,55,11]
print(lst)
lst.append(25)
print(lst)
lst.insert(2,22)
print(lst)
l2=[100,200,300]
lst.extend(l2)
print(lst)
lst.append(l2)
print(lst)
lst.pop(10)
print(lst)
lst.remove(55)
print(lst)
print(lst.index(23))
print(55 in lst)
print(lst.count(23))
lst.sort()
print(lst)
lst.reverse()
print(lst)