# Initial Resource
Initial_water = 500
Initial_milk = 500
Initial_coffee = 200
Initial_money  = 0
machine_state = "on"
coffee_type = ""


coffee_master = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18,"cost":2.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24,"cost":3.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24,"cost":4.0} 
}

def check_resources(coffee_type):  
    """Checks if there are enough resources to make the selected coffee type."""
    if (Initial_water < coffee_master[coffee_type]["water"]):
        print("Sorry there is not enough water.")
        return False
    elif (Initial_milk < coffee_master[coffee_type]["milk"]):
        print("Sorry there is not enough Milk.") 
        return False
    elif (Initial_coffee < coffee_master[coffee_type]["coffee"]):
        print("Sorry there is not enough Coffee.")
        return False
    else:
        return True

def print_report():
    print("printing report")
    print(f"Total water in coffee machine : {Initial_water}")
    print(f"Total milk in coffee machine : {Initial_milk}")
    print(f"Total coffee in coffee machine : {Initial_coffee}")
    print(f"Total money collected in coffee machine :$ {Initial_money}")

def make_coffee_collect_money(coffee_type):
    global  Initial_water
    global Initial_milk
    global Initial_coffee
    global Initial_money

    print("Please insert the coins mentioning number of Quarters, Dimes,Pennies or nickles")
    quarters = float(input("Number of Quarters: "))
    dimes = float(input("Number of Dimes: "))
    nickles  = float(input("Number of nickles: "))
    pennies  = float(input("Number of pennies: "))
    total = 0.25*quarters+0.10*dimes+0.05*nickles+0.01*pennies
    print(f"You paid amount: ${total:.2f}")
    if (coffee_master[coffee_type]["cost"]>total):
        print("Sorry that's not enough money")
        print(f"Money Refunded: ${total:.2f}")
    else:
        refund = total - coffee_master[coffee_type]["cost"]
        Initial_water -= coffee_master[coffee_type]["water"]
        Initial_milk -= coffee_master[coffee_type]["milk"]
        Initial_coffee -= coffee_master[coffee_type]["coffee"]
        Initial_money  += coffee_master[coffee_type]["cost"]
        machine_state = "on"
        print(f"Your refund is: ${refund:.2f}")
        print(f"Please enjoy you {coffee_type}")

while machine_state == "on":
    print("Enter 1 for Print Report")
    print("Enter 2 for veding coffee")
    print("Enter 3 to put off the coffee vending machine")
    choice = int(input("Please enter your choice"))

    if choice == 1:
        print_report()
    elif choice == 2:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type not in coffee_master:
            print("Please check the coffee type selected by you.")
            continue
        if check_resources(coffee_type) == False:
            break
        else:
            make_coffee_collect_money(coffee_type)          
    elif choice == 3:
        machine_state = "off"                      
    else:
        print("Please select correct option")
    