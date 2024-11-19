# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list={
    "Name":[],
    "Price":[],
    "Quantity":[],
    "Item Cost":[]
}
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    print(menu_items)
    # Get the customer's input
    menu_category = input("Type menu number: ")
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_category_sub=input("Type menu number: ")
            # 3. Check if the customer typed a number
            if menu_category_sub.isdigit():
            # Convert the menu selection to an integer
                menu_category_sub=int(menu_category_sub)
                # 4. Check if the menu selection is in the menu items
                if (menu_category_sub) in menu_items.keys():
                    # Store the item name as a variable
                    menu_category_sub_name = menu_items[menu_category_sub]["Item name"]
                    #Store it item price as a variable
                    menu_category_sub_price=menu_items[menu_category_sub]["Price"]
                    print(f"You selected {menu_category_sub_name}")
                    # Ask the customer for the quantity of the menu item
                    menu_category_sub_quantity=input(f"How many {menu_category_sub_name} do you want? ")
                    # Check if the quantity is a number, default to 1 if not
                    if menu_category_sub_quantity.isdigit():
                        # Add the item name, price, and quantity to the order list
                        order_list["Name"].append(menu_category_sub_name)
                        order_list["Price"].append(menu_category_sub_price)
                        order_list["Quantity"].append(menu_category_sub_quantity)                       
                    else:
                        # Tell the customer that their input isn't valid 
                        print(f"The quantity of {menu_category_sub_name} was not valid.  As a result, your quantity is assumed to be 1.")
                        menu_category_sub_quantity=1 #default to 1
                        # Add the item name, price, and quantity to the order list
                        order_list["Name"].append(menu_category_sub_name)
                        order_list["Price"].append(menu_category_sub_price)
                        order_list["Quantity"].append(menu_category_sub_quantity)
                    print(order_list)          
                # Tell the customer they didn't select a menu option
                else:
                    print(f"{menu_category_sub_name} is not a valid member of {menu_category_name}")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
        break
    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
    # 5. Check the customer's input
    if(keep_ordering=="y"):
    # Keep ordering
        place_order = True
    else:
    # Exit the keep ordering question loop 
        place_order = False

# Complete the order
# Since the customer decided to stop ordering, thank them for
# their order
# Print out the customer's order
print("\nThank you for your order.  This is what we are preparing for you.\n")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list,
item_cost_lc=[order_list["Price"][j]*int(order_list["Quantity"][j]) for j in range(len(order_list["Name"]))]
order_list["Item Cost"]=item_cost_lc
# Uncomment the following line to check the structure of the order
print(order_list,"\n")

print("Item name                 | Price  | Quantity | Item Cost")
print("--------------------------|--------|----------|-----------")
# 6. Loop through the items in the customer's order
# 7. Store the dictionary items as variables
for y in range(len(order_list["Name"])):
     # 8. Calculate the number of spaces for formatted printing
    num_name_spaces=26-len(order_list["Name"][y])
    num_price_spaces=6-len(str(order_list["Price"][y]))
    num_quantity_spaces=9-len(str(order_list["Quantity"][y]))
    # 9. Create space strings
    spaces_name=" " * num_name_spaces
    spaces_price=" " * num_price_spaces
    spaces_quantity=" " * num_quantity_spaces
    # 10. Print the item name, price, and quantity, and item cost
    print(f"{order_list['Name'][y]}{spaces_name}| ${order_list['Price'][y]}{spaces_price}| {order_list['Quantity'][y]}{spaces_quantity}| ${order_list['Item Cost'][y]}")
#print out total for whole order
# and print the prices.
print(f"\n\nOrder Total                                     ${sum(order_list['Item Cost'])}\n\n\nWe strive for excellent service at variety food truck.\nPlease go to www.varietyfoodtruck.com to fill out a\nbrief survey and receive a coupon for a free drink on your\nnext visit.\n\nThank you and have a great day!")
   