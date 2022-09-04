##############################################################################
#                      Arguments vs Parameters in Python                     #
##############################################################################

# Arguments are the values passed to a function when it is called.
# Parameters are the variables listed inside the parentheses in the function

fname = "Funky"
lname = "Winkerbean"

def my_function(fname, lname): # fname and lname are parameters
    print(f'Jello, {fname} {lname}')

my_function(fname, lname) # fname and lname are arguments
# These arguments override the parameters, as in
my_function("Gomer", "Pyle")

# Arguments are used to pass values to a function

# Parameters are used to define the values that will be passed to the function
# Arguments are used to pass values to a function, dig?

