# def sum(num1, num2):
#     return num1 + num2
# total = sum(10, 20)    
# print(sum(56, total)) # 86
# print(sum(56, sum(10, 20))) # 86
# The return statement is used to exit a function and go back to the place from
# where it was called

# A function should do one thing and do it well
# A function should return something

# Nested functions

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
total = sum(10, 20)
print(total) # Returns None if no return  statement is used in the outer function
# otherwise returns 30.

# A return automatically exits the function

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    return 5 # This line will never be executed
    print('Hello') # This line will never be executed
