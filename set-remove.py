a = {1,2,3,4,"hi"}
a.remove(3)
print(a)
# a.remove(5) # it gives key error as 5 is not present and not value erroe
# print(a)

#discard
a.discard("hi")
print(a)
a.discard("hello") # even though hello is not present it doesnt show any error
print(a)

#pop
a.pop() # any random element will be removed
print(a)
#it will throe key error if it is empty element

#clear
a.clear()
print(a)