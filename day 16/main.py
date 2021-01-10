from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_is_on = True
while machine_is_on:

    options = menu.get_items()
    my_choice = input("What would you like? ({}):".format(options))
    if my_choice == 'quit':
        machine_is_on = False
    elif my_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(my_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
