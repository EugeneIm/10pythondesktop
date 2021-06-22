import re
import sys
from os import write

def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    try: 
        if re.search("([0-9]{8})", order_num) is None:
            raise ValueError("Order Number is invalid")
        else:
            print('Valid Order Number') #check
        with open("book_order_utils.txt", "a") as f:
            f.write("BOOK ORDER" "\n" "Order number: " + order_num + "\n")

        if re.search("([a-zA-Z\s]$)", title) is None:
            raise ValueError("Title is invalid")
        else:
            print('Valid Title') #check
        with open("book_order_utils.txt", "a") as f:
            f.write("Book Title: " + title + "\n")

        if re.search("([A-Z\s\"'\"])", author) is None:
            raise ValueError("Author is invalid")
        else:
            print('Valid Author Name') #check
        with open("book_order_utils.txt", "a") as f:
            f.write("Author Name: " + author + "\n")
        
        if re.search("([0-9]{4,20})", isbn) is None:
            raise TypeError("ISBN is invalid")
        else:
            print("ISBN is valid")
        with open("book_order_utils.txt", "a") as f:
            f.write("Book ISBN: " + isbn + "\n")
        
        if re.search("(([0-9]){4})", year) is None:
            raise ValueError("Year is invalid")
        else:
            print('Valid Year')
        with open("book_order_utils.txt", "a") as f:
            f.write("Year Published: " + year + "\n")
        
        if re.search("^([0-9]\d*)$", quantity) is None:
            raise TypeError("Quantity must be an integer")
        else:
            print('Valid Quantity')
        with open("book_order_utils.txt", "a") as f:
            f.write("Total Quantity: " + quantity + "\n")
        
        if re.search("^([0-9][0-9]?|1000)$", cost) is None:
            raise ValueError("Quantity is invalid")
        else:
            print('Valid Quantity Number')
        with open("book_order_utils.txt", "a") as f:
            f.write("Cost in dollars: " + cost + "\n")
    finally:
        print('Order details finished')



validate_book_order_details('12345678', "harry potter", "JK Rowling", "1234", "2001", "1", "50")

'''
insert doc string of explanation
'''


def calculate_per_book_cost(cost, quantity):
        try:
                cost = float(input('Enter the book cost: '))
                quantity = input('Enter the quantity of books: ')
                book_cost = int(cost)/int(quantity)
                book_cost_format = "{:.2f}".format(book_cost)
                if quantity == 0:
                        raise ZeroDivisionError('Cannot divide by 0')
                else:
                        print(book_cost_format)
                with open('book_cost.txt', 'a') as b:
                        b.write('Cost per book is :' + book_cost_format + "\n")
        finally:
                print('Costs have been calculated')

'''
insert doc string of explanation
'''


calculate_per_book_cost(0, 0)

def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    try: 
        if re.search("^([a-zA-Z]{1,8}\.txt)$", filename) is None:
                filename = input("Invalid file name, please enter a valid name: ")
        with open(filename, 'w') as f:    
                f.write(filename + "\n")
        if re.search("([a-zA-Z\s]$)", title) is None:
            raise ValueError("Title is invalid")
        else:
            print('Valid Title') #check
        with open(filename, "a") as f:
            f.write("Book Title: " + title + "\n")

        if re.search("([A-Z\s\"'\"])", author) is None:
            raise ValueError("Author is invalid")
        else:
            print('Valid Author Name') #check
        with open(filename, "a") as f:
            f.write("Author Name: " + author + "\n")
        
        if re.search("([0-9]{4,20})", isbn) is None:
            raise TypeError("ISBN is invalid")
        else:
            print("ISBN is valid")
        with open(filename, "a") as f:
            f.write("Book ISBN: " + isbn + "\n")
        
        if re.search("(([0-9]){4})", year) is None:
            raise ValueError("Year is invalid")
        else:
            print('Valid Year')
        with open(filename, "a") as f:
            f.write("Year Published: " + year + "\n")
        
        if re.search("^([0-9]\d*)$", quantity) is None:
            raise TypeError("Quantity must be an integer")
        else:
            print('Valid Quantity')
        with open(filename, "a") as f:
            f.write("Total Quantity: " + quantity + "\n")
        
        if re.search("1[0-9]?[0-9]|2[0-9]?[0-9]|3[0-9]?[0-9]|4[0-9]?[0-9]|5[0-9]?[0-9]|6[0-9]?[0-9]|7[0-9]?[0-9]|8[0-9]?[0-9]|9[0-9]?[0-9]", cost) is None:
            raise ValueError("Cost is invalid")
        else:
            print('Valid Price')
        with open(filename, "a") as f:
            f.write("Cost in dollars: " + cost + "\n")

        unit_cost = float(int(cost))/int(quantity)
        with open(filename, "a") as f:
                f.write("Unit Cost in dollars: " + str(unit_cost) + "\n")
    finally:
        print('Order details finished')

'''
insert doc string of explanation
'''



write_book_order_details(filename="asdfasdfadf", title="New Bible", author="Unknown", isbn="69420", year="0000", quantity="2", cost="50", unit_cost="25" )
#for some reason it doesn't matter what I put in for the "unit_cost" as the parameter, it just calculates the unit_cost in the .txt file. 