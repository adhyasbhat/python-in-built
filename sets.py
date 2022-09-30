s = {}
print(s) # this creats a emply dictionary n not set

_set = set() # set() is a constructor
print(_set)

# hash value
l = [1,2,3,4]
t = (1,2,3,5)
print(dir(t))
print(hash(t))
print(hash(l)) # list cant have hash value
# slice index cant be done in set as it is unordered