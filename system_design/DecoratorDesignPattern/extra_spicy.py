from toppings_decorator import ToppingsDecorator
from pizza import Pizza

class ExtraSpicy(ToppingsDecorator):
    def __init__(self, pizza_obj: Pizza):
        self.pizza_obj = pizza_obj

    def cost(self):
        return 10 + self.pizza_obj.cost()