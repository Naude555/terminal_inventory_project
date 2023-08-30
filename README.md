Shoe Inventory Management System
This Python program is designed to read data from the text file inventory.txt and perform various operations on the data to prepare it for presentation to your managers. The program is structured with a class named Shoe and several functions to handle different tasks related to shoe inventory management.

Getting Started
Clone this repository to your local machine.
Make sure you have Python installed (version 3.6 or higher).
Open the terminal and navigate to the repository's directory.
Files
inventory.py: Contains the main code for the Shoe Inventory Management System.
inventory.txt: This is the input text file containing shoe inventory data.
Class: Shoe
The Shoe class represents a shoe item and has the following attributes:

country
code
product
cost
quantity
The class defines the following methods:

get_cost(): Returns the cost of the shoe.
get_quantity(): Returns the quantity of the shoe.
__str__(): Returns a string representation of the shoe.
Functions
read_shoes_data()
This function reads data from the inventory.txt file and creates Shoe objects with the data. Each line in the file represents data to create one Shoe object. The function skips the first line and utilizes error handling with try-except.

capture_shoes()
Allows the user to capture data about a shoe and creates a Shoe object using the captured data. The created object is appended to the list of shoes.

view_all()
Iterates over the list of shoes and prints the details of each shoe using the __str__() method. Optional: The data can be organized in a tabulated format using the tabulate module.

re_stock()
Finds the shoe object with the lowest quantity (needing restocking), asks the user if they want to add a specific quantity of shoes, and updates the quantity. The updated quantity is also updated in the inventory.txt file.

search_shoe(code)
Searches for a shoe in the list using the provided shoe code and returns the corresponding Shoe object.

value_per_item()
Calculates and prints the total value for each item in the inventory using the formula: value = cost * quantity.

highest_qty()
Determines the product with the highest quantity and prints this shoe as available for sale.

main()
Creates a menu that allows the user to execute each of the above functions.

Running the Program
Execute the inventory.py script using the following command in your terminal:

bash
Copy code
python inventory.py
Follow the on-screen prompts to navigate through the different functionalities of the Shoe Inventory Management System.

Note
Make sure the inventory.txt file is in the same directory as the inventory.py script for the program to read data correctly.