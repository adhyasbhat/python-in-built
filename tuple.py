#it is heterogeneous n its represented in ()
# it is more memory efficient compared to list
t = (1,2,3,4,5)
print(t)

#nested tuple
t = (1,2,3,[5,6,7,8],(12,12,32))
print(t)

# single item in tuple
t = (1)
print(t)

# count
t = (1,2,3,4,2,4,2)
print(t.count(2))

# index
t = (1,3,2,5,6)
print(t.index(2))

# adding and deleting is not performed in tuple