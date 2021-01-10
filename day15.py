menu = {
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
machine_resources = {"water": 300, "milk": 200, "coffee": 100}
machine_money = 0


def description_of_drinks(offert):
    for drink in offert:
        print(f'{drink.title()}: ${offert[drink]["cost"]}')


def report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f'Money: ${machine_money}')


def paying():
    print("Please insert coins.")
    quarters = int(input('How many quarters?: ')) * 0.25
    dimes = int(input('How many dimes?: ')) * 0.10
    nickles = int(input('How many nickles: ?')) * 0.05
    pennies = int(input('How many pennies: ?')) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_enough_resources(order):
    for ingredient in order:
        if order[ingredient] > machine_resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


def is_enough_money(given_money, drink_cost):
    global machine_money
    print(given_money)
    if given_money >= drink_cost:
        change = given_money - drink_cost
        print(change)
        if change <= machine_money:
            print(f'Your change: ${change}')
            machine_money += drink_cost
            return True
        else:
            print(f'There is no more coins in Machine for change. Pay the exact price of the product')
            return False
    else:
        print("Sorry, not enough money. Money refunded.")
        return False


def make_coffee(name_of_product, order):
    for ingredient in order:
        machine_resources[ingredient] -= order[ingredient]
    print(f'Here is your {name_of_product}, Enjoy')


machine_is_on = True

while machine_is_on:

    my_input = input("What would you like? (espresso/latte/cappuccino):")
    if my_input == 'quit':
        machine_is_on = False
    elif my_input == 'offer':
        description_of_drinks(menu)
    elif my_input == 'report':
        report()
    else:
        drink_choice = menu[my_input]
        if is_enough_resources(drink_choice['ingredients']):
            payment = paying()
            if is_enough_money(payment, drink_choice['cost']):
                make_coffee(my_input, drink_choice['ingredients'])
