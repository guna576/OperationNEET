
# The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one responsibility or job


class Book:
    def __init__(self,
            title: str,
            author: str,
            price: float
    ):
        self.title = title
        self.author = author 
        self.price = price
    
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price