# Python program to demonstrate Creation of Set in Python

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with the use of a String
set1 = set("Bhagyashri")
print("\nSet with the use of String: ")
print(set1)


# Creating a Set with the use of Constructor
# (Using object to Store String)
String = 'Hardwork is the key'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)


# Creating a Set with the use of a List
set1 = set(["Bhagya", "Shree", "shree"])
print("\nSet with the use of List: ") # shree ekdach print hoil karan set duplicate allow krt nahi
print(set1)


# Creating a Set with a List of Numbers(Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)


# Creating a Set with a mixed type of values (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)


