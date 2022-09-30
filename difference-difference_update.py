a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b))
print(a-b)

a = {1,2,3}
b = {2}
a.difference_update(b)
print(a)