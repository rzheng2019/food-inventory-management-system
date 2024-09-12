"""
Ricky Zheng
Class: CS 521 - Spring 1
Date: 2/21/2024
Final Project
Description of File: This python file is meant to serve as the user's
                     main interface. The overall application should be
                     run through this file.
"""

import main_menu
import inventory_manager
import create_order_interface


if __name__ == '__main__':
    # Initial Setup
    main_menu.print_title_info()
    main_menu.print_main_menu()

    # Load in current inventory
    stock = inventory_manager.Inventory()

    # Enable menu
    while True:
        menu_selection = input("Select Option #: ")

        if menu_selection == "":
            continue

        # Ensure selection is valid
        try:
            selection = int(menu_selection)
        except ValueError:
            print("Invalid option (1 for Main Menu). Please try again.")
            continue

        if int(menu_selection) <= 0:
            print("Invalid option (1 for Main Menu). Please try again.")
            continue

        if int(menu_selection) > len(main_menu.MenuOptions.OPTION_DICT):
            print("Invalid option (1 for Main Menu). Please try again.")
            continue

        select_option = main_menu.MenuOptions.OPTION_DICT[int(menu_selection)]

        if select_option == main_menu.MenuOptions.OPTION_DICT[1]:
            main_menu.print_main_menu()
        elif select_option == main_menu.MenuOptions.OPTION_DICT[2]:
            stock.print_current_inventory()
        elif select_option == main_menu.MenuOptions.OPTION_DICT[3]:
            # Prompt for customer info
            print("")
            print("Enter customer information below.")
            print("")

            customer_first_name = input("Customer First Name: ")
            customer_last_name = input("Customer Last Name: ")

            print("")

            # Ask user what they want to order
            create_order_interface.create_order(stock,
                                                customer_first_name,
                                                customer_last_name)
            # Refresh inventory after changes
            stock.refresh_inventory()
        elif select_option == main_menu.MenuOptions.OPTION_DICT[4]:
            print("")
            print("Successfully exited application.")
            break
        else:
            print("Invalid option (1 for Main Menu). Please try again.")
