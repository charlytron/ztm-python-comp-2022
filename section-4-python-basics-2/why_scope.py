######################################################################
#                          Why Scope Matters                         #
######################################################################

# Why can't everything have access to everything else?

# It would be easier if we could just access everything from everywhere.
# But that would be a security nightmare.

# Machines have limited resources. We have to be careful about how we use them.
# Sometimes we have to share resources, but we have to be careful about how we do that.

def outer():
    x = "local"

    def inner():
        nonlocal x # nonlocal keyword
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer() # returns 'inner: nonlocal outer: nonlocal'

# When this function is run, we're creating one location in memory for the variable x.
# when we use nonlocal, we're saying that we want to use the variable x that is in the outer scope.

# If we didn't have the nonlocal keyword, we would be creating a new variable x in the inner scope.
# Now we have two locations in memory for the variable x.

# Once we call the outer function, the computer destroys all this memory.
# Once we finish with the outer function, we can't call print(x) anymore.
# The garbage collector will come along and clean up all this memory.

# This is why scope matters. We have to be careful about how we use memory.



x = float(2.8)
print (x)