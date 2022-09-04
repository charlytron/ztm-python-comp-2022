##############################################################################
#                             Function vs Method                             #
##############################################################################

# Function
def my_func():
    pass

# Method
class MyClass:
    def my_method(self):
        pass

# Whatever is to the left of the dot is the object that owns the method

"jello".capitalize() # String object owns the capitalize method
print("jello".capitalize()) # Jello