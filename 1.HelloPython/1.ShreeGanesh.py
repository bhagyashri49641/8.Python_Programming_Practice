#print function in python
# syntax  
# print(*objects,sep='',end='\n',file=sys.stdout,flush=false)


print("Shree Ganesh!!!")  
  
a = 10  
# Two objects are passed in print() function  
print("a =", a)  

  
b = a  
# Three objects are passed in print function  
print('a =', a, '= b') 

#using sep and end arguments

print("a =", a, sep='dddd', end='\n')  

print("a =", a, sep='__', end='$$$$$\n')

"""output
Welcome to javaTpoint.
a = 10
a = 10 = b
a =dddd10
a =__10$$$$$
"""