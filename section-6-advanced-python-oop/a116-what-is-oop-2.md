# What is OOP (continued)?

[A paradigm. A way of thinking about programming and structuring our code.](https://en.wikipedia.org/wiki/Paradigm)

``` python
# OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Hello'))
print(type([]))
print(type(()))
print(type({}))
```

A procedural code was just like a procedure. Top-to-bottom, nothing special. Now, we're modeling real-world objects.

Car object: has data on the car, like color, make, model, etc. It also has methods, like drive(), brake(), etc.

By organizing things thusly, it's a better way to think and to run things. And Python is an object-oriented language. It's able to support this paradigm of objects and models.

## What is this `class` keyword?

``` python
class Car:
    pass
```

The naming convention is different than what we're used to. We're used to using snake_case, but for classes, we use CamelCase, where every new word is capitalized.

``` python
class BigArseTruck:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

obj1 = BigArseTruck('Ford', 'F-150', 'red')
print(obj1.make) # Ford
print(type(obj1)) # <class '__main__.BigArseTruck'>
```

## What just happened?

in OOP, there is idea of class and object. A class is a blueprint for an object. What are the properties? What methods can it take?

An object is an instance of a class. Think of a cookie cutter. The cookie cutter is the class. The cookie is the object.

The class can be ***instantiated*** by creating different *instances* of the class. We can create **multiple objects** from the same class.

``` python
class BigArseTruck:
  pass

obj1 = BigArseTruck()
```

The double bracket is us **instantiating** the class. We're creating an object from the class.

It's like creating a list. When we do, we have access to all the methods, and sometimes attributes, that are available to lists.

``` python
class BigArseTruck:
  pass

obj1 = BigArseTruck()
obj2 = BigArseTruck()
obj3 = BigArseTruck()
```
