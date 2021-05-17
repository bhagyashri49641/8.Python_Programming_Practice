x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

"""
OUTPUT:

b'Hello'
<class 'bytes'>
"""

###################################################################################
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x))
 
"""
OUTPUT:

bytearray(b'\x00\x00\x00\x00\x00')
<class 'bytearray'>
"""

####################################################################################

x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

"""
OUTPUT:
<memory at 0x7f4b7aaac340>
<class 'memoryview'>


"""
