# 100 Days of Code
# Coffee Machine

from data import MENU, resources
from art import logo

# Coins
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# Resources
remaining_water = resources["water"]
remaining_milk = resources["milk"]
remaining_coffee = resources["coffee"]


def tabulate_payment(quarters, dimes, nickels, pennies):
    """Counts coins given to machine, returns total dollar amount given"""
    quarter_amount = quarters * QUARTER
    dime_amount = dimes * DIME
    nickel_amount = nickels * NICKEL
    penny_amount = pennies * PENNY
    change = quarter_amount + dime_amount + nickel_amount + penny_amount
    return change


def change_back(amount_given, cost):
    """Returns change to customer if required"""
    difference = amount_given - cost
    return difference


def print_report():
    """Displays remaining amount of material"""
    print(f"Water: {remaining_water}ml")
    print(f"Milk: {remaining_milk}ml")
    print(f"Coffee: {remaining_coffee}mg")
    print("Money: $0")


def check_supply(drink):
    """Checks supply of material required to make each drink"""
    if drink == "espresso":
        if remaining_water >= 50 and remaining_coffee >= 18:
            supply_ok = True
            return supply_ok
        else:
            if remaining_water < 50:
                print("Sorry, there is not enough water.")
            elif remaining_coffee < 18:
                print("Sorry, there is not enough coffee.")
            supply_ok = False
            return supply_ok
    elif drink == "latte":
        if remaining_water >= 200 and remaining_milk >= 150 and remaining_coffee >= 24:
            supply_ok = True
            return supply_ok
        else:
            if remaining_water < 200:
                print("Sorry, there is not enough water.")
            elif remaining_milk< 250:
                print("Sorry, there is not enough milk.")
            elif remaining_coffee < 24:
                print("Sorry, there is not enough coffee.")
            supply_ok = False
            return supply_ok
    elif drink == "cappuccino":
        if remaining_water >= 250 and remaining_milk >= 100 and remaining_coffee >= 24:
            supply_ok = True
            return supply_ok
        else:
            if remaining_water < 250:
                print("Sorry, there is not enough water.")
            elif remaining_milk< 100:
                print("Sorry, there is not enough milk.")
            elif remaining_coffee < 24:
                print("Sorry, there is not enough coffee.")
            supply_ok = False
            return supply_ok


def make_coffee(drink):
    """Prints out the ordered drink, with a smile"""
    if drink == "espresso":
        print("Here is your espresso ☕ Enjoy!")
    elif drink == "latte":
        print("Here is your latte ☕ Enjoy!")
    elif drink == "cappuccino":
        print("Here is your cappuccino ☕ Enjoy!")


def coffee_machine():
    """Takes requested drink and verifies payment"""
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    cost = 0
    drink_type = input(" What would you like? (espresso = $1.50 / latte = $2.50 / cappuccino = $3.00): ")
    if drink_type == "espresso":
        cost = espresso_cost
        print(f"Please insert ${espresso_cost} in coins.")
    elif drink_type == "latte":
        cost = latte_cost
        print(f"Please insert ${latte_cost} in coins.")
    elif drink_type == "cappuccino":
        cost = cappuccino_cost
        print(f"Please insert ${cappuccino_cost} in coins.")
    elif drink_type == "report":
        print_report()
        coffee_machine()

    supply_ok = check_supply(drink=drink_type)

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    amount_given = tabulate_payment(quarters, dimes, nickels, pennies)

    if amount_given >= cost:
        order_ok = True
        change_owed = change_back(amount_given, cost)
        print(f"Here is ${round(change_owed, 2)} in change")
    else:
        order_ok = False
        print("Sorry, that's not enough money. Here's your refund.")
        coffee_machine()

    if order_ok and supply_ok:
        make_coffee(drink_type)
        return drink_type


# main coffee machine loop
print(logo)

while True:
    drink_served = (coffee_machine())

    if drink_served == "espresso":
        remaining_water -= 50
        remaining_coffee -= 18
    elif drink_served == "latte":
        remaining_water -= 200
        remaining_milk -= 150
        remaining_coffee -= 24
    elif drink_served == "cappuccino":
        remaining_water -= 250
        remaining_milk -= 100
        remaining_coffee -= 18









