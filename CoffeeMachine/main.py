
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money_earned = 0


def process_coins():
    """Function to collect money from the user."""
    print("Please insert coins.")
    quarter = int(input("How many quarters?: ")) * 0.25
    dime = int(input("How many dimes?: ")) * 0.10
    nickel = int(input("How many nickels?: ")) * 0.05
    penny = int(input("How many pennies?: ")) * 0.01
    total_money = round(quarter + dime + nickel + penny, 2)
    return total_money


def check_resources(order_ingredients):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(order_name, order_ingredients):
    """Deduct ingredients from resources and serve coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order_name}. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine."""
    global money_earned
    while True:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino/report/exit): ").lower()

        if choice == "exit":
            print("Turning off the machine. Goodbye!")
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money_earned:.2f}")
        elif choice in MENU:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    money_earned += drink["cost"]
                    make_coffee(choice, drink["ingredients"])
                    if change > 0:
                        print(f"Here is ${change} in change.")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please select from the menu.")


coffee_machine()
