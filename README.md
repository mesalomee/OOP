# OOP

- Object/instance - same thing. 
- Attribute - variable created inside class
- Methods - functions inside classes

**Python passes the object/instance as a first parameter to the method, that’s why we pass self -  as a first parameter every time we create a method.**


If we want some attributes to be crucial, and if they are not passed then an instance won’t be created, we can execute something in the background the second the instance/object is created. This is when `__init__` method (magic method) comes handy. 

You can give default values to the attributes same way as it was in the functions.

You can add additional attributes to the object, which has not been created in the `__init__ ` method. If you need them.

In the method we can ask for special types for parameters. For example
`def __init__ (self, name: str)`
This means that it will only accept string as a parameter value 

If we have default value passed for the parameter then there is no need to specify type as it will expect same type as a default value.

We can run validations inside `__init__` method by using a word `assert`

It is possible to create attribute which is shared but all the objects. It is called class attribute.

If you call an attribute on an object first it tries to find it inside object, if it can’t find it there, it will search for the attribute on the class level. 

`__dict__` is a magic method which shows all the attributes of an object on object level or a class itself on class level

Double underscore - dunder
`__str__`  (nicely, readable representation of the object)
`__repr__`  (official string representation of the object)

When you directly refer to an object you are supposed to get repr method which is formal way of that object, but when you turn it into a string it is supposed to print string which is nicer and more understandable. 
