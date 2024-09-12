"""
Ricky Zheng
Class: CS 521 - Spring 1
Date: 2/21/2024
Final Project
Description of File: This python file is meant to display the main menu for the
                     Food Inventory Management System.
"""


def print_menu_bar():
    """ Prints menu bar in main interface."""

    print("")
    print("********************************************")
    print("                    Menu                    ")
    print("********************************************")
    print("")


class MenuOptions:
    """Class used to display menu options in main interface.

    Attributes:
        OPTION_DICT (Dictionary): Contains all options for the main menu.

    Methods:
        print_menu_options(): Prints all menu options.
    """

    OPTION_DICT = {1: "Main Menu",
                   2: "Current Inventory",
                   3: "Create New Order",
                   4: "Exit Application"}

    def print_menu_options(self):
        """Prints the options from OPTION_DICT attribute."""

        menu_options = list()

        for option in self.OPTION_DICT:
            menu_options.append(f"[{option}] {self.OPTION_DICT[option]}")

        print_menu_bar()

        for option in menu_options:
            print(option)

        print("")


def print_title_info():
    """Displays application title."""

    print("********************************************")
    print("      Food Inventory Management System      ")
    print("********************************************")
    print("")


def print_main_menu():
    """Displays main menu on main interface."""

    menu = MenuOptions
    menu.print_menu_options(menu())
