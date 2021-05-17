#Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print (Tuple1)

#Creatting a Tuple with the use of string
Tuple1 = ('Shree', 'hi')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

#Creating a Tuple with the use of built-in function
Tuple1 = tuple('Shree')
print("\nTuple with the use of function: ")
print(Tuple1)


###################################################################################
"""
Creating a Tuple with Mixed Datatypes.
Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.).

 Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.
"""

#Creating a Tuple
#with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Shree')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

#Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'Welcome')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#Creating a Tuple
#with repetition
Tuple1 = ('Shree',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

#Creating a Tuple
#with the use of loop
Tuple1 = ('Shree')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
	Tuple1 = (Tuple1,)
	print(Tuple1)
"""
OUTPUT:

Initial empty Tuple: 
()

Tuple with the use of String: 
('Shree', 'hi')

Tuple using List: 
(1, 2, 4, 5, 6)

Tuple with the use of function: 
('S', 'h', 'r', 'e', 'e')

Tuple with Mixed Datatypes: 
(5, 'Welcome', 7, 'Shree')

Tuple with nested tuples: 
((0, 1, 2, 3), ('python', 'Welcome'))

Tuple with repetition: 
('Shree', 'Shree', 'Shree')

Tuple with a loop
('Shree',)
(('Shree',),)
((('Shree',),),)
(((('Shree',),),),)
((((('Shree',),),),),)


"""
