class PlayerCharacter:
    def __init__(self, name,age):
        self.name = name # attributes, or properties
        self.age = age 

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy', 20)
player2 = PlayerCharacter('Mildred', 21)

# print(player1) # <__main__.PlayerCharacter object at 0x7f8b8c0b4a90>

# print(player1.name) # Billy
# print(player1.age) # 20
# print(player2.name) # Mildred
# print(player2.age) # 21
# print(player1.run()) # run done

# help(player1)
help(list)