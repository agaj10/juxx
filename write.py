from datetime import datetime
Datetime_ = datetime.now()
datetime_ = Datetime_.strftime("%Y-%m-%d_%H-%M-%S")
#for updating the data in the textfile...
def updatedata (textfile,mainlist):
    with open(textfile, 'w') as file:
        # Loop through each list in 'mainlist'
        for innerlist in mainlist:
            # Write the elements of each list to the file, separated by commas and with a 
            file.write(str((innerlist[0])) + "," + str((innerlist[1])) +  ","+ str((innerlist[2])) +  "," +str((innerlist[3])) +  "," +str((innerlist[4]))  +  ","+ str((innerlist[5])) +  "," + str((innerlist[6])) + "\n")
def billtextfile(choices,customer_name,info_added,TotalAmount,total,VATAMT,about_bill):
    if choices == "2":
            shipments = "Including shipments charge"
            ship = "Shipments charge = $200"
    else:
        shipments = ""    
        ship= "" 
    # Create a filename based on 'customer_name' and 'customerphone'
    filename = f"{datetime_}{customer_name}.txt"
    # Open the file with the filename in write mode using 'with' statement
    with open(filename, 'w') as file:
        file.write("\n")
        file.write("\n")
        file.write("\t==============================================================================================\n")
        file.write(f"\t {customer_name}                                                    {Datetime_}           \n")
        file.write(f"\t                                        {about_bill}                                         \n")
        file.write("\n")
        file.write("\t==============================================================================================\n")
        file.write("\t----------------------------------------------------------------------------------------------\n") 
        file.write("\t|S.N.   |  Brand Name    | Laptop Name     |    Price    |    quantity    |    Totalprice \n")
        file.write("\t----------------------------------------------------------------------------------------------\n")
        a=1
        # Loop through each line in 'info_added'
        for line in info_added:
            file.write(f"\t {a}           {line[5]}        \t {line[0] }          {line[1]}   \t\t     {line[3]}   \t\t\t   {line[4]}  \n")
            file.write("\t----------------------------------------------------------------------------------------------\n")
            file.write("\n")
            a+=1
        # Write the total, VAT charge, and VAT amount to the file
        file.write(f"\t                                                                  Net Amout = ${total}\n   ") 
        file.write("\t                                                                  VAT charge = 13%    \n  ")
        file.write(f"\t                                                                  Vat Amount = ${VATAMT} \n")
        file.write(f"\t                                                                  {ship}  \n")
        file.write(f"\t{customer_name}. your  Total Amount {shipments }is ${TotalAmount}. \n")
        file.write("\t                                 THANK YOU FOR CHOOSING US...                                ")
        file.write("\n")
        file.write("\t==============================================================================================\n")
        file.write("\n")
        file.write("\n")
def display_laptops():
    print("-------------------------------------------------------------------------------------------------------------------------") 
    print("|ID.      |  Laptop Name    |   Brand Name  |    Price    |    Quantity    |     Processor     |       Graphicard       |")
    print("-------------------------------------------------------------------------------------------------------------------------")
    # Opening the file containing laptop details and displaying the items
    with open("laptopdetails.txt", "r") as filedisplay:
        for line in filedisplay:
             # Replacing comma separators with tab spaces for better display of laptop details
            print("  "+line.replace(",", "\t       "))
            print("-------------------------------------------------------------------------------------------------------------------------")
        print("\n")
    # Prompting the user to enter the SN number of the laptop they want to add or sell
    sn_number = input("Enter the S.N number for the laptop you want to add: ")
    print("\n")
    return sn_number
def displaybill(choices,customer_name,info_added,TotalAmount,total,VATAMT,about_bill):
        if choices == "2":
            shipments = "including shipments charge"
            ship = "shipments charge = $100"
        else:
            shipments = ""    
            ship= ""
        print("\n")
        print("\n")
        # Print a header with the customer name and the current date and time
        print("\t-----------------------------------------------------------------------------------------------")
        print(f"\t                                                                        {Datetime_}           ")
        print(f"\t                                {about_bill}                                       ")
        print("                                                                                            ")
        print("\t----------------------------------------------------------------------------------------------")
        print(f"{customer_name}")
        # Print a table header for the products purchased
        print("\t----------------------------------------------------------------------------------------------") 
        print("\t|S.N.   |  Brand Name    | Laptop Name     |    Price    |    quantity    |    Totalprice ")
        print("\t----------------------------------------------------------------------------------------------")
        # Iterate over the products purchased and print each one in a table row
        a=1
        for line in info_added:
            print(f"\t {a}           {line[5]}   \t   {line[0] } \t\t{line[1]}\t\t{line[3]} \t\t  {line[4]}  ")
            print("\t----------------------------------------------------------------------------------------------")
            print("\n")
            a+=1
        # Print the net amount, VAT charge, and VAT amount and other information at the bottom of the bill..
        print(f"\t                                                                  TotalAmount= ${total}   ") 
        print("\t                                                                   VAT = 13%     ")
        print(f"\t                                                                  Vat Amount = ${VATAMT}  ")
        print(f"\t                                                                 {ship}  ")
        print("\n")
        print(f"\t\t\t\t {customer_name}, your Grand total {shipments }is ${TotalAmount}. ")
        print("\n")
        print("\t                                 THANK YOU FOR CHOOSING US...                                 ")
        print("\n")
        print("\t==============================================================================================")
        print("\n")
        print("\n")
             