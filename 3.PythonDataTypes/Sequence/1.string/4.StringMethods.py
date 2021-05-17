####################  capitalize() ###########################
#Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

# output     Hello, and welcome to my world.

###################  casefold()  ############################
# Make the string lower case:

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

# hello, and welcome to my world!

#################################################### center() ##################################################
''' The center() method will center align the string, 
using a specified character (space is default) as the fill character.

Syntax       

string.center(length, character)
'''
txt = "banana"

x = txt.center(20, "O")

print(x)						#OOOOOOObananaOOOOOOO



################################################## count()  ##################################################
'''
The count() method returns the number of times a specified value appears in the string.

Syntax 

string.count(value, start, end)

value	Required.      A String. The string to value to search for
start	Optional.      An Integer. The position to start the search. Default is 0
end	    Optional.      An Integer. The position to end the search. Default is the end of the string
'''

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 0, 24)

print(x)				# 2

################################################ encode()   ###################################################

'''
The encode() method encodes the string, using the specified encoding. 
If no encoding is specified, UTF-8 will be used.

syntax

string.encode(encoding=encoding, errors=errors)

encoding			Optional. A String specifying the encoding to use. Default is UTF-8

errors				Optional. A String specifying the error method. Legal values are:

					'backslashreplace'	- uses a backslash instead of the character that could not be encoded
					'ignore'			- ignores the characters that cannot be encoded
					'namereplace'		- replaces the character with a text explaining the character
					'strict'			- Default, raises an error on failure
					'replace'			- replaces the character with a questionmark
					'xmlcharrefreplace'	- replaces the character with an xml character

'''

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

'''
OP

b'My name is St\\xe5le'
b'My name is Stle'
b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
b'My name is St?le'
b'My name is Ståle'
'''

############################################### endswith()  #####################################################
'''
 The endswith() method returns True if the string ends with the specified value, otherwise False.

 Syntax
 string.endswith(value, start, end)

value			Required. The value to check if the string ends with
start			Optional. An Integer specifying at which position to start the search
end				Optional. An Integer specifying at which position to end the search

'''
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)  # False

#############################################  expandtabs() #####################################################
'''
The expandtabs() method sets the tab size to the specified number of whitespaces.

Syntax

string.expandtabs(tabsize)


tabsize	Optional. A number specifying the tabsize. Default tabsize is 8

'''
txt = "H\te\tl\tl\to"

print(txt)  # default is 8 
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
print(txt.expandtabs(12))
​

'''
OP

H	e	l	l	o
H e l l o
H   e   l   l   o
H         e         l         l         o
H           e           l           l           o

'''
########################################## find()  ####################################################

'''
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, 
			the only difference is that the index() method raises an exception if the value is not found.
			 (See example below)

Syntax 

string.find(value, start, end)

value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end		Optional. Where to end the search. Default is to the end of the string
'''
txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x) #8



txt = "Hello, welcome to my world."

print(txt.find("q")) # -1
print(txt.index("q")) #ValueError: substring not found

############################################### format()   #########################################
'''
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The format() method returns the formatted string.
The placeholder is defined using curly brackets: {}. 

Syntax
string.format(value1, value2...)

value1, value2...	Required. One or more values that should be formatted and inserted in the string. The values can be A number specifying the position of the element you want to remove.

					The values are either a list of values separated by commas, a key=value list, or a combination of both.

					The values can be of any data type.

The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
'''
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1) #My name is John, I'm 36
print(txt2) #My name is John, I'm 36
print(txt3) #My name is John, I'm 36

######################################### index() #################################################
'''
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method,
the only difference is that the find() method returns -1 if the value is not found. (See example below)

Syntax
string.index(value, start, end)

value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	    Optional. Where to end the search. Default is to the end of the string

If the value is not found, the find() method returns -1, but the index() method will raise an exception:
'''
txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)  #8

######################################## isalnum() ###################################################

'''
The isalnum() method returns True if all the characters are alphanumeric,
 meaning alphabet letter (a-z) and numbers (0-9).

syntax

 string.isalnum()
'''

txt = "Company 12"

x = txt.isalnum()

print(x) # False

######################################### isalpha() ############################################
'''The isalpha() method returns True if all the characters are alphabet letters (a-z).

Example of characters that are not alphabet letters: (space)!#%&? etc.

Syntax
string.isalpha()
'''
txt = "Company10"

x = txt.isalpha()

print(x)# False

############################################
'''
The isdecimal() method returns True if all the characters are decimals (0-9).

This method is used on unicode objects.

Syntax
string.isdecimal()

'''
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal()) #True
print(b.isdecimal()) #False

#################################################

'''
The isdigit() method returns True if all the characters are digits, otherwise False.

Exponents, like ², are also considered to be a digit.

Syntax
string.isdigit()
'''

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit()) # True
print(b.isdigit()) #True

##################################################
'''
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

Syntax
string.isidentifier()
'''
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier()) # True
print(b.isidentifier()) #True
print(c.isidentifier()) #False
print(d.isidentifier()) #False

##############################################
'''
The islower() method returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

Syntax
string.islower()
'''
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower()) #False
print(b.islower()) #True
print(c.islower()) #False

####################################################
'''
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
syntax
string.isnumeric()
'''
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())#T
print(b.isnumeric())#T
print(c.isnumeric())#F
print(d.isnumeric())#F
print(e.isnumeric())#F
###########################################################
'''
The istitle() method returns True if all words in a text start with a upper case letter, 
AND the rest of the word are lower case letters, otherwise False.
Symbols and numbers are ignored.

syntax
string.istitle()
'''
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())#F
print(b.istitle())#T
print(c.istitle())#T
print(d.istitle())#T

######################################################
'''
The isupper() method returns True if all the characters are in upper case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

syntax
string.isupper()
'''
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())#F
print(b.isupper())#F
print(c.isupper())#T
##########################################################
'''
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.

syntax
string.join(iterable)

iterable	Required. Any iterable object where all the returned values are strings
'''
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x) #nameTESTcountry

###########################################################
# there are many more methods see w3school website for details








