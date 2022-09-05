################################################################
#                         Scope Rules                          #
################################################################

# What is the output of this code?

a = 1 # Global scope

def confusion():
    a = 5 # Local scope
    return a

print(a) # 1
print(confusion()) # 5

# What if we change the order of the print statements?

a = 1 # Global scope

def confusion():
    a = 5 # Local scope
    return a


print(confusion()) # 5
print(a) # 1

# Rules of scope
# 1. Start with local. If nothing there, check...
# 2. Parent local? If nothing there, check global

def parent():
    a = 10 # Parent local
    def confusion():
        return a
    return confusion()

print(parent()) # 10
print(a) # 

# 3. Global
# 4. Built in Python functions

def parent():
    a = 10 # Parent local
    def confusion():
        return sum
    return confusion()

print(parent()) # 10
print(a) # 
