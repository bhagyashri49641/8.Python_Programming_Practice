
###############################  Looping throgh strings ########################################
for x in "Bhagyashri":
	print(x)

	'''
	output 
	B
	h
	a
	g
	y
	a
	s
	h
	r
	i
	'''

#################################string length len() function ################################

a = "Hello, World!"
print(len(a))					# Output 13

################################### Check string ##############################################

txt = "The best things in life are free!"
print("free" in txt)			#output  True


# we can also use in keyword in if statment
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#output  Yes, 'free' is present

################################# check if not #####################################
txt = "The best things in life are free!"
print("expensive" not in txt)

# output True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

#output   Yes, 'expensive' is NOT present

########################################## Operators  ##################################
str = "Hello"     
str1 = " world"    
print(str*3) 			# prints HelloHelloHello    # * multiply
print(str+str1)		# prints Hello world	     # + Add String
print(str[4]) 			# prints o                  #slice operator
print(str[2:4]); 		# prints ll                 #slice particular part of string
print('w' in str) 		# prints false as w is not present in str    # 'in' is  membership operator
print('wo' not in str1) 	# prints false as wo is present in str1.     # 'not in' is membership operator
print(r'C://python37') 	# prints C://python37 as it is written       #  raw operator
print("The string str : %s"%(str)) # prints The string str : Hello          #formatting operator

'''
 Output
HelloHelloHello
Hello world
o
ll
False
False
C://python37
The string str : Hello
 
 '''


########################################### Escape sequence ##############################

# using triple quotes  
print('''They said, "What's there?"  ''')  
  
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  


'''
OUTPUT
They said, "What's there?"
They said, "What's going on?"
They said, "What's going on?"
'''

print("C:\\Users\\DEVANSH SHARMA\\Python32\\Lib")  
print("This is the \n multiline quotes")  
print("This is \x48\x45\x58 representation")  
print(r"C:\\Users\\DEVANSH SHARMA\\Python32")  

'''
Output
#C:\\Users\\DEVANSH SHARMA\\Python32\\Lib
This is the 
 multiline quotes
This is HEX representation
C:\\Users\\DEVANSH SHARMA\\Python32
'''

##################################### format() ##########################################
# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
  
#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  
  
#Keyword Argument  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  

'''
output
Devansh and Abhishek both are the best friend
Rohit and Virat best players 
James,Peter,Ricky 
'''
age = 26
txt = "My name is Shree, and I am {}"
print(txt.format(age))

'''
output
My name is Shree, and I am 26
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
'''
output
I want to pay 49.95 dollars for 3 pieces of item 567
'''
############################### using % operator ########################################
Integer = 10;    
Float = 1.290    
String = "Devansh"    
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String)) 

'''
output
Hi I am Integer ... My value is 10
Hi I am float ... My value is 1.290000
Hi I am string ... My value is Devansh

'''
