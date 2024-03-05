from read import *
from write import *
from operation import *
# Introducing required modules
# The main loop that shows the user a list_ of alternatives
while True:
    # Using welcome() to display choices to the user1
    
    choices = welcome()
   # including_function() is used to load a file and add items to a cart if the user chooses option 1 in the drop-down menu.
    if choices == "1":
        list_=adding_function('laptop.txt')
         # Declaring an empty list_ to store the details of items added to the cart
        info_added = []
        # welcomeing the loop that asks the user to add more items by setting the hi variable to "y
        hi = "y"
        # welcomeing the loop that asks the user to add more items by setting the hi variable to "y"
        while hi == "y":
           # Invoking the display_laptops() function to display the laptops that are available and ask the user for their SN
            id = display_laptops()
           # Invoking the examine_stock() function to verify the validity of the supplied SN and add the product to the shopping cart.
            hi, model_num = examine_stock(id, list_, info_added,hi)
            # Print an error message if the model cannot be found.
            if model_num == False:
                print("Laptop not found")
        # Compute the total cost, VAT, and overall cost of the items you've added to your cart.
        customer_phone, customer_name, TotalAmount, total, vatamt = determining(info_added,choices)
         # Recording the billing information in a file
        bill = "Organization  BILL"
        billtextfile(choices,customer_name,info_added, TotalAmount, total, vatamt,bill)
        # Displaying the billing details to the user
        displaybill(choices,customer_name, info_added, TotalAmount, total, vatamt,bill)
    # If the user selects option 2, the Selling_function() is called to load a file and remove items from the inventory
    elif choices == "2":
        list_= adding_function('laptop.txt')
        # Declaring an empty list__ to store the details of items sold
        info_added = []
        # Initializing the hi variable to "y" to enter the loop that prompts the user to sell more items
        hi = "y"
        # Loop that displays items and prompts the user to sell them until the user enters "n"
        while hi == "y":
            # Calling the display_laptops() function to show the available laptops and prompt the user to enter an SN
            id = display_laptops()
            # Calling the examine_selling() function to check if the entered SN is valid and remove the item from the inventory
            hi,model_num = examine_selling(id, list_, info_added,hi)
            # Print an error message if the model cannot be found.
            if model_num == False:
                print("laptop not found")
        # Calculating the total amount, VAT, and grand total of the items sold
        customer_phone, customer_name, TotalAmount, total, vatamt = determining(info_added,choices)
        # Writing the billing details to a file
        bill = "CUSTOMER BILL"
        billtextfile(choices,customer_name, info_added, TotalAmount, total, vatamt,bill)
        # Displaying the billing details to the user
        displaybill(choices,customer_name, info_added, TotalAmount, total, vatamt,bill)
    elif choices =="3":
        break
   