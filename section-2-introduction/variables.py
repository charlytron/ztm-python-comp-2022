iq = 190
# We're binding the variable iq to the value 190
# When we request the value of iq,
# it will return the value 190
# The computer will look for the value of iq in memory


########################################################
#               Naming Conventions                     #
######################################################## 

# snake_case      
# Must start with lowercase letter or underscore
# Can contain letters, numbers, or underscores
# No spaces
# case sensitive
# don't overwrite keywords

user_iq = 190
_user_iq = 190 # private variable
_user_IQ = 190 # case sensitive

print(iq)
print(user_iq)
print(_user_iq)
print(_user_IQ)

print(bin(iq))

# print = 190 print is not callable
# Keywords are highlighted in yellow in this IDE
# Variables are highlighted in blue in this IDE

########################################################
#               Constants                              #
########################################################

# Constants are variables that cannot be changed
# Constants are always in uppercase
# Are meant to be immutable

PI = 3.14

########################################################
#                 Dunders                              #
########################################################

# Dunders are used to mark private variables

__file__
__name__
__doc__
__package__
__loader__
__spec__

# These are meant to be left alone

########################################################

a,b,c = 1,2,3

print(a,b,c) # 1 2 3

