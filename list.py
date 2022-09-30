l1 = [1,4,24,32,3,6]
l2 = [3,62,5,12,64]

#merging of list
print(l1+l2)
print(*l1,*l2)

#slicing of list
print(l1[:3:1])

# reverse of list
name = ['adhya','aarabhi','aarini','abhinav']
print(name[::-1])

# slice problems 
name1 = ['microsoft','insta','facebook','amazon','yahoo','google','apple']
print(name1[::-1])
print(name1[2][3])
print(name1[-2:3])
print(name1[-2:3:-1])
print(name1[-6:5])
print(name1[-1:2:-1])
print(name1[1+3])

# replacing the element in the origing list
name1[:2]=["unknown","unknown"]
print(name1)
