# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Shree',
		'A' : {1 : 'Shree', 2 : 'Nayan', 3 : 'Sangita'},
		'B' : {1 : 'anks', 2 : 'ash'}}
print("Initial Dictionary: ")
print(Dict)

##################################################################################
# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

#################################################################################
# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

#################################################################################
#using pop() method
# Creating a Dictionary
Dict = {1: 'Hello', 'name': 'Hi', 3: 'Bye bye'}
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

################################################################################
#using popitem() method			randomly kontipn pair delete hou shkte
# Creating Dictionary
Dict = {1: 'Hello', 'name': 'Hi', 3: 'Bye bye'}

# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

##############################################################################
#Using clear() method
# Creating a Dictionary
Dict = {1: 'Hello', 'name': 'Hi', 3: 'Bye bye'}
# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)

