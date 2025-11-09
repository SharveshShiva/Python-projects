from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_given = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

def coffee_maker():
    should_continue = True
    while should_continue:
        take_order = input(f"{menu_given.get_items()}report/off: ")

        if take_order == "report":
            coffee.report()
            money.report()

        elif take_order == "off":
            should_continue = False

        elif take_order == "espresso":
            if coffee.is_resource_sufficient(MenuItem("espresso",50,0,18,1.5)):
                money.make_payment(1.5)
                coffee.make_coffee(MenuItem("espresso",50,0,18,1.5))

        elif take_order == "latte":
            if coffee.is_resource_sufficient(MenuItem("latte", 200, 150, 24, 2)):
                money.make_payment(2)
                coffee.make_coffee(MenuItem("latte", 200, 150, 24, 2))

        elif take_order == "cappuccino":
            if coffee.is_resource_sufficient(MenuItem("cappuccino", 250, 100, 24, 3)):
                money.make_payment(3)
                coffee.make_coffee(MenuItem("cappuccino", 250, 100, 24, 3))
        else:
            should_continue = True

coffee_maker()

# without find_drinks function.


