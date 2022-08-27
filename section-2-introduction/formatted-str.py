############################################################
#                    FORMATTED STRINGS                     #
############################################################

# Formatted strings are strings that contain placeholders for variables.

name = "B-b-billy"
# age = str(20)
age = 26

print('My name is ' + name + '. I am ' + str(age) +  ' years old, and I still don\'t know what to do') 
# Hello Billy. You are 20 year old, and you still don't know what to do

# You can use the 3.6 format() method to do the same thing, saving you from having to type out the string.

print(f'My name is {name}. I am {age} years old, and I still don\'t know what to do')

# This is called an f-string.

# Before Python 3.6, we had to use the .format() method:

print('My name is {}. I am {} years old, and I still don\'t know what to do'.format('Billy', '26'))

# But this doesn't allow us to use variables in the placeholders.

print('My name is {0}. I am {1} years old, and I still don\'t know what to do'.format(name, age))

# Between the curly braces, you can put the position of the variable names you want to use
# per the order they occur in the string.

# Or we could create new variable names on the fly:

print('My name is {new_name}. I am {age} years old, and I still don\'t know what to do'.format(new_name='Thor', age=100))