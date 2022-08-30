############################################################
#                   Password Checker                       #
############################################################                

username = input("What is your Username? ")
password = input("What is your password? ")
password_length = len(password)
hidden_password = password_length * '*'


print(f'Hey, {username}, youse password {hidden_password} is {password_length} characters long')