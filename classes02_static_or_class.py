#when to use class methods and when to use static methods?

class Item:
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
#class and static methods can be called on object as well as class but Usually it is called on Class and not on Object
print(Item.check_integer())
item1 = Item()
print(item1.check_integer())