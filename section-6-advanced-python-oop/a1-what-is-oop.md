# What is OOP?

Everything in Python is an object.

What does that mean? It means that every variable you create is an object. Every function you create is an object. Even the modules you import are objects.

``` python
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Hello'))
print(type([]))
print(type(()))
print(type({}))
```

When we print out these types, we get the following:

``` python
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>

<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
```

All of these data types have the class type in front of them. This is because they are all objects. They are all instances of a class.

In Python, everything is built by this class keyword. We're able to use different methods on our objects to perform some actions on them, using the dot method.

But OOP allows us to go beyond what we're given. With the `class` keyword we can do this.

## We can create our own data types, with different attributes and methods

**why is this useful?**

We can structure our code in a way that is easier to maintain, extend and write.

Amazon Drone example:

Propeller object
Camera object
Claws object that holds the package
Battery object
GPS object
etc.

We're dividing functionality into different objects. This is a very common pattern in OOP. Should we wish to create another type of delivery system, we can extend the functionality from our Drone.
