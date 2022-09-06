class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy')
print(player1) #
print(player1.run()) # run done