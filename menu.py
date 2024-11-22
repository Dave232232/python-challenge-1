# Menu dictionary
#imports
import random
from datetime import datetime  #from AI overview in google search.  Also used on line 211
#code
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
order_list=[]
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
    menu_selection = input("Type menu number: ")
    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_selection_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selection_name].items():
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
            menu_selection=input("Type menu number: ")
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
            # Convert the menu selection to an integer
                menu_selection=int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                if (menu_selection) in menu_items.keys():
                    # Store the item name as a variable
                    menu_selection_sub_name = menu_items[menu_selection]["Item name"]
                    #Store it item price as a variable
                    menu_selection_sub_price=menu_items[menu_selection]["Price"]
                    print(f"You selected {menu_selection_sub_name}")
                    # Ask the customer for the quantity of the menu item
                    quantity=input(f"How many {menu_selection_sub_name} do you want? ")
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        #convert the quantity to an integer
                        quantity=int(quantity)
                        # Add the item name, price, and quantity to the order list
                        order_list.append({"Item name":menu_selection_sub_name,
                                          "Price":float(menu_selection_sub_price),
                                          "Quantity":int(quantity)})   
                    else:
                        # Tell the customer that their input isn't valid 
                        print(f"The quantity of {menu_selection_sub_name} was not valid.  As a result, your quantity is assumed to be 1.")
                        quantity=1 #default to 1
                        # Add the item name, price, and quantity to the order list
                        order_list.append({"Item name":menu_selection_sub_name,
                                          "Price":float(menu_selection_sub_price),
                                          "Quantity":int(quantity)}) 
                else:
                      # Tell the customer they didn't select a menu option
                      print(f"You did not input a valid member of {menu_selection_name}") 
            # Tell the customer they didn't select a menu option
            else:
                  print(f"You did not input a valid member of {menu_selection_name}")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    # 5. Check the customer's input
    #converting the case of keep ordering before the check as indicated in the instructions but why 
    match(keep_ordering.lower()):
        case "y":
            #continue to ask for more items
            place_order= True
        case "n":
            #exit the the ordering question loop
            place_order=False
        case _:
            #instructions have asking again if like to keep ordering but do not specify what happens is something other than y or n is put in.  This allows a retry and then exits order loop if still not y or n.
            retry_counter=0
            while keep_ordering not in["y","Y","n","N"] and retry_counter<=1:
                            retry_counter=retry_counter+1
                            print("Please try again using Y for \"yes\" or N for \"No\"")
                            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
                            place_order=True
            match(keep_ordering.lower()):
                case "y":
                    #continue to ask for more items
                    place_order= True
                case "n":
                    #exit the the ordering question loop
                    place_order=False
                case _:
                    keep_ordering="n"
                    #exit the the ordering question loop
                    place_order=False
# Complete the order
# Since the customer decided to stop ordering, thank them for
# their order
# Print out the customer's order
print("\nThank you for your order.  This is what we are preparing for you.\n")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list,
item_cost_lc=[order_list[j]["Price"]*order_list[j]["Quantity"] for j in range(len(order_list))]
# Uncomment the following line to check the structure of the order
print(order_list,"\n")

print(f"variety food truck\nOrder #: {random.randint(1,1000)}\nDate: {datetime.now()}\n")
print("Item name                 | Price  | Quantity | Item Cost")
print("--------------------------|--------|----------|-----------")
# 6. Loop through the items in the customer's order
# 7. Store the dictionary items as variables
for y in range(len(order_list)):
    #create item_name, price, and quantity variables from order_list
    item_name=order_list[y]["Item name"]
    price=order_list[y]["Price"]
    quantity=order_list[y]["Quantity"]
    # 8. Calculate the number of spaces for formatted printing
    num_name_spaces=26-len(item_name)
    num_price_spaces=6-len(str(price))
    num_quantity_spaces=9-len(str(quantity))
    # 9. Create space strings
    spaces_name=" " * num_name_spaces
    spaces_price=" " * num_price_spaces
    spaces_quantity=" " * num_quantity_spaces
    # 10. Print the item name, price, and quantity, and item cost
    print(f"{item_name}{spaces_name}| ${price}{spaces_price}| {quantity}{spaces_quantity}| ${item_cost_lc[y]:.2f}")
#print out total for whole order
# and print the prices.  Sum done below, list comprehension on line 187 so could add onto receipt.
print(f"\n\nOrder Total                                     ${sum(item_cost_lc):.2f}\n\n\nWe strive for excellent service at variety food truck.\nPlease fill out our survey and receive a coupon for a\nfree drink on your next order by:\nGoing to varietyfoodtruck.com/survey and entering your\n     order number at the top of this receipt\nOR scanning the QR code on this receipt\nOR scanning the QR code on the front of the truck by the\n    menu and entering your order number at the top this\n    receipt.\n\nThank you and have a great day!")
   