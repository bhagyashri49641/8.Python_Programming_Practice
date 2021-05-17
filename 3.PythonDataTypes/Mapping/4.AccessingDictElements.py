# Python program to demonstrate
# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Bhagyashri', 'Middle_name': 'Bhalchandra', 3: 'Mane'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Middle_name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])




# accessing a element using get()
# method

# Creating a Dictionary
Dict = {1: 'Bhagyashri', 'Middle_name': 'Bhalchandra', 3: 'Mane'}

print("Accessing a element using get:")
print(Dict.get(3))


#accessing nested dict elements

# Creating a Dictionary
Dict = {'Dict1': {1: 'Hello'},
		'Dict2': {1: 'Bhagyashri', 'Middle_name': 'Bhalchandra', 3: 'Mane'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2'][3])

