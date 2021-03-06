# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 8,7, 6, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set
# using Remove() method
set1.remove(5)	#remove(value)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)
#element is not there then remove method gives error

# Removing elements from Set
# using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set
# using iterator method
for i in range(1, 5):
	set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)
#########################################################################################

# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)

#########################################################################################

#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)


# Removing all the elements from
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)

