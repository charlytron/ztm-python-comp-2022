##############################################################################
#                     Default Parameters and Keyword Arguments              #
##############################################################################



fname = "Funky"
lname = "Winkerbean"

# Position plays no role in keyword arguments

# Before, we used positional parameters:
def my_function(fname, lname): # fname and lname are parameters
    print(f'Jello, {fname} {lname}')

# And we passed positional arguments:
my_function("Gomer", "Pyle") # fname and lname are arguments
# These arguments override the parameters

my_function("Pyle", "Gomer") # position matters


# Now, we can use keyword arguments:
#my_function(lname="Flubble", fname="Gomer") # fname and lname are arguments

# We can argue that Keyword arguments are bad practice
# But, they are useful when we have a lot of parameters
# When not at scale, tough, keyword arguments over-complicate things

# Default parameters
# We can set default values for parameter

def my_function(fname, lname="Vader"): 
    print(f'Jello, {fname} {lname}')

my_function("Gomer") # fname and lname are arguments
# We can still pass a value for lname
# But, we don't have to

