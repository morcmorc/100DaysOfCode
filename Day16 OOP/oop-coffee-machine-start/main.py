from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    items = menu.get_items()
    choice = input(f"What would you like? ({items}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif choice == "off":
        print("Shutting down...")
        exit()
    elif choice in items:
        on = menu.find_drink(choice)
        if not coffee_maker.is_resource_sufficient(on):
            continue
    else:
        print("Wrong input!")
        continue

    # money part
    cost = on.cost
    if not money_machine.make_payment(cost):
        continue

    # make coffee
    coffee_maker.make_coffee(on)