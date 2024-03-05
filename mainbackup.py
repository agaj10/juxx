while True:
    print("===============================================================================================")
    print("                                           WELCOME TO STORE                                      ")
    print("===============================================================================================")
    print("1. ADD STOCK")
    print("2. SELL")
    print("3. EXIT")
    print("===============================================================================================")
    choices = input("select the choices (1-3): ")
    if choices == "1":
        with open('laptop.txt', 'r') as file:
            ## declaring empty list to store text file as 2D list.............
            list = []
            for i in file:
                file_strip = i.strip()
                file_split = file_strip.split(',')
                list.append(file_split)
            ##declaring empty list for adding details of a items that user select when asked to enter SN: ........
            info_added = []
            hi = "y"   
            ##loop for displaying until user selects (n) which means they finished shopping and billing part is excueted......... 
            while hi == "y":
                print("-------------------------------------------------------------------------------------------------------------------------") 
                print("|S.N.   |  Laptop Name    |   Company Name  |    Price    |    quantity    |     processor     |       Graphicard       |")
                print("-------------------------------------------------------------------------------------------------------------------------")
                ##to display item stored in text file...............
                with open("laptop.txt", "r") as filedisplay:
                    for line in filedisplay:
                        print("  "+line.replace(",", "\t       "))
                        print("-------------------------------------------------------------------------------------------------------------------------")
                    print("\n")
                #asking user to enter particular SN: to buy the item .......
                id = input("Enter the S.N number for the laptop you want to add: ")
                model_num = False
                #looking into the list where we stored the text file to check the particular SN: entered by the user...........
                for innerlist in list:
                    if str(id) == innerlist[0]:
                        print(innerlist)
                        model_num = True
                        #asking user to enter the quantiy of the iteam selected.......
                        quantity = int(input("enter the quantity: "))
                        ##increase the quantity of item selected by user in list........ 
                        latest_quantity= (int(innerlist[4]) + quantity)
                        innerlist[4] = latest_quantity
                        product_name = innerlist[1]
                        product_quantity = (quantity)
                        price_per_product = innerlist[3]
                        choosed_product_amount = innerlist[3].replace("$",'')
                        total_price = (int(product_quantity) * int(choosed_product_amount))
                        info_added.append([product_name, price_per_product,choosed_product_amount, product_quantity, total_price])
                        ##writing the new data in the textfile for displaying after adding stock.........
                        with open('laptop.txt', 'w') as file:
                            for innerlist in list:
                                file.write(str((innerlist[0])) + "," + str((innerlist[1])) +  ","+ str((innerlist[2])) +  "," +str((innerlist[3])) +  "," +str((innerlist[4]))  +  ","+ str((innerlist[5])) +  "," + str((innerlist[6])) + "\n")
                        ##asking user if they want to add more items......
                        hi = (input("do you want to add more items y/n: "))
                        hi = hi.lower()
                if model_num == False:
                    print("model not found")
            #for billing
            customer_name =  input("enter your name: ")
            customer_contact =  input("enter your number: ")
            total = 0
            print(info_added)
            for laptops in info_added:
                price = laptops[2]
                total += (int(price)* int(laptops[3]))
            total_including_vat = (total + ((13 * total)/100))
            TotalAmount = (total_including_vat + 20)
            print("\n")
            print("\n")
            print("============================================================================")
            print("\n")
            print("                                  YOUR BILL                                 ")
            print("\n")
            print("============================================================================")
            print("----------------------------------------------------------------------------") 
            print("|ID   |  Laptop Name     |    Price    |    quantity    |    Totalprice     ")
            print("----------------------------------------------------------------------------")
            d=1
            for line in info_added:
                print(f"  {d}        {line[0]}           {line[1] }            {line[3]}\t\t{line[4]} ")
                print("----------------------------------------------------------------------------")
                print("\n")
                d+=1
            print("\t\t\t\t\t\t shipment charge = $20 ")
            print("\t\t\t\t\t\t VAT charge = 13% ")
            print("\n")
            print(f"\tMRS/MISS {customer_name}. your total charge for overall purchues including shipment charge is ${TotalAmount}. ")
            print("\n")
            print("                                                 THANK YOU FOR CHOOSING US...                                             ")
            print("\n")
            print("                                    For any Query contact us on : 98XXXXXXX ,027XXXXXXX                                   ")
            print("==========================================================================================================================")
            print("\n")
            print("\n")  
            break
    elif choices == "2":
         with open('laptop.txt', 'r') as file:
            ## declaring empty list to store text file as 2D list.............
            list = []
            for i in file:
                file_strip = i.strip()
                file_split = file_strip.split(',')
                list.append(file_split)
            ##declaring empty list for adding details of a items that user select when asked to enter SN: ........
            info_added = []
            hi = "y"   
            ##loop for displaying until user selects (n) which means they finished shopping and billing part is excueted......... 
            while hi == "y":
                print("-------------------------------------------------------------------------------------------------------------------------") 
                print("|ID     |  Laptop Name    |   Company Name  |    Price    |    quantity    |     processor     |       Graphicard       |")
                print("-------------------------------------------------------------------------------------------------------------------------")
                ##to display item stored in text file...............
                with open("laptop.txt", "r") as filedisplay:
                    for line in filedisplay:
                        print("  "+line.replace(",", "\t       "))
                        print("-------------------------------------------------------------------------------------------------------------------------")
                    print("\n")
                #asking user to enter particular SN: to buy the item .......
                id = input("Enter the S.N number for the laptop you want to add: ")
                model_num = False
                #looking into the list where we stored the text file to check the particular SN: entered by the user...........
                for innerlist in list:
                    if str(id) == innerlist[0]:
                        print(innerlist)
                        model_num = True
                        #asking user to enter the quantiy of the iteam selected.......
                        quantity = int(input("enter the quantity: "))
                        ##increase the quantity of item selected by user in list........ 
                        latest_quantity= (int(innerlist[4]) + quantity)
                        innerlist[4] = latest_quantity
                        product_name = innerlist[1]
                        product_quantity = (quantity)
                        price_per_product = innerlist[3]
                        choosed_product_amount = innerlist[3].replace("$",'')
                        total_price = (int(product_quantity) * int(choosed_product_amount))
                        info_added.append([product_name, price_per_product,choosed_product_amount, product_quantity, total_price])
                        print(info_added)
                        ##writing the new data in the textfile for displaying after adding stock.........
                        with open('laptop.txt', 'w') as file:
                            for innerlist in list:
                                file.write(str((innerlist[0])) + "," + str((innerlist[1])) +  ","+ str((innerlist[2])) +  "," +str((innerlist[3])) +  "," +str((innerlist[4]))  +  ","+ str((innerlist[5])) +  "," + str((innerlist[6])) + "\n")
                        ##asking user if they want to add more items......
                        hi = (input("do you want to add more items y/n: "))
                        hi = hi.lower()
                if model_num == False:
                    print("model not found")
            #for billing
            customer_name =  input("enter your name: ")
            customer_contact =  input("enter your number: ")
            total = 0
            print(info_added)
            for laptops in info_added:
                price = laptops[2]
                total += (int(price)* int(laptops[3]))
            total_including_vat = (total + ((13 * total)/100))
            TotalAmount = (total_including_vat + 20)
            print("\n")
            print("\n")
            print("============================================================================")
            print("\n")
            print("                                  YOUR BILL                                 ")
            print("\n")
            print("============================================================================")
            print("----------------------------------------------------------------------------") 
            print("|S.N.   |  Laptop Name     |    Price    |    quantity    |    Totalprice   ")
            print("----------------------------------------------------------------------------")
            a=1
            for line in info_added:
                print(f"  {a}        {line[0]}           {line[1] }            {line[3]}\t\t{line[4]} ")
                print("----------------------------------------------------------------------------")
                print("\n")
                a+=1
            print("\t\t\t\t\t\t shipment charge = $20 ")
            print("\t\t\t\t\t\t VAT charge = 13% ")
            print("\n")
            print(f"\tMRS/MISS {customer_name}. your total charge for overall purchues including shipment charge is ${TotalAmount}. ")
            print("\n")
            print("                                                 THANK YOU FOR CHOOSING US...                                             ")
            print("\n")
            print("                                    For any Query contact us on : 98XXXXXXX ,027XXXXXXX                                   ")
            print("==========================================================================================================================")
            print("\n")
            print("\n")
            break
    elif choices == "3":
        break