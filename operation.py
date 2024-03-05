from datetime import datetime
from write import *
Datetime_ = datetime.now()
datetime_ = Datetime_.strftime("%Y-%m-%d_%H-%M-%S")
def welcome():
    #welcome msg
    print("\n")
    print("-----------------------------------------------------------------------------------------------")
    print("\n")
    print("                                           WELCOME TO STORE                                    ")
    print("\n")
    print("-----------------------------------------------------------------------------------------------")
    print("\n")
    # Available Choices
    print("1. ADD TO STOCK")
    print("2. MAKE A SELL")
    print("3. EXIT")
    print("\n")
    print("-------------------------------------------------------------------------------------------------")
    print("\n")
    
    print("What would you like to do")
    choices = input("select the choices (1-3): ")
    print("\n")
    return choices
def modify_quantity_adding(innerlist,quantity,info_added):
    
    new_quantity = (int(innerlist[4]) + quantity)

   
    innerlist[4] = new_quantity

    
    product_name = innerlist[1]
    brand = innerlist[2] 

    # Get the quantity and price per unit of the product purchased
    product_quantity = (quantity)
    prodcut_price_per_unit = innerlist[3]

    # Calculate the total price of the product purchased by multiplying the quantity by the price per unit
    selected_prodcut_price = innerlist[3].replace("$",'')
    total_price = (int(product_quantity) * int(selected_prodcut_price))

    # Add the product information to the info_added list
    info_added.append([product_name, prodcut_price_per_unit,selected_prodcut_price, product_quantity, total_price,brand])
def examine_selling(ID,list_,info_added,hi):
    model_num = False
    for innerlist in list_:
    
        if str(ID) == innerlist[0]:
            re_enter = True
            
            model_num = True
            while re_enter == True:
                
                while True:
                    try:
                        quantity = int(input("Enter the quantity: "))
                        if quantity <= 0:
                            print("Invalid input. Please enter a positive number.")
                            continue
                        print("\n")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            ##increase the quantity of item selected by user in list........ 
            
                re_enter = update_quantity_selling(innerlist,quantity,info_added)
            
            updatedata('laptopdetails.txt',list_)
            ##asking user if they want to add more items......
            while True:
                try:
                    hi = input("Do you want to add more items? (y/n): ")
                    print("\n")
                    hi = hi.lower()
                    if hi != "y" and hi != "n":
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter either 'y' or 'n'.")
    return hi,model_num
    # return user's response and boolean flag indicating whether SN number was found or not             
def update_quantity_selling(innerlist,quantity,info_added,):
    # Calculate the new quantity of the product purchased by subracting the quantity purchased to the current quantity in stock
    if quantity<=(int(innerlist[4])):
        new_quantity = (int(innerlist[4]) - quantity)
        innerlist[4] = new_quantity      
        product_name = innerlist[1]
        brand = innerlist[2] 
        product_quantity = (quantity)
        prodcut_price_per_unit = innerlist[3]
     
        selected_prodcut_price = innerlist[3].replace("$",'')
        total_price = (int(product_quantity) * int(selected_prodcut_price))
        
        info_added.append([product_name, prodcut_price_per_unit,selected_prodcut_price, product_quantity, total_price,brand])
        re_enter = False
    else:
        re_enter = True
        print("WE DON'T HAVE ENOUGH QUANTITY.. PLEASE REENTER THE QUANTITY")
    return re_enter
def determining(info_added,choices):
   
    while True:
        try:
            print("+===============================================================================================+")
            print("                                    ENTER YOUR DETAILS FOR BILLING                               ")
            print("+===============================================================================================+")
            print("\n")
            customer_name = input("Enter your name: ")
            print("\n")
            if not customer_name:
                raise ValueError("Name cannot be empty")
            contact = input("Enter your phone number: ")
            print("\n")
            if not contact:
                raise ValueError("contact cannot be empty")
            break
        except ValueError as err:
            print(f"Invalid input: {err}")
    # Initialize total variable to 0 and print the list of items purchased
    total = 0

    # Create empty lists to store the names and brands of the purchased laptops
    laptop_names = []
    laptop_brand = []

    # Calculate the total price of all items purchased by adding up the price of each item multiplied by its quantity
    for laptops in info_added:
        price = laptops[2]
        total += (int(price)* int(laptops[3]))
        laptopn = laptops[1]
        brand = laptops[5]
        laptop_names.append(laptopn)
        laptop_brand.append(brand)

    # Calculate the VAT amount and total price with VAT included
    VATAMT = (13/100)* total
    grand_with_vat = (total + ((13 * total)/100))

    if choices == "1":
        shipping_cost = 0
    else:
        shipping_cost = 100

    
    TotalAmount = (grand_with_vat)+ (shipping_cost)

    
    return contact,customer_name,TotalAmount,total,VATAMT
def examine_stock(ID,list_,info_added,hi):
    model_num = False
    for innerlist in list_:
   
        if str(ID) == innerlist[0] :
           
            model_num = True
            # prompt user to enter quantity
            while True:
                try:
                    quantity = int(input("Enter the quantity for the selected laptop: "))
                    if quantity <= 0:
                        print("Invalid input. Please enter a positive number.")
                        continue
                    print("\n")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.") 
            # call function to add quantity to info_added list
            modify_quantity_adding(innerlist,quantity,info_added)

            
            updatedata('laptopdetails.txt',list_)
            ##asking user if they want to add more items......
            while True:
                try:
                    hi = input("Do you want to add more items? (y/n): ")
                    print("\n")
                    hi = hi.lower()
                    if hi != "y" and hi != "n":
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter either 'y' or 'n'.")
    
    return hi,model_num
