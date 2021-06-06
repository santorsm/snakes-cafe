# displays welcome message and menu
intro_and_menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(intro_and_menu)

# empty dictionary of menu items
menu_items = {
    "wings": 0,
    "cookies": 0,
    "spring rolls": 0,
    "salmon": 0,
    "steak": 0,
    "meal tornado": 0,
    "a literal garden": 0,
    "ice cream": 0,
    "cake": 0,
    "pie": 0,
    "coffee": 0,
    "tea": 0,
    "unicorn tears": 0,
}

# message prompt for customer order
order_prompt = """
***********************************
** What would you like to order? **
***********************************
"""

print(order_prompt)

# sets initial state of order to an empty string
customer_order = ""

# while loop allows user to continue ordering until 'quit' is entered
while customer_order != "quit":
    # while the customer hasn't entered 'quit' prompt for input
    # displays '> ' for input with tailing space & assigns value to variable
    customer_order = input("> ")
    # if 'quit' exit & bid a fond adeu
    if customer_order == "quit":
        print("Thank you for your business! We look forward to serving you again soon.")
        break
    # check to see if desired key is in dictionary
    elif customer_order in menu_items:
        # increment menu_item by 1 if customer_order in menu_item
        # https://www.kite.com/python/answers/how-to-increment-a-value-in-a-dictionary-in-python
        menu_items[customer_order] += 1
        if menu_items[customer_order] == 1:
            print(
                f"** {menu_items[customer_order]} order of {customer_order} has been added to your meal **"
            )
        else:
            print(
                f"** {menu_items[customer_order]} orders of {customer_order} have been added to your meal **"
            )
