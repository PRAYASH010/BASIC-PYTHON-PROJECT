coffee_products = {
    'Black Coffee' : 150,
    'White Coffee' : 200,
    'Hot Coffee' : 250,
    'Cold Coffee' : 300,
}
soft_drinks = {
    'CoCo Cola' : 100,
    'Fanta' : 100,
    'Mountain Dew' : 100,
}
sweet_items = {
    'Chocolate Cake' : 500,
    'Strawberry Cake' : 550,
    'Pastery' : 200
}

# 1. Ask the user what category they want
navigation = input("What are you looking for? (coffee, drinks, sweets): ").strip().lower()

# 2. Handle the Coffee category
if navigation == 'coffee':
    order = input("What kind of coffee do you want? (Black Coffee, White Coffee, etc.): ").strip()
    
    # Check if the item actually exists in our dictionary
    if order in coffee_products:
        price = coffee_products[order]
        print(f"The price of {order} is: {price}")
    else:
        print("Sorry, we don't have that specific coffee on the menu.")

# 3. Handle Soft Drinks
elif navigation == 'drinks':
    order = input("What kind of soft drink do you want?(CoCo Cola, Fanta, Mountain Dew): ").strip()
    if order in soft_drinks:
        print(f"The price of {order} is: {soft_drinks[order]}")
    else:
        print("Sorry, we don't have that drink.")

# 4. Handle Sweets
elif navigation == 'sweets':
    order = input("What sweet item do you want?(Chocolate Cake, Strawberry, Pastery): ").strip().lower()
    if order in sweet_items:
        print(f"The price of {order} is: {sweet_items[order]}")
    else:
        print("Sorry, we don't have that sweet item.")

else:
    print("Invalid category selected.")