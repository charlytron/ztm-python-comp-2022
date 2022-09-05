################################################################
#                        Nonlocal Keyword                      #
################################################################

# The nonlocal keyword is used to refer to the parent scope from inside a nested function.
# It's a way for us to use a variable that is not a global variable, but is not a local variable either.

def outer():
    x = "local"

    def inner():
        nonlocal x # nonlocal keyword
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer() # returns 'inner: nonlocal outer: nonlocal'

# Key takeaway: We've modifed the outer scope from inside the inner function, with the nonlocal keyword.