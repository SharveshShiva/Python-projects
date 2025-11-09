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
        drink = menu_given.find_drink(take_order)

        if take_order == "report":
            coffee.report()
            money.report()

        elif take_order == "off":
            should_continue = False

        else:
            if coffee.is_resource_sufficient(drink):
                money.make_payment(drink.cost)
                coffee.make_coffee(drink)

coffee_maker()

# with find_drinks function.