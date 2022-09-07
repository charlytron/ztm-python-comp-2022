# Attributes and Methods

OOP allows us to create objects that have their own methods and attributes.

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

It's a great way to add more functionality to our code. We need to group attributes together with methods to create a class that is able to mimic something in the real world.

When we write:

``` python
player.run()
```

our text editor shows us what we have access to, properties as well as methods.

If we write:

``` python
help(player1)
```

we actually get the entire blueprint of the object.

``` bash
Help on PlayerCharacter in module __main__ object:

class PlayerCharacter(builtins.object)
 |  PlayerCharacter(name, age)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  run(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```

Another cool thing is to look at built-in classes:

``` python
help(list)
```

We have to use the `self` keyword to refer to the object itself, making sure that is dynamic and can be used with different objects.

__But there's another thing called the *class object* attribute.__

What if we have to have a membership in order to play?

``` python

class PlayerCharacter:
    membership = True # class object attribute
    def __init__(self, name,age):
        self.name = name # attributes, or properties
        self.age = age 

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy', 20)
player2 = PlayerCharacter('Mildred', 21)

print(player1.membership) # True
print(player1.name) # Billy
print(player1.age) # 20
print(player2.name) # Mildred
print(player2.age) # 21
print(player1.run()) # run done
```

Unlike the regular class attributes, the class object attributes are the same for all instances of the class.
They're static.

``` python
print(player1.membership) # True
print(player2.membership) # True
```

All the players have the same membership, set to `True`. But this is obviously not dynamic. Class object doesn't change across instances.

Maybe we want to check membership; only if membership is `True` we want to assign the name and age. But in order for us to access membership, we need to use the class name.

``` python

class PlayerCharacter:
    membership = True # class object attribute
    def __init__(self, name,age):
        if (self.membership):
            self.name = name # attributes, or properties
            self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Billy', 20) #
player2 = PlayerCharacter('Mildred', 21)

print(player1.membership) # True
print(player1.name) # Billy
print(player1.age) # 20
print(player2.name) # Mildred
print(player2.age) # 21
print(player1.run()) # run done
```

We can also change the class object attribute above:

``` python
if (PlayerCharacter.membership):
    self.name = name # attributes, or properties
    self.age = age
```
