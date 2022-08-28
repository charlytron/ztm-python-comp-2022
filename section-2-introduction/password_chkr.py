############################################################
#                   Password Checker                       #
############################################################                

username = input("What is your Username? ")
password = input("What is your password? ")
password_length = len(password)
password = password_length * '*'


print(f'Hey, {username}, youse password {password} is {password_length} characters long')