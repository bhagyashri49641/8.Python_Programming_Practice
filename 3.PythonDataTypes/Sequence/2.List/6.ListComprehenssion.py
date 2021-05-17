"""
List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.

A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

Syntax:

newList = [ expression(element) for element in old List if condition ]


"""

# Python program to demonstrate list comprehension in Python	
# below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print (odd_square)

"""
output

[1, 9, 25, 49, 81]

"""



list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
list2=[x*2 for x in list1 if x%2==0]
print(list2)

"""
output
[4, 8, 12, 16, 20, 24, 28, 32]

"""

