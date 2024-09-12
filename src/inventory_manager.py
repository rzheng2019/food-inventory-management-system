"""
Ricky Zheng
Class: CS 521 - Spring 1
Date: 2/21/2024
Final Project
Description of File: This Python file defines an Inventory class which serves to
                     extract and modify the master inventory text file when
                     required to do so.
"""

import os


class Inventory:
    """Holds all the information extracted from each item in inventory input
    file and refreshes based on changes.

    Attributes:
        inventory (dictionary): Stores item names, prices, and quantity.

        item_price_lookup (dictionary): Stores item names and prices.

    Methods:
        __init__(): Initializes inventory using master inventory file.

        print_current_inventory(): Displays the items in current inventory.

        modify_inventory(new_inventory): Modify existing inventory according
                                         to new_inventory.

        refresh_inventory(): Updates current inventory with any changes in
                             master inventory file.
    """

    def __init__(self):
        """Initializes an inventory and item price look up storage using the
        master inventory text file as input."""

        self.inventory = dict()
        self.item_price_lookup = dict()
        self.refresh_inventory()

    def print_current_inventory(self):
        """ Prints current items formatted within inventory."""

        print("")
        print("********************************************")
        print("              Current Inventory             ")
        print("********************************************")
        print("")

        column1 = "Items"
        column1_underline = "---------"
        column2 = "Price ($)"
        column2_underline = "---------"
        column3 = "Stock"
        column3_underline = "---------"
        print(f"{column1: ^15} {column2: ^15} {column3: ^10}")
        print(f"{column1_underline: ^15} "
              f"{column2_underline: ^15} "
              f"{column3_underline: ^10}")

        for item in self.inventory:
            print(f"{item[0]: ^15} {item[1]: ^15} {self.inventory[item]: ^10}")
        print("")

    def modify_inventory(self, new_inventory):
        """Changes quantity of items within file.

        Args:
            new_inventory (dictionary): current inventory after making an order
        """

        cwd = os.getcwd()
        inventory_file_path = os.path.join(cwd, "inventory.txt")

        self.inventory.clear()
        entry_lines = list()

        with open(inventory_file_path) as inventory_file:
            for line in inventory_file:
                # Each entry line's name and quantity in list
                entry_lines += line.splitlines()

            for entry in entry_lines:
                entries = entry.split(", ")

                # Should just be 3 fields in list, don't add if field
                # formatted incorrectly in inventory.txt.
                if len(entries) == 3:
                    try:
                        name_and_price = (entries[0].lower(), float(entries[1]))
                        quantity = int(entries[2])
                    except ValueError:
                        continue

                    item_name = entries[0].lower()
                    item_price = float(entries[1])
                    item_quantity = int(entries[2])
                    name_and_price = (item_name, item_price)
                    quantity = item_quantity
                    self.inventory[name_and_price] = quantity
                    self.item_price_lookup[item_name] = item_price

            # Update current inventory quantity
            for name_and_price in new_inventory:
                self.inventory[name_and_price] -= new_inventory[name_and_price]

        # Update inventory text file
        with (open(inventory_file_path, "w") as inventory_file):
            for name_and_price in self.inventory:
                line = str(name_and_price[0]) + ", "
                line += str(name_and_price[1]) + ", "
                line += str((self.inventory[name_and_price])) + "\n"
                inventory_file.write(line)

    def refresh_inventory(self):
        """Refreshes inventory by opening and extracting current content within
        inventory.txt."""

        cwd = os.getcwd()
        inventory_file_path = os.path.join(cwd, "inventory.txt")

        self.inventory.clear()
        entry_lines = list()

        with open(inventory_file_path) as inventory_file:
            for line in inventory_file:
                # Each entry line's name and quantity in list
                entry_lines += line.splitlines()

            for entry in entry_lines:
                entries = entry.split(", ")

                # Should just be 3 fields in list, don't add if field
                # formatted incorrectly in inventory.txt
                if len(entries) == 3:
                    try:
                        name_and_price = (entries[0].lower(), float(entries[1]))
                        quantity = int(entries[2])
                    except ValueError:
                        continue

                    item_name = entries[0].lower()
                    item_price = float(entries[1])
                    item_quantity = int(entries[2])
                    name_and_price = (item_name, item_price)
                    quantity = item_quantity
                    self.inventory[name_and_price] = quantity
                    self.item_price_lookup[item_name] = item_price
