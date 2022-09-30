#pop removes the specified from the dictionary 
d = {"name":"ram","age":30}
d.pop('age')
print(d)
d = {"name":"ram","age":30}
d.pop('phone','key not found')
print(d)
# popitem removes the last key insteted in dictionary
d = {"name":"ram","age":30}
print(d.popitem())
#delete the last element
l={1,2,3}
l1={5,6,7}
print(l+l1)