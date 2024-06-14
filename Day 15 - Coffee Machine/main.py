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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}

machine_on = True


def sufficient_resources(coffee_type):
    if MENU[f"{coffee_type}"]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif MENU[f"{coffee_type}"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough Coffee")
        return False
    elif coffee_type != "espresso":
        if MENU[f"{coffee_type}"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        return True
    else:
        return True


def process_money():
    print("Insert Coins:")
    quarters = int(input("How many quarters ? ")) * 0.25
    dimes = int(input("How many dimes ? ")) * 0.1
    nickles = int(input("How many nickles ? ")) * 0.05
    pennies = int(input("How many pennies ? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def make_coffee(coffe_type, total):
    if MENU[coffe_type]["cost"] > total:
        print("Sorry, money is insufficient, please collect your full refund ")
        return False
    else:
        change = round(total - MENU[coffe_type]["cost"], 2)
        resources["money"] = resources["money"] + MENU[coffe_type]["cost"]
        resources["water"] = resources["water"] - MENU[choice]["ingredients"][
            "water"]
        resources["coffee"] = resources["coffee"] - MENU[choice][
            "ingredients"]["coffee"]
        if coffe_type != "espresso":
            resources["milk"] = resources["milk"] - MENU[choice][
                "ingredients"]["milk"]
        print(f"Here is your change ${change}, enjoy the {coffe_type} 🍵 !")


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    else:
        if sufficient_resources(choice):
            payment = process_money()
            make_coffee(choice, payment)
