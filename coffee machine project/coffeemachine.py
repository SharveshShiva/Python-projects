MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
total = 0

def coffee_maker(money):
    price = 0
    get_info = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if get_info == "report":
        for i in resources:
            if i == "water" or i == "milk":
                print(f"{i.title()}: {resources[i]}ml")
            else:
                print(f"{i.title()}: {resources[i]}g")
        print(f"Money: ${money}")
        coffee_maker(money)

    elif get_info == "off":
        exit()

    elif get_info == "espresso" or get_info == "latte" or get_info == "cappuccino":
        if get_info == "espresso":
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))  # a
                dimes = int(input("how many dimes?: "))  # b
                nickles = int(input("how many nickles?: "))  # c
                pennies = int(input("how many pennies?: "))  # d
                total = amount_calculator(quarters, dimes, nickles, pennies)
                if total < 1.5:
                    print("Sorry that is not enough money. Money refunded.")
                    coffee_maker(money)
                else:
                    money = money + 1.5
                    price = 1.5
                    print(calculate_change(price, total))
                    print("Here is your espresso ☕️. Enjoy!")
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    coffee_maker(money)
            elif resources["water"] < 50:
                print("Your coffee machine does not have enough water and coffee for making espresso")
                coffee_maker(money)
            elif resources["water"] <= 50 and resources["coffee"] <= 18:
                print("Your coffee machine does not have enough water and coffee for making espresso")
                coffee_maker(money)
            else:
                print("Your coffee machine does not have enough coffee for making espresso")
                coffee_maker(money)

        elif get_info == "latte":
            if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))  # a
                dimes = int(input("how many dimes?: "))  # b
                nickles = int(input("how many nickles?: "))  # c
                pennies = int(input("how many pennies?: "))  # d
                total = amount_calculator(quarters, dimes, nickles, pennies)
                if total < 2.5:
                    print("Sorry that is not enough money. Money refunded.")
                    coffee_maker(money)
                else:
                    money = money + 2.5
                    price = 2.5
                    print(calculate_change(price, total))
                    print("Here is your latte ☕️. Enjoy!")
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    coffee_maker(money)
            elif resources["water"] < 200 and resources["coffee"] < 24 and resources["milk"] < 150:
                print("Your coffee machine does not have enough water and coffee and milk for making latte")
                coffee_maker(money)
            elif resources["water"] < 200 and resources["milk"] < 150:
                print("Your coffee machine does not have enough milk and water for making latte")
                coffee_maker(money)
            elif resources["water"] < 200:
                print("Your coffee machine does not have enough water for making latte")
                coffee_maker(money)
            elif resources["water"] < 200 and resources["coffee"] < 24:
                print("Your coffee machine does not have enough water and coffee for making latte")
                coffee_maker(money)
            elif resources["milk"] < 150 and resources["coffee"] < 24:
                print("Your coffee machine does not have enough milk and coffee for making latte")
                coffee_maker(money)
            elif resources["milk"] < 150:
                print("Your coffee machine does not have enough milk for making latte")
                coffee_maker(money)
            elif resources["coffee"] < 24:
                print("Your coffee machine does not have enough coffee for making latte")
                coffee_maker(money)
            else:
                coffee_maker(money)

        elif get_info == "cappuccino":
            if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))  # a
                dimes = int(input("how many dimes?: "))  # b
                nickles = int(input("how many nickles?: "))  # c
                pennies = int(input("how many pennies?: "))  # d
                total = amount_calculator(quarters, dimes, nickles, pennies)
                if total < 3:
                    print("Sorry that is not enough money. Money refunded.")
                    coffee_maker(money)
                else:
                    money = money + 3
                    price = 3
                    print(calculate_change(price, total))
                    print("Here is your cappuccino ☕️. Enjoy!")
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    coffee_maker(money)
            elif resources["water"] < 250 and resources["coffee"] < 24 and resources["milk"] < 100:
                print("Your coffee machine does not have enough water and coffee and milk for making cappuccino")
                coffee_maker(money)
            elif resources["water"] < 250 and resources["milk"] < 100:
                print("Your coffee machine does not have enough milk and water for making cappuccino")
                coffee_maker(money)
            elif resources["water"] < 250:
                print("Your coffee machine does not have enough water for making cappuccino")
                coffee_maker(money)
            elif resources["water"] < 250 and resources["coffee"] < 24:
                print("Your coffee machine does not have enough water and coffee for making cappuccino")
                coffee_maker(money)
            elif resources["milk"] < 100 and resources["coffee"] < 24:
                print("Your coffee machine does not have enough milk and coffee for making cappuccino")
                coffee_maker(money)
            elif resources["milk"] < 100:
                print("Your coffee machine does not have enough milk for making cappuccino")
                coffee_maker(money)
            elif resources["coffee"] < 24:
                print("Your coffee machine does not have enough coffee for making cappuccino")
                coffee_maker(money)
        else:
            coffee_maker(money)

def amount_calculator(a,b,c,d):
    amount_quarter = a * 0.25
    amount_dimes = b * 0.10
    amount_nickles= c * 0.05
    amount_pennies = d * 0.01
    total_money = amount_pennies + amount_nickles + amount_quarter + amount_dimes
    return total_money

def calculate_change(price,total_amount):
    if total_amount >= price:
        total_amount-=price
        return f"Here is ${round(total_amount,4)} in change."
    return None

coffee_maker(money)