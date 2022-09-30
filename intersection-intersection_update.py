#intersection
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b)) # the original set a will not get updated
#intersection_update
a = {1,2,3,4}
b = {3,4,5,6}
a.intersection_update(b) # the original set a will get updated
print(a)