from recipes import MENU, resources, cash

machine_on = True
order = ""

def money ():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    qt = quarters * 0.25
    dm = dimes * 0.10
    nck = nickles * 0.05
    pn = pennies * 0.01
    money = qt + dm + nck + pn
    return money

while not order == 'off':
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print ("Water:", resources["water"],
           "\nMilk:", resources["milk"],
           "\nCoffee:", resources["coffee"],
           "\nMoney:", cash["money"])
    if order == 'espresso':
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
           print("Sorry there is not enough water.")
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
           print("Sorry there is not enough coffee.")
        print ("Please insert coins.")
        if cash["money"] is None:
            cash["money"] = 0.0
        cash["money"] = money()
        if MENU["espresso"]["cost"] == cash["money"]:
            cash["money"] += MENU["espresso"]["cost"]
        if MENU["espresso"]["cost"] < cash["money"]:
            change = cash["money"] - MENU["espresso"]["cost"]
            print(f"Here is ${change} dollars in change.")
        else:
          print("Sorry that's not enough money. Money refunded.")
          money = 0

        # if MENU["espresso"]["ingredients"]["water"] < resources["water"]:
        #    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        # if MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]:
        #    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

    if order == 'latte':
        if MENU["latte"]["ingredients"]["water"] > resources["water"]:
           print("Sorry there is not enough water.")
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
           print("Sorry there is not enough coffee.")
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
           print("Sorry there is not enough milk.")
        if MENU["latte"]["ingredients"]["water"] < resources["water"]:
           resources["water"] -= MENU["latte"]["ingredients"]["water"]
        if MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]:
           resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        if MENU["latte"]["ingredients"]["milk"] < resources["milk"]:
           resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    if order == 'cappuccino':
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
           print("Sorry there is not enough water.")
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
           print("Sorry there is not enough coffee.")
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
           print("Sorry there is not enough milk.")
        if MENU["cappuccino"]["ingredients"]["water"] < resources["water"]:
           resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        if MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]:
           resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        if MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:
           resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

print(resources)

