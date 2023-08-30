import os
from tabulate import tabulate


# Class definition
class Shoe:
    """
    Represents a shoe item in the inventory.
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Initializes a Shoe object with the provided attributes.

        Args:
            country (str): The country of origin for the shoe.
            code (str): The unique code for the shoe.
            product (str): The name of the shoe product.
            cost (float): The cost of the shoe.
            quantity (int): The quantity of the shoe in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        Returns the cost of the shoe.

        Returns:
            float: The cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoe in stock.

        Returns:
            int: The quantity of the shoe.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of the Shoe object.

        Returns:
            str: The string representation of the shoe.
        """
        return f"{self.product} ({self.code}): {self.quantity} available"


# Shoe list
shoe_list = []

# Filepath to inventory.txt uses the current python file running and looks in the directory
file_path = os.path.join(os.path.dirname(__file__), "inventory.txt")


# Functions
def read_shoes_data():
    """
    Reads shoe data from the inventory.txt file and populates the shoe_list.
    """
    # This function skips the header line and reads the shoe data from the file.
    # Each line is split into respective attributes, converted to the appropriate data types,
    # and a Shoe object is created and added to the shoe_list.

    if shoe_list:
        print("The file has already been read")
        return
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 5:  # Checks to see if the data for the line is 5 long
                    country, code, product, cost, quantity = data
                    cost = float(cost)
                    quantity = int(quantity)
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
        print(f"File has been read with {len(shoe_list)} rows added to memory")
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")


def write_shoes_data():
    """
    Writes shoe data from the shoe_list to the inventory.txt file.
    """

    # Each shoe in the shoe_list is written as a line in the file,
    # with attributes separated by commas.

    try:
        with open(file_path, "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
        print("Shoe data written to file successfully.")
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")


def capture_shoes():
    """
    Captures new shoe information from the user and adds it to the shoe_list.
    """

    # The user is prompted to enter the country, code, product, cost, and quantity
    # for the new shoe. Input validation is performed to ensure correct data types are entered.
    # The new shoe is then added to the shoe_list and written to the inventory.txt file.

    country = input("Enter country: ")
    code = input("Enter code: ").upper()
    product = input("Enter product: ").title()
    cost = None
    while cost is None:
        try:
            cost = float(input("Enter cost: "))
        except ValueError:
            print("Invalid input. Please enter a valid cost (e.g., 12.99).")
    quantity = None
    while quantity is None:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input. Please enter a valid quantity (e.g., 10).")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully.")
    write_shoes_data()


def view_all():
    """
    Displays a tabulated view of all shoes in the shoe_list.
    """
    table = []
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(table, headers, tablefmt="grid"))


def re_stock():
    """
    Re-stocks a shoe with an additional quantity.
    """

    # The shoe with the lowest quantity in the shoe_list is identified.
    # The user is prompted to enter the quantity to add, and the quantity
    # of the shoe is updated accordingly. The shoe data is then written to
    # the inventory.txt file.

    lowest_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe with the lowest quantity: {lowest_quantity_shoe}")
    add_quantity = int(input("Enter quantity to add: "))
    lowest_quantity_shoe.quantity += add_quantity
    print("Quantity updated successfully.")
    write_shoes_data()


def search_shoe():
    """
    Searches for a shoe in the shoe_list based on its code.
    """

    # The user is prompted to enter the shoe code to search for.
    # If a shoe with the provided code is found, its details are displayed.
    # Otherwise, a message indicating that the shoe was not found is shown.

    code = input("Enter shoe code to search: ").upper()
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"Shoe found: {shoe}")
            return
    print("Shoe not found.")


def value_per_item():
    """
    Calculates and displays the value of each shoe item in the shoe_list for the Country in a table.
    """

    # The value of each shoe is calculated by multiplying its cost and quantity.

    table = []
    for shoe in shoe_list:
        table.append(
            [
                shoe.country,
                shoe.code,
                shoe.product,
                shoe.cost * shoe.quantity,
            ]
        )
    headers = ["Country", "Code", "Product", "Total Value"]
    print(tabulate(table, headers, tablefmt="grid"))


def highest_qty():
    """
    Finds and displays the shoe with the highest quantity in the shoe_list.
    """
    max_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe with the highest quantity: {max_quantity_shoe}")


choice = None
# Main menu
# The while loop looks for the exit of a 0 entered in the choice to exit the program
while choice != "0":
    print("\n===== Inventory Management System =====")
    print("1. Read shoe data from file")
    print("2. Capture new shoe")
    print("3. View all shoes")
    print("4. Re-stock")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find shoe with highest quantity")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if not shoe_list and choice != "1":
        print("You have not read in the data yet.")
        continue

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice != "0":
        print("Invalid choice. Please try again.")


print("Thank you for using the Inventory Management system!")
