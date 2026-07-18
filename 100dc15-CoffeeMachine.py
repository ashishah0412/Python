# Initial Resource
Initial_water = 100
Initial_milk = 50
Initial_coffee = 76
Initial_money  = 0
machine_state = "on"


coffee_master = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18},
    "latte": {"water": 200, "milk": 150, "coffee": 24},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24} 
}

def check_resources(coffee_type):  
    """Checks if there are enough resources to make the selected coffee type."""
    if (Initial_water < coffee_master[coffee_type]["water"] or
        Initial_milk < coffee_master[coffee_type]["milk"] or
        Initial_coffee < coffee_master[coffee_type]["coffee"]):
        return False
    return True

while machine_state == "on":
    print("Enter 1 for Print Report")
    print("Enter 2 for veding coffee")
    print("Enter 3 to put off the coffee vending machine")
    choice = int(input("Please enter your choice"))
    if choice == 3:
        machine_state = "off"
    elif choice == 1:
        print("printing report")
    elif choice == 2:
        print("What would you like? (espresso/latte/cappuccino): ")
        if check_resources == False:
            break
        else:
            print("preparing coffee")
    else:
        print("Please select correct option")





