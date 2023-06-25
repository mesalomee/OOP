import csv

class Item:
    all = []
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity = 0):
        #Validations
        assert price>=0, f"Price {price} is not greater or equal to zero"
        assert quantity>=0, f"Price {quantity} is not greater or equal to zero"
        
        #Assign to self object 
        self.__name = name
        self.price = price
        self.quantity = quantity
    
    
        #Actions to execute
        Item.all.append(self)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception("This name is too long!")
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    @classmethod
    def instances_from_csv(cls):
        with open('OOP/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def check_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}'s price is {self.price} and we have {self.quantity} of them"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    

    @property
    def read_only_name(self):
        return "This is #0001"

item1 = Item("myItem", 12)
print(item1.read_only_name)
item1.name = "OtherName"
print(item1.name)