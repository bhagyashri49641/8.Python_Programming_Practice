# Python program to demonstrate Removal of elements in a List

# Creating a List
List = ['B','H','A','G','Y','A','S','H','R','I','M','A','N','E']
print("Intial List: ")
print(List)

# Print elements of a range using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

##############################################################################################
# Negative index slicing

#Creating a List
List = ['B','H','A','G','Y','A','S','H','R','I','M','A','N','E']
print("Initial List:")
print(List)

# Print elements from beginning to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

