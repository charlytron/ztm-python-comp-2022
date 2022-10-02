from random import randint
import sys
# generate a number 1 - 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# check that input is a number from 1 to 10
while True:
    try:
        print(answer)
        guess = int(input('guess a number from 1 to 10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('all good')
                break
        else:
            print('hey, doobah, 1 -10, okay?')
    except ValueError:
        print('Please enter a number')
        continue

# check if number is the right guess
