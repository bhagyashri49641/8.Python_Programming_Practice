# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)
# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)


# Adding elements to the List using Iterator
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)


# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)


# Addition of List to a List
List2 = ['For', 'Shree']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)


###################################################################################
#using insert method

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at specific Position (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Shree')
print("\nList after performing Insert Operation: ")
print(List)

##################################################################################
"""
this method is used to add multiple elements at the same time at the end of the list.
"""
	
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of multiple elements to the List at the end (using Extend Method)
List.extend([8, 'Shree', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)

"""output

Initial List: 
[1, 2, 3, 4]

List after performing Extend Operation: 
[1, 2, 3, 4, 8, 'Shree', 'Always']

"""
###################################################################################

