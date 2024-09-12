"""
Ricky Zheng
Class: CS 521 - Spring 1
Date: 2/21/2024
Final Project
Description of File: This Python scripts contains the functionality that allows
                     the user to create a customer order upon menu selection.
"""

import customer_order


def display_interface_info():
    """Displays helpful information to help navigate new order creation."""

    print("******************************************************")
    print("Please enter each item to order in the format below.")
    print('To look at items currently in cart, enter: "cart')
    print('To finish order, enter: "checkout"')
    print('To cancel order, enter: "cancel"')
    print("*******************************************************")
    print("")


def display_cart(cart):
    """ Displays all the current items the customer has added to cart.

    Args:
        cart (dictionary): Contains all items customer has put in their cart.
    """

    total_quantity = 0
    total_price = 0

    # Total quantity
    for name_and_price in cart:
        total_quantity += cart[name_and_price]

    print("")
    print("********************************************")
    print(f"                 Cart ({total_quantity})                    ")
    print("********************************************")
    print("")

    column1 = "Items"
    column1_underline = "---------"
    column2 = "Price ($)"
    column2_underline = "---------"
    column3 = "Quantity"
    column3_underline = "---------"
    print(f"{column1: ^15} {column2: ^15} {column3: ^10}")
    print(f"{column1_underline: ^15} "
          f"{column2_underline: ^15} "
          f"{column3_underline: ^10}")

    if len(cart) == 0:
        empty_item = "Empty"
        empty_quantity = "Empty"
        empty_price = "Empty"
        print(f"{empty_item: ^15} {empty_price: ^15} {empty_quantity: ^10}")

    for name_and_price in cart:
        item_total_price = name_and_price[1] * cart[name_and_price]
        item_total_price_str = f"{item_total_price:.2f}"
        total_price += item_total_price

        print(f"{name_and_price[0]: ^15} "
              f"{item_total_price_str: ^15} "
              f"{cart[name_and_price]: ^10}")

    print("")
    total_price_str = f"Total ($): {total_price:.2f}"
    print(f"{total_price_str: ^40}")
    print("")


def create_order(stock, customer_first_name, customer_last_name):
    """Creates a customer order by prompting user for necessary information.
    Ensures successful orders are created by validating user selections.

    Args:
        stock (Inventory): Contains all items currently in stock based off
                           inventory file.

        customer_first_name (string): First name of customer.

        customer_last_name (string): Last name of customer.
    """

    customer_cart = dict()
    order_finished = False

    display_interface_info()

    while True:
        item_request = input("Enter Item and Quantity (Ex: potato 23): ")

        if item_request.lower() == "":
            continue

        # Checkout Order
        if item_request.lower() == "checkout":
            checkout = False

            while True:
                selection = input("Complete checkout (Y or N): ")
                if selection.upper() == "Y":
                    checkout = True
                    break
                elif selection.upper() == "N":
                    break
                else:
                    print("Invalid selection. Please try again.")
                    continue

            if checkout:
                order_finished = True
                break
            else:
                continue

        # Cancel order
        if item_request.lower() == "cancel":
            checkout = False

            while True:
                selection = input("Cancel this order (Y or N): ")
                if selection.upper() == "Y":
                    checkout = True
                    break
                elif selection.upper() == "N":
                    break
                else:
                    continue

            if checkout:
                order_finished = False
                break
            else:
                continue

        # Look at items in cart
        if item_request.lower() == "cart":
            display_cart(customer_cart)
            continue

        items_in_cart = item_request.split()

        # Make sure selection is valid
        if len(items_in_cart) != 2:
            print("Invalid selection. Please try again.")
            continue

        if not items_in_cart[1].isnumeric():
            print("Invalid quantity. Please enter a digit(s).")
            continue

        if int(items_in_cart[1]) <= 0:
            print("Invalid quantity. Please enter a non-zero quantity.")
            continue

        item_name = str(items_in_cart[0]).lower()
        item_quantity = int(items_in_cart[1])

        # Check if item in inventory
        if item_name.lower() not in stock.item_price_lookup.keys():
            print(f'Could not find "{item_name}" in inventory. '
                  f'Please try again.')
            continue

        # Check if item quantity is in stock
        lookup_pair = (item_name, stock.item_price_lookup[item_name])
        if int(item_quantity) > int(stock.inventory[lookup_pair]):
            print(f"Not enough stock for ({stock.inventory[lookup_pair]})."
                  f" Please try again.")
            continue

        # Add to cart, update quantity if already in cart
        if lookup_pair in customer_cart.keys():
            customer_cart[lookup_pair] += item_quantity
        else:
            customer_cart[lookup_pair] = item_quantity

    # Create customer order
    if order_finished:
        if len(customer_cart.keys()) > 0:
            # Modify existing amount in inventory file
            stock.modify_inventory(customer_cart)

            # Create customer order based off previous entered info
            new_order = customer_order.CustomerOrder(customer_cart,
                                                     customer_first_name,
                                                     customer_last_name)

            # Display order location
            print("")
            print(f"Order Location: "
                  f"{new_order.display_order_file_info(include_path=True)}")

            # Display customer overall info
            print(new_order.display_customer_info(include_file_name=True))
            print(new_order.display_customer_items())

            print("Checkout complete! Returning to main menu.")
            print("")
        else:
            print("Empty Cart. No order created. Returning to main menu.")
    else:
        print("Order cancelled. Returning to main menu.")

