# Shoe Inventory Management System

- [Introduction](#shoe-inventory-management-system)
- [Getting Started](#getting-started)
- [Files](#files)
- [Class: Shoe](#class-shoe)
- [Functions](#functions)
  - [`read_shoes_data()`](#read_shoes_data)
  - [`capture_shoes()`](#capture_shoes)
  - [`view_all()`](#view_all)
  - [`re_stock()`](#re_stock)
  - [`search_shoe()`](#search_shoe)
  - [`value_per_item()`](#value_per_item)
  - [`highest_qty()`](#highest_qty)
  - [`main()`](#main)
- [Running the Program](#running-the-program)
  - [Welcome Menu](#welcome-menu)
  - [Load Data](#load-data)
  - [Capture New Shoe](#capture-new-shoe)
  - [View All Shoes](#view-all-shoes)
  - [Re-stock](#re-stock)
  - [Search for a shoe](#search-for-a-shoe)
  - [Calculate value per item](#calculate-value-per-item)
  - [Find Shoe with highest quantity](#find-shoe-with-highest-quantitiy)
 - [Credits](#Credits)

## Introduction

This Python program is designed to read data from the text file `inventory.txt` and perform various operations on the data to prepare it for presentation to your managers. The program is structured with a class named `Shoe` and several functions to handle different tasks related to shoe inventory management.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python installed (version 3.6 or higher).
3. Open the terminal and navigate to the repository's directory.

## Files

- `inventory.py`: Contains the main code for the Shoe Inventory Management System.
- `inventory.txt`: This is the input text file containing shoe inventory data.

## Class: Shoe

The `Shoe` class represents a shoe item and has the following attributes:

- `country`
- `code`
- `product`
- `cost`
- `quantity`

The class defines the following methods:

- `get_cost()`: Returns the cost of the shoe.
- `get_quantity()`: Returns the quantity of the shoe.
- `__str__()`: Returns a string representation of the shoe.

## Functions

### `read_shoes_data()`

This function reads data from the `inventory.txt` file and creates `Shoe` objects with the data. Each line in the file represents data to create one `Shoe` object. The function skips the first line and utilizes error handling with `try-except`.

### `capture_shoes()`

Allows the user to capture data about a shoe and creates a `Shoe` object using the captured data. The created object is appended to the list of shoes.

### `view_all()`

Iterates over the list of shoes and prints the details of each shoe using the `__str__()` method. Optional: The data can be organized in a tabulated format using the `tabulate` module.

### `re_stock()`

Finds the shoe object with the lowest quantity (needing restocking), asks the user if they want to add a specific quantity of shoes, and updates the quantity. The updated quantity is also updated in the `inventory.txt` file.

### `search_shoe(code)`

Searches for a shoe in the list using the provided shoe code and returns the corresponding `Shoe` object.

### `value_per_item()`

Calculates and prints the total value for each item in the inventory using the formula: `value = cost * quantity`.

### `highest_qty()`

Determines the product with the highest quantity and prints this shoe as available for sale.

### `main()`

Creates a menu that allows the user to execute each of the above functions.

## Running the Program

Execute the `inventory.py` script using the following command in your terminal:



```bash
python inventory.py
```

### Welcome Menu
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/62cbbc6f-0004-4ea8-844b-fc688415f172)

### Load Data 
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/5be77d0b-e1dc-40b3-b83c-503d4608f760)

### Capture New Shoe
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/0a26e98b-644c-4e8c-b274-11c7428f6613)

### View all shoes
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/135fccde-9b6f-4d7b-9ed6-3468e53b4990)

### Re-stock
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/51bec7a6-36ce-4608-bbba-2ff9616b44cc)

### Search for a shoe
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/b18d1144-df68-449c-9007-7c936841342f)

### Calculate value per item
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/382be491-73d6-4cd7-bdf7-c00137709c81)

### Find shoe with highest quantitiy 
![image](https://github.com/Naude555/terminal_inventory_project/assets/60476722/a7a0ddb6-0789-483a-8f88-cc01630ed338)


## Credits
Naude Opperman
