from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


list_of_drinks = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()




options = list_of_drinks.get_items()

running = True

while running == True:
    choice = input(f"What would you like?  {options}: ").lower()
    if choice == "off":
        running = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        choice = list_of_drinks.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(choice):
            price = choice.cost
            if my_money_machine.make_payment(price):
                my_coffee_maker.make_coffee(choice)





