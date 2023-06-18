class Item:
    all = []
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity = 0):
       #Validations
       assert price>=0, f"Price {price} is not greater or equal to zero"
       assert quantity>=0, f"Price {quantity} is not greater or equal to zero"
        
       #Assign to self object 
       self.name = name
       self.price = price
       self.quantity = quantity
       
       #Actions to execute
       Item.all.append(self)
       
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    def __str__(self):
        return f"{self.name}'s price is {self.price} and we have {self.quantity} of them"
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
