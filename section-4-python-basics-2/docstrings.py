######################################################################
#                             Docstrings                             #
######################################################################



# Docstring allows us to comment inside a function and it is not executed
# Docstrings are used to document functions, classes, and modules.

def test(a):
    '''
    Info: This here function tests and prints parameter a.
    Isn't that special?
    '''
    print(a)

# help(test) # prints the docstring
print(test.__doc__)
