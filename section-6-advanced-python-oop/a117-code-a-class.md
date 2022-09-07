# Coding Our Own Class

We're working for a gaming company, and they're on this wizard kick.

``` python
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy')
print(player1) # <__main__.PlayerCharacter object at 0x7f8b8c0b4a90>
```

When we're building a class, we'll usually see `__init__` as the first method. This is the __constructor__. It's a special method that gets called when we instantiate the class.

What's up with the `self` parameter? It's a reference to the object itself, the `PlayerCharacter`, like `this` in JavaScript.

``` python
print player1.name # Billy
```

`self` refers to whatever is to the left of the dot. So, `self.name` is the same as `player1.name`. it allows us a reference to something that hasn't been created yet.

``` python
player2 = PlayerCharacter('Mildred')
print(player2.name) # Mildred
```

We can create different players with different attributes but still use the same code.

``` python
class PlayerCharacter:
    def __init__(self, name,age):
        self.name = name # attributes, or properties
        self.age = age 

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy', 20)
player2 = PlayerCharacter('Mildred', 21)

print(player1) # <__main__.PlayerCharacter object at 0x7f8b8c0b4a90>

print(player1.name) # Billy
print(player1.age) # 20
print(player2.name) # Mildred
print(player2.age) # 21
print(player1.run()) # run done
```

## `Player1` and `player2` are at different memory locations even though they're both instances of the same class

``` python
print(player1) # <__main__.PlayerCharacter object at 0x7f8b8c0b4a90>
print(player2) # <__main__.PlayerCharacter object at 0x7f8b8c0b4a90>
```

