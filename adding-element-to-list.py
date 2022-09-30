# append element in list (it will only take one argument)
names = ['adhya','aarabhi','aarini','abhinav']
names.append("ankitha")
print(names)
names.append(1)
print(names)

print("----------------------------------------")

digits = [1,2,3,4]
digits.append(["cat"])
print(digits)

print("----------------------------------------")

# nested list
names.append(["arpitha","aproova"])
print(names)

print("----------------------------------------")

# extend element to list (it will take multiple elements/arguments)
name1 = ['bhavya','bhookima']
name1.extend(["bhavana","bindu"])
print(name1)

print("----------------------------------------")

numb = [1,2,3]
numb.extend(['run'])
print(numb)
numb.extend('run')
print(numb)

print("----------------------------------------")

#insert element to list (insert in the element in perticular position) 
num = [3,5,1,65,21,64]
num.insert(2,7)
print(num)

print("----------------------------------------")

num.insert(21) #this will throw an error as insert() expects 2 argument & we are just passing only one argument
print(num)