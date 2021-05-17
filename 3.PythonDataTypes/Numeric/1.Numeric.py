import sys


a = None
print(a)
print(type(a))				#Nonetype
print(sys.getsizeof(a))


a = 11
print(a)
print(type(a))			#<class 'int'>
print(sys.getsizeof(a))


a = 11.45
y = 12E4
z = -87.7e100
print(a)
print(y)
print(z)
print(type(a))				#<class 'float'>
print(sys.getsizeof(a))


a=5
b=6
no=complex(a,b)
print(no)
print(type(no))			#<class 'Complex'>
print(sys.getsizeof(no))


import random

print(random.randrange(1, 10))
