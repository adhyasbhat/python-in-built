from audioop import reverse
from unicodedata import name


names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']
names.append(['netfix','walmart','kroger'])
print(names)
names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']
names.extend(['netfix','walmart','kroger'])
print(names)

#descending order
names.sort(reverse=True)
print(names)

#ascending order of length
names.sort(key=len)
print(names)

#decending order of length
names.sort(key=len,reverse=True)
print(names)

#string to list
string = "hi welcome to python"
print(string.split())
print(list(string))