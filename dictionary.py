# indexing slicing cant be done 
# it is unordered
d ={} # empty dictionary
d = dict()# dictionary constructor

d = dict([('bangalore',30),('chenni',40)])
print(d)
d = dict(bangalore=30,chenni=35,delhi=30)
print(d)
d = dict({'bangalore':25,'chennai':35,"delhi":30})
print(d)

#key can oly be strinhg and tuple and not list dictionary so keys are immutable or hashable

#acessing the values from the dictionary
d ={'blore':30,'chennai':45,"delhi":21}
print(d['delhi'])

#print(d['goa']) --as it nt present it throw key erroe to avoid key error we can use get() method
print(d.get('goa','it is not found'))