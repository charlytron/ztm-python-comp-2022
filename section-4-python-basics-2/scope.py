######################################################################
#                            Scope                                   #
######################################################################

# Scope is the area in which a variable is visible and accessible
# There are two types of scope: local and global

# print(name()) # NameError: name 'name' is not defined

# Scope in Python is determined by the location of the variable assignment

# Global scope
# total = 100 # Global variable

# When Python has functional scope, it looks for the variable in the local scope

def some_func():
    total = 50 # Local variable
    
print(total) # NameError: name 'total' is not defined, because total is not defined in the global scope

# Think of scope as a new world where the variable is defined


