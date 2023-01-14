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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print("Here your coffee ☕")


def is_resource_sufficient(order_ingredient):
    for item in resources:
        if order_ingredient[item] >= resources[item]:
            return False
        else:
            return True


def process_coins():
    '''Calculate the money'''
    print("Enter the coins: ")
    total = int(input("Enter the number of Quarters: ")) * 0.25
    total += int(input("Enter the number of Dimes: ") ) * 0.10
    total += int(input("Enter the number of Nickles: ")) * 0.05
    total += int(input("Enter the number of Pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''Calculate profit '''
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"here your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money")
        return False


machine_is_on = True
while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        machine_is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink, drink['ingredients'])





