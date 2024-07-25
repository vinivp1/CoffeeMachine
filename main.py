from recipes import MENU, resources, cash

machine_on = True

def money ():
    """Count the money received from the client/user"""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def enough_resource(order_ingredients):
    """Verify if have enough ingredients to make the coffee"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry that's not enough {item}")
            return False
    return True

def success_payment(money_received , drink_cost):
    """If the money received is equal or up from the drink cost returns True, besides it returns False
     and returns the change"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Remove the ingredients used from the report page"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        machine_on = False
    elif order == 'report':
        print (f"Water:, {resources["water"]}ml")
        print (f"Milk:, {resources["milk"]}ml")
        print (f"Coffee:, {resources["coffee"]}g")
        print (f"Money:, ${cash}")
    else:
        drink = MENU[order]
        if enough_resource(drink["ingredients"]):
            payment = money()
            if success_payment(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
