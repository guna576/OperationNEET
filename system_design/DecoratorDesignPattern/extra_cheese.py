from toppings_decorator import ToppingsDecorator
from pizza import Pizza

class ExtraCheese(ToppingsDecorator):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza 

    def cost(self):
        return 20 + self.pizza.cost()