from copy import deepcopy
# id copies the memory address
from copy import deepcopy


l = [1,2,3,4]
l2 = l
print(id(l), id(l2))

# using copy() function
l1 = [1,4,2,5]
l3 = l1.copy # it doesnt copy memeory address
print(l1,l3)
print(id(l3),id(l1))


p1 = [1,2,3,4,[5,6,7]]
p2 = p1.copy()
print(p1,p2)
print(id(p1),id(p2))
print(id(p1[3]),id(p2[3]))
p1.append(8)
print(p1,p2)
print("-------------------------")
# shallow copy - during the nested list the copy memory address is not copied so deep copy is used

p2 = deepcopy(p1)
print(id(p1),id(p2))
print(id(p1[3]),id(p2[3]))