# OOP 

## Live Session 1
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

It is possible to create attribute which is shared by all the objects. It is called class attribute.

If you call an attribute on an object first it tries to find it inside object, if it can’t find it there, it will search for the attribute on the class level. 

`__dict__` is a magic method which shows all the attributes of an object on object level or a class itself on class level

Double underscore - dunder
`__str__`  (nicely, readable representation of the object)
`__repr__`  (official string representation of the object)

When you directly refer to an object you are supposed to get repr method which is formal way of that object, but when you turn it into a string it is supposed to print string which is nicer and more understandable. 
Classes 2




## Live Session 2

If we want to create a method inside a class that will create an instance/object (instantiate), we can’t create an object method as the object has not been created yet. So we need to create a class method instead. 

To create a class method, 
1. we don’t need to pass the object self as a parameter
2. We need to add decorator @classmethod before a method to declare it as a class method
3. We need to pass the class itself as the first parameter 

def instantiate_from_csv(cls):


#### Difference between static and class methods:
 @staticmethod
    def check_integer():
        '''
        This is something that has a relationship with a class but
        is not something that is unique for per instance'''
        
        '''
        This def could be used as an isolated function outside the class but
        as it is in relation with a class it is inside the class and not outside
        '''
    
    @classmethod
    def instantiate_from_something(cls):
        '''
        Usually, are used to manipulate different structures of data to instantiate objects
        (create objects/instances)
        '''

The static method doesn’t pass ტჰე object as a first argument. The class method has a mandatory first parameter - class itself - cls


For each child class we create, we need to call the super() function in the __init__ in order to have access to all the attributes and methods a parent has. 

self.__class__.__name__ is a way to access the name of the object’s class


To create readable code we better have each class in a separate file and one file for creating instances. 

The idea is that an object should be like a black box—you don't need to know what the box contains, as long as you know (or can find out) what methods it supports. This black box approach is known as encapsulation.  (concept of bundling data and methods within a single unit)


It is possible to restrict users to overwrite attributes after initialising the instances.

To create read-only attributes we need to use decorator (they are functions that pre-execute before a function) @property
We create a function that has the name of the attribute we want to be untouchable (which are called properties)
