############################################################
#                   Password Checker                       #
############################################################                

password = input("What is your password? ")
password_length = len(password)
password = password_length * '*'


print(f'password {password} is {password_length} characters long')