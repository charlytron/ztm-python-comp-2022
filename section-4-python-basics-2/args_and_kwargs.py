######################################################################
#                   Args and Kwargs                                  #
######################################################################

# *args and **kwargs are used to pass a variable number of arguments to a function.

def super_func_1(args):
  return sum(args)

def super_func_2(*args):
    print(*args) # prints the arguments passed to the function
    # print(args) # prints a tuple of the arguments passed to the function
    return sum(args) # can accept any number of positional arguments

    
def super_func_3(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


# super_func_1(1, 2, 3, 4, 5) 
# TypeError: super_func_1() 
# takes 1 positional argument but 5 were given

super_func_2(1, 2, 3, 4, 5) # 15
# We can extend the function to accept any number of positional arguments

print(super_func_3(1, 2, 3, 4, 5, num1=5, num2=10)) # 30

# Rule: params, *args, default parameters, **kwargs in that order

name = 'jose'
def super_func_4(name, *args, **kwargs): # 
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func_4(name, 1, 2, 3, 4, 5, i="Hi", num1=5, num2=10)) # 30
# usually we only use two of these in a function

