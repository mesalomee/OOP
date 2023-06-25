from item import Item


class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=0, broken_phone = 0):
        super().__init__(name, price, quantity)
        #Validations
        assert broken_phone >=0, f"Broken phones {broken_phone} is not greater or equal to zero"

        #Assign to self object 
        self.broken_phones = broken_phone
