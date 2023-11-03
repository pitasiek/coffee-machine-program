# Made by Piotr Zięba on 02.11.2023. This project is related with day 15.
# It is a coffee machine.

from data import menu    # menu dictionary with information about coffees and their ingredients.


def check_for_ingredients(picked):    # A little bit tricky, it wasn't well explained about this use of dictionaries.
    """Checks whether the machine has enough ingredients and then returns True or False"""
    for i in picked:
        if picked[i] > ingredients[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def is_it_enough():
    """User inputs money and this functions checks whether it is enough for a cup of coffee"""
    print(f"Please insert ${order['cost']} in coins.")
    coins = float(input("how many quarters?: ")) * 0.25
    coins += float(input("how many dimes?: ")) * 0.1
    coins += float(input("how many nickles?: ")) * 0.05
    coins += float(input("how many pennies?: ")) * 0.01
    return coins


def make_the_order(cash):
    """Prepares coffee and returns earned money."""
    if cash == order['cost']:
        print(f"Making {coffee_selected}... 3... 2... 1... Ready!")
        print("Take your coffee. Enjoy!")
        return cash
    elif cash > order['cost']:
        cash = cash - order['cost']
        rounded = round(cash, 2)
        print(f"Here is your change: ${rounded}")
        print(f"Making {coffee_selected}... 3... 2... 1... Ready!")
        print("Take your coffee. Enjoy!")
        cash = order['cost']
        return cash
    else:
        print(f"Your coins are total: ${cash} but you need ${order['cost']}. You need more coins. Money refunded.")
        cash = 0
        return cash


def subtracts_spent_ingredients(ing):
    """Subtracts spent ingredients from those in the machine storage."""
    for item in ing:
        ingredients[item] -= ing[item]


ingredients = {    # Machine's storage.
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0    # Money earned.
while True:    # While loop for the game system.
    coffee_selected = input("What would you like? (espresso/latte/cappuccino):")    # Decision about your coffee.
    if coffee_selected == "off":    # Turns the machine off.
        print("'Off' command turns this machine off.")
        off = input("Are you sure to turn it off? y or n")
        if off == "y":
            print("Good bye!")
            break
    elif coffee_selected == "report":    # Report for the technician.
        print(f"Water: {ingredients['water']}ml")
        print(f"Milk: {ingredients['milk']}ml")
        print(f"Coffee: {ingredients['coffee']}g")
        print(f"Money: ${money}")
    else:
        order = menu[coffee_selected]    # Gets hold of the selected coffee ingredients and price.
        if check_for_ingredients(order['ingredients']):    # Checks whether we have enough ing.
            given_money = is_it_enough()    # Sums up user's money.
            money += make_the_order(given_money)    # Prepares order for the user and returns earned money.
            subtracts_spent_ingredients(order['ingredients'])    # Gives us updated amount of ingredients.
            