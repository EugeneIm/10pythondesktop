'''
Now create a Python script called book_order.py and create and call your main function.

Your main function should do the following:

•	Verify there are exactly 8 command-line arguments
•	Get the following from the command-line (in this order):
o	order_num
o	title
o	author
o	isbn
o	year
o	quantity
o	cost
Note that you need to import sys to retrieve the command line arguments
If the value of your command line argument includes spaces, you need to put quotes around it when your script is called.
•	Call the validate_book_order_details function in the book_order_utils module to validate your command-line arguments.
o	Note: Make sure to import your book_order_utils module
•	Call the calculate_per_book_cost function in the book_order_utils module to get the unit cost of each book.
•	Call the write_book_order_details function in the book_order_utils module to write the book order to file.

Add exception handling to your main function. Put the calls to the functions in book_order_utils above into a try block and add exception handlers for the following exceptions:

•	ValueError – Print “Value Error: “ then the message from the ValueError exception.
•	TypeError – Print “Type Error: “ then the message from the TypeError exception.
•	ZeroDivisionError – Print “No Books in Order”
'''

print('hello world')