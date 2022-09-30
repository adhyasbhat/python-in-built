# the list has to be homogeneous inorder to sort
# ascending order
l = [1,6,25,2,62,85]
l.sort()
print(l)
#decending order
l.sort(reverse=True)
print(l)

# ascending according to length
l =['hi','hello','bye','baby']
l.sort(key=len)
print(l)

# decending according to length
l.sort(key=len,reverse=True)
print(l)