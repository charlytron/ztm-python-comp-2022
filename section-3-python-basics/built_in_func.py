############################################################
#                    BUILT-IN FUNCTIONS                    #
############################################################

# Built-in functions are functions that are part of the language itself.

# str() # converts any object to a string
# int() # converts any object to an integer
# type() # returns the type of an object
# print() # prints to the screen
# float() # converts any object to a float
# bool() # converts any object to a boolean
# len() # returns the length of a string or list
# abs() # returns the absolute value of a number
# round() # rounds a number to the nearest integer
# max() # returns the largest number in a list
# min() # returns the smallest number in a list
# sum() # returns the sum of all numbers in a list
# range() # returns a list of numbers from start to end
# list() # converts a string to a list
# tuple() # converts a string to a tuple
# chr() # converts an integer to a character
# ord() # converts a character to an integer

print(len('Jelllooooooo')) # returns 12, the length of a string
# len counts from 1

greet = 'Jelllooooooo'
print(greet[0:]) # prints the entire string
print(greet[:]) # prints the entire string
print(greet[0:len(greet)]) # prints the entire string

############################################################
#                    BUILT-IN METHODS                      #
############################################################

# Built-in methods are functions that are part of the language itself.
# They are used to modify the behavior of an object.

# They usually begin with a dot (.)

# String methods are used to modify the behavior of a string.

# str.format() # formats a string
# str.upper() # converts a string to uppercase
# str.lower() # converts a string to lowercase
# str.capitalize() # capitalizes the first letter of a string
# str.title() # capitalizes the first letter of each word in a string
# str.count() # counts the number of times a substring occurs in a string
# str.find() # finds the first occurrence of a substring in a string
# str.replace() # replaces a substring in a string with another substring
# str.strip() # removes whitespace from the beginning and end of a string
# str.split() # splits a string into a list of substrings
# str.join() # joins a list of strings into a single string
# str.startswith() # returns True if a string starts with a specified substring
# str.endswith() # returns True if a string ends with a specified substring
# str.isalpha() # returns True if a string contains only letters
# str.isdigit() # returns True if a string contains only digits
# str.isalnum() # returns True if a string contains only letters or digits
# str.isspace() # returns True if a string contains only whitespace
# str.istitle() # returns True if a string contains only titlecase characters
# str.isupper() # returns True if a string contains only uppercase characters
# str.islower() # returns True if a string contains only lowercase characters
# str.index() # returns the index of the first occurrence of a substring
# str.rindex() # returns the index of the last occurrence of a substring

quote = "OU812? I81B4U!"
print(quote.lower()) # converts the string to lowercase
print(quote.capitalize()) # capitalizes the first letter of a string
print(quote.center(50, '*')) # centers a string in a field of a specified width

# Don't worry about dunder methods. They are relevant to classes.

print(quote.find('81')) # returns the index of the first occurrence of a substring

print(quote.replace('81', 'ATE ONE')) # replaces a substring in a string with another substring

print(quote) # prints the original string because it was not modified

