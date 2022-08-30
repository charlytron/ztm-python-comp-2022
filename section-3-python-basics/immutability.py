############################################################
#                       IMMUTABILITY                       #
############################################################

# Immutability is the property of an object that it cannot be changed.

# previous chapter's example of step-over is called slicing"

sequencer = '01234567'
print(sequencer[0:3:2]) # 02 step by 2

# Now, we need to discuss immutability.

# Strings are immutable. This means that they cannot be changed.
# We could reassign sequencer to a new value, but we can't reassign the value of a string.

# sequencer[0] = 9 # this will raise an error
print(sequencer) 
# TypeError: 'str' object does not support item assignment

# Reassignment of the variable sequencer removes the previous value from memory.
# Instead, we can reassign the variable sequencer to a new value.

sequencer = '100'

# We'll talk about immutability more in the context of lists.