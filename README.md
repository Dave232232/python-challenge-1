# python-challenge-1
## Description
This repository includes 1 file: menu.py in addition to this README.  In menu.py, a food truck menu for **variety food truck** is printed to the terminal.  The menu is stored as a dictionary in menu.py. The user is then asked to select a menu category which leads to a sub menu of individual items and prices.  From that sub-menu, the user selects an item, inputs the quantity, an order list is updated, and asks if more items are to be ordered.  If more items are wanted, the process is repeated until no more items are wanted.  When no more items are wanted the code prints out a receipt as an order summary that totals the cost for each item type and the whole order.
## Module Dependencies
- random: to generate an order number that is put on the receipt
- datetime: to place a order date and time on the receipt
## Python Version
  3.12.7
## Error Handling
- When a menu selection is made or quantity entered, checks are done for type and letter vs. number.
- When asked to continue ordering, checks are done to ensure proper input.
- If repeated improper inputs to continue ordering are received, the order is ended.
- If a quantity is not entered it is assumed to be 1.
