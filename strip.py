# removes the charater mentioned inside the function the default charater is space
s = "  hi adhya how are you   "
print(s.strip())
print(s.rstrip())
print(s.lstrip())
print("---------------")
a = "@@adhya hi@@ h@ow@@"
print(a.strip('@'))
print(a.rstrip('@'))
print(a.lstrip('@'))
print("---------------")
b = "******************** hello ##########################"
print(b.lstrip('*'))
print(b.rstrip('#'))
print(b.strip('*#'))