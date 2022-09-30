# pop a element from the lsit
l = [1,2,3,4,5,6]
l.pop() # by default it removes the last element
print(l)
l.pop(3) # here 3 is the postion so 4 will be deleted from the lsit
print(l)
# l.pop(8)
# print(l) #if position is not present the it will throw index error

print("-------------------------------")

# remove the 1st occurance of element in the list
l1 = ['a','g','d','g','f','c','a']
l1.remove('g')
print(l1)
# l1.remove('e')
# print(l1) # as e is not present in the list it will thow value arror

print("-------------------------------")

#clear the elements in the list without deleting the list
l2 = [1,2,3,45]
l2.clear()
print(l2)

print("-------------------------------")

#deleting perticular position element in the list 
l4 = [1,2,3,4]
del l4[2]
print(l4)

print("-------------------------------")

# deleting the compelet list
l3 = [1,2,3,4,5]
del l3
print(l3)