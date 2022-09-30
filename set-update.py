#update - it will get updated in original set so give print(a) seperately
a = {1,2,3,4}
b = {3,4,5,6}
a.update(b)
print(a)
b.update(a)
print(b)