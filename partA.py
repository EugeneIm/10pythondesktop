#def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    
print('hello world')


'''
This function will validate each of the order details, represented by the params. 
The table below describes the validation for each parameter and the type of exception that needs to be raised. 
You may use regex (or other means) to do the validation. Make sure you "import re" if you use regex. 

Order_num:
Validation: one or more int values. Both 1 and 0001 should be valid.
Exception: ValueError | Order Number is invalid

    if re.search(")

Title: 
Validation: one or more lower or uppercase letters or spaces.
Exceptions: ValueError | Title is invalid

    if re.search("([a-zA-Z\s]$, title) is None:
        raise ValueError("Title is invalid")
    else:
        continue

Author:
Validation: zero or more lower or uppercase letters, spaces or apostrophes. 
Exception: ValuError | Author is invalid
    if re.search(")

ISB:
Validation: must be between 4 and 20 digits, inclusive. 
Exception: TypeError | ISBN in invalid
    if re.search("[0-9]{4, 20}")

Year: 
Validation: Must be 4 digits EXACTLY
Exception: ValueError | Year is invalid


Quantity: 
Validation: Must be integers
Exception: TypeError | Quantity must be an integer


Cost:
Validation: Must be ebtween 0 and 1000, inclusive
Exception: ValueError | Quantity is invalid. 
'''

#def calculate_per_book_cost(cost, quantity):


#def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
