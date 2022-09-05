######################################################################
#                       Global Keyword                              #
######################################################################

# The global keyword allows us to modify a global variable inside a function

a = 10 # Global variable
def confusion(b):
    print(b) # 
    a = 90 # Local variable

confusion(300) 

# "b" the parameter is a local variable.
# parameters are local variables
# When we define the function, we let the interpreter know that we are going to 
# use the local variable "b"

# Is there a way for us to use the global variable "a" inside the function?
# Yes, we can use the global keyword

total = 0

def count():
    global total # global keyword
    total += 1
    return total

count()
count()
print(count()) # 3

# a better way to do this is dependency injection

total = 0

def count(total):
    total += 1
    return total

count(total)
count(total)
print(count(count(count(total)))) # 3

# We're able to detach the effect that the count function has on the global scope.