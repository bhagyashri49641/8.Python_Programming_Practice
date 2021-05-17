# Creating a Dictionary
# with Integer Keys

d = {1:'Shree', 2:'Mane', 3:'Nayan', 4:'Mane'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[3])    
  
print (d.keys())    
print (d.values())    


"""
OUTPUT
1st name is Shree
2nd name is Nayan
dict_keys([1, 2, 3, 4])
dict_values(['Shree', 'Mane', 'Nayan', 'Mane'])

"""


# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Shree', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

"""
Dictionary with the use of Mixed Keys: 
{1: [1, 2, 3, 4], 'Name': 'Geeks'}
"""


# Creating an empty Dictionary
Dict = {}
print("\nEmpty Dictionary: ")
print(Dict)



# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Welcome', 2: 'to', 3:'Python'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Bhagyashri'), (2, 'Mane')])




print("\nDictionary with each item as a pair: ")
print(Dict)

