print("Please enter the 10 resturant menu items and their prices")

n = 0
resturant_menu = {}
while n <= 2:
    item = input("Enter the menu item: ")
    price = float(input("Enter the price of the item: "))
    resturant_menu[item] = price
    n += 1
print("\n"*100)
print("\nResturant Menu")
for item, price in resturant_menu.items():
    menu_item = len(item)
    price_length = len(str(price))
    Total_length = menu_item + price_length
    print(f"\n{item} {'-' * (47 - Total_length)}INR {price}")    