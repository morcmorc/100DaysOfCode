import math

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

# coins: penny = 1 cent, Nickel = 5 cents, Dime = 10 cents, Quater = 25 cents
# report() gives information about: water 300ml, milk 200ml, coffee 100g, money 0$
# what would you like? (espresso/latte/cappuccino): latte // here i need to check resources
# Please insert coins.
# How many quaters?: 12
# How many dimes?: 12
# Hpw many nickels?: 12
# How many pennies?: 12 // not enough money? -> return
# Here is ${change} in change.
# Here is your latte (coffee emoji) Enjoy!
# What would you like? e/l/c -> report substract ingredians for latte -> cappuccino -> but money from latte is in it
# Sorry, ther is not enough water.

def main():
    # variables
    money = 0
    # ingredients
    machine = {"water": 300,
               "milk": 200,
               "coffee": 100,
               "money": 0}
    # water = 300
    # milk = 200
    # coffee = 100
    # machine = [water,milk,coffee]
    offer = MENU.keys()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino)").lower()
        if choice == "report":
            report(machine)
        elif choice == "off":
            print("Shutting down...")
            exit()
        elif choice in offer:
            # print(check_ingredients(MENU[choice], machine))
            x = check_ingredients(MENU[choice], machine)
            if x != True:
                print(f"not enough {x}.")
                continue
            
            # get_coins()
            price = MENU[choice]["cost"]
            if get_coins(price,machine):
                remove_ingredients(choice,machine)
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("wrong input")



def check_ingredients(coffee,machine):
    ingredients_dict = coffee["ingredients"]
    if ingredients_dict.get("water",0) > machine["water"]:
        return "Water"
    elif ingredients_dict.get("milk",0) > machine["milk"]:
        return "Milk"
    elif ingredients_dict.get("coffee",0) > machine["coffee"]:
        return "coffee"
    else: 
        return True

def remove_ingredients(coffee,machine):
    ingredients_dict = coffee["ingredients"]
    machine["water"] -= ingredients_dict.get("water",0)
    machine["milk"] -= ingredients_dict.get("milk",0)
    machine["coffee"] = ingredients_dict.get("coffee",0)
    return True

def report(machine):
    milk = machine.get("milk")
    water = machine.get("water")
    coffee = machine.get("coffee")
    money = machine.get("money")
    print(f"the current resources are:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def get_coins(price,machine):
    total_inserted = 0
    print("Insert coins:")
    quaters = int(input(("How many quaters?: "))) * 0.25 
    dimes = int(input(("How many dimes?: "))) * 0.10
    nickels = int(input(("How many nickels?: "))) * 0.05
    pennies = int(input(("How many pennies?: "))) * 0.01

    total_inserted = quaters + dimes + nickels + pennies
    total_inserted = round(total_inserted,2)
    if total_inserted > price:
        change = total_inserted - price 
        change = round(change,2)
        # print(f"change: {change} total_inserted: {total_inserted}")
        print(f"You inserted: ${total_inserted} and this is your change: ${change}")
        machine["money"] += price
        return True
    else:
        print(f"You only inserted: ${total_inserted}, but it costs: ${price}")
        return False


main()