from pizza import Pizza
from extra_cheese import ExtraCheese
from mushroom_pizza import MushroomPizza
from chicken_pizza import ChickenPizza
from extra_spicy import ExtraSpicy

def main():
    pizza: Pizza = ExtraCheese(MushroomPizza())
    print("cost for Mushroom Pizza with extra cheese: ", pizza.cost())

    pizza: Pizza = ExtraSpicy(ChickenPizza())
    print("cost for spicy chicken pizza is: ", pizza.cost())


main()