# This function takes a text file as input
def Adding_function(textfile):
    # Open the text file in read mode
    with open(textfile, 'r') as file:
        # Initialize an empty list to store the contents of the text file
        list_ = []
        # Loop through each line in the text file
        for i in file:
            # Strip the line of any leading or trailing whitespace
            file_strip = i.strip()
            # Split the line into a list using a comma as a delimiter
            file_split = file_strip.split(',')
            # Append the list to the overall list
            list_.append(file_split)
        # Return the overall list of lists containing the contents of the text file
        return list_                
# This function does not take any input parameters
def adding_function():
    # Open the laptopdetails.txt file in read mode
    with open('laptop.txt', 'r') as file:
        # Initialize an empty list to store the contents of the text file
        list_ = []
        # Loop through each line in the text file
        for i in file:
            # Strip the line of any leading or trailing whitespace
            file_strip = i.strip()
            # Split the line into a list using a comma as a delimiter
            file_split = file_strip.split(',')
            # Append the list to the overall list
            list_.append(file_split)
        # Initialize the variable 'Addmore' to "y"
        Addmore = "y"
        # Loop until the user enters "n" to indicate they are finished shopping and the billing part can be executed
        while Addmore == "y":
            # Display a table of laptop details
            print("-------------------------------------------------------------------------------------------------------------------------")
            print("|ID.   |  Laptop Name    |   Brand Name  |    Price    |    Quantity    |     Processor     |       Graphicard       |")
            print("-------------------------------------------------------------------------------------------------------------------------")
            # Display the contents of the laptopdetails.txt file in tabular form
            with open("laptop.txt", "r") as filedisplay:
                for line in filedisplay:
                    print("  "+line.replace(",", "\t       "))
                    print("-------------------------------------------------------------------------------------------------------------------------")
                print("\n")
    
                                
                    
