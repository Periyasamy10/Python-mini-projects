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


def check_resource(order_resource):
    for item in order_resource:
        if order_resource[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"The change is ${change}")
        profit += drink_cost
        return True
    else:
        print("Not enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


profit = 0
is_continue = True
while is_continue:
    choice = input("What would you like ? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"coffee: {resources['coffee']}g")
        print(f"milk: {resources['milk']}ml")
        print(f"water: {resources['water']}ml")
        print(f"money: ${profit}")

    elif choice == 'off':
        is_continue = False
    else:
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice,drink['ingredients'])
