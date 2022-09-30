x = {1,2,3,}
a = {1,2,3,4,20}
# superset
print(a.issuperset(x))
print(x.issuperset(a))
print("-------------------")
# subset
print(a.issubset(x))
print(x.issubset(a))
print("-------------------")
#disjoint
x1= {1,2,3}
x2 = {2,4,6}
x3 = {2,3,4}
print(x1.isdisjoint(x2))
print(x1.isdisjoint(x3))