############################################################
#                  Type Conversion                         #
############################################################

# Type conversion is the process of converting one type of 
# data to another type of data.

print(str(100)) # => '100' printed as 100

# is the result an integer or a string?

print(type(str(100))) # => <class 'str'>

print(type(100)) # => <class 'int'>

print(type(int(str(100)))) # => <class 'int'>

# Same as saying:

a = str(100)
b = int(a)
c = type(b)
 
print(c) # => <class 'int'>

# Just a little less verbose

