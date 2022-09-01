is_magician = False
is_expert = True

# Check if both conditions are true

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician and not(is_expert):
    print("You are a magician")

elif not(is_magician):
    print("Y'all need to learn magic")

else: print('I give up')