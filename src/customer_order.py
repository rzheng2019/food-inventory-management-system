"""
Ricky Zheng
Class: CS 521 - Spring 1
Date: 2/21/2024
Final Project
Description of File: This Python file defines the CustomerOrder class that is
                     used to house all information for each individual
                     order created.
"""

import os


class CustomerOrder:
    """This class is used to hold all the necessary customer order info.
    Upon every customer order created, an output file detailing the order
    is created for future reference.

    Attributes:
        customer_first_name (string): First name of customer.

        customer_last_name (string): Last name of customer.

        items_ordered (dictionary): Storage for items ordered.

        __order_number (int): Number used to determine orders created.

        order_id (string): An order ID that's created unique for each order.

    Methods:
        __init__(items_ordered, first_name, last_name): Initializes customer
                                                        info and creates an
                                                        order_id.

        __generate_order_id(first_name, last_name): Generate an order_id string.

        __generate_order_file(): Generates the output file for each customer
                                 order.

        __confirm_customer_info(first_name, last_name): Ensures information
                                                        entered meets user
                                                        criteria.

        display_customer_info(include_file_name): Displays customer name and
                                                  order_id along with its file
                                                  location.

        display_customer_items(): Displays all items ordered by customer.

        display_order_file_info(include_path): Displays output file name and
                                               location.

        __str__(): Displays both customer info and items ordered.

        __dir__(): Displays all CustomerOrder class attributes.
    """

    def __init__(self, items_ordered, first_name="", last_name=""):
        """Creates customer order from customer names and items ordered.
        Generates an order id for each object created.

        Args:
            items_ordered (dictionary): Items the customer ordered.

            first_name (string): First name of customer.

            last_name (string): Last name of customer.
        """

        # Public customer attributes
        self.customer_first_name = first_name
        self.customer_last_name = last_name
        self.items_ordered = items_ordered

        # Private customer attribute
        self.__order_number = 1

        # Order ID gets created once and is never changed
        self.order_id = self.__generate_order_file()

    def __generate_order_id(self, first_name, last_name):
        """Generates an order id by confirming customer info entered is correct.

        Args:
            first_name (string): Customer first name.

            last_name (string): Customer last name.

        Return:
            confirmation_num (string): A combination of first name, last name,
                                       and an order number.
        """

        # Confirm customer info
        print(self.__confirm_customer_info(first_name, last_name))

        # Find all file order numbers
        existing_numbers = set()

        cwd = os.getcwd()
        order_path = os.path.join(cwd, "orders")

        if os.path.exists(order_path):
            customer_orders_file_path = os.listdir(order_path)

            # Put all order numbers in existing numbers set
            for order_id in customer_orders_file_path:
                if not order_id.startswith('.'):
                    file_name = order_id.split(".txt")

                    # Remove .txt for file name
                    while "" in file_name:
                        file_name.remove("")

                    # Extract number from order name
                    file_name_parts = file_name[0].split("_")
                    order_num = int(file_name_parts[2])

                    # Place into set to avoid duplicates
                    existing_numbers.add(order_num)

            current_order_number = self.__order_number

            # New order number always be 1 more than most recent order number.
            if current_order_number in sorted(existing_numbers):
                current_order_number += sorted(existing_numbers)[-1]

            self.__order_number = current_order_number
        else:
            os.mkdir(order_path)

        confirmation_num = (f"{str(self.customer_first_name)}"
                            f"_{str(self.customer_last_name)}"
                            f"_{self.__order_number}")

        return confirmation_num

    def __generate_order_file(self):
        """Creates an output file that details the customers info and
        items ordered.

        Return:
            file_name (string): The customers order output file name.
        """

        cwd = os.getcwd()
        orders_path = os.path.join(cwd, "orders")
        file_name = self.__generate_order_id(self.customer_first_name,
                                             self.customer_last_name)
        customer_order_path = os.path.join(orders_path, f"{file_name}.txt")

        # Create output file
        with open(customer_order_path, "w+") as customer_order_file:
            customer_order_file.write(self.display_customer_info())
            customer_order_file.write("\n")
            customer_order_file.write(self.display_customer_items())
            customer_order_file.flush()
            os.fsync(customer_order_file.fileno())

        # Return file name as the order_id
        return file_name

    def __confirm_customer_info(self, first_name, last_name):
        """Confirms the users information entered when prompted for
        after checkout sequence occurs.

        Args:
            first_name (string): Customers first name.

            last_name (string): Customers last name.

        Return:
            confirmation_output_message (string): Message that confirms success.
        """

        full_name = f"{first_name} {last_name}"

        while True:
            print("Please confirm info below:")

            print(f"Customer Name: {full_name}")

            confirmation_popup = input("Is this correct (Y or N): ")

            if confirmation_popup.upper() == "N":
                self.customer_first_name = input("Customer First Name: ")
                self.customer_last_name = input("Customer Last Name: ")
                full_name = (f"{self.customer_first_name}"
                             f" {self.customer_last_name}")
                print(f"Customer Name changed to: {full_name}")
            elif confirmation_popup.upper() == "Y":
                break
            else:
                continue

        confirmed_output_message = "\n" + "Customer information saved!"

        return confirmed_output_message

    def display_customer_info(self, include_file_name=False):
        """Displays customer first name, last name, and order_id.

        Args:
            include_file_name (bool): Determines if file name should be
                                      included as well.

        Return:
            customer_info (string): A string containing customers first name,
                                    last name, order_id, and output file name
                                    if desired.
        """

        full_name = f"{self.customer_first_name} {self.customer_last_name}"
        full_name_underscore = (f"{self.customer_first_name}"
                                f"_{self.customer_last_name}")
        file_name = (full_name_underscore
                     + "_"
                     + str(self.__order_number)
                     + ".txt")

        if include_file_name:
            customer_info = (f"Customer Name: {full_name}"
                             f"\n"
                             f"Customer Order ID: {full_name_underscore}_"
                             f"{self.__order_number}"
                             f"\n"
                             f"Customer File Name: {file_name}")
        else:
            customer_info = (f"Customer Name: {full_name}"
                             f"\n"
                             f"Customer Order ID: {full_name_underscore}_"
                             f"{self.__order_number}")

        return customer_info

    def display_customer_items(self):
        """Displays items ordered section from the customer order output
        file.

        Return:
            total_output (string): The entire customer items info section.
        """

        total_quantity = 0
        total_price = 0
        total_output = ""

        # Total quantity
        for name_and_price in self.items_ordered:
            total_quantity += self.items_ordered[name_and_price]

        total_output += "\n"
        total_output += "********************************************\n"
        total_output += (f"              Items Ordered ({total_quantity})      "
                         f"              \n")
        total_output += "********************************************\n"
        total_output += "\n"

        column1 = "Items"
        column1_underline = "---------"
        column2 = "Price ($)"
        column2_underline = "---------"
        column3 = "Stock"
        column3_underline = "---------"
        category_columns = f"{column1: ^15} {column2: ^15} {column3: ^10}"
        underline_columns = (f"{column1_underline: ^15} "
                             f"{column2_underline: ^15} "
                             f"{column3_underline: ^10}")

        total_output += category_columns + "\n" + underline_columns + "\n"

        if len(self.items_ordered) == 0:
            empty_item = "Empty"
            empty_quantity = "Empty"
            empty_price = "Empty"
            print(f"{empty_item: ^15} {empty_price: ^15} {empty_quantity: ^10}")
        else:
            for name_and_price in self.items_ordered:
                item_total_price = (name_and_price[1]
                                    * self.items_ordered[name_and_price])
                item_total_price_str = f"{item_total_price:.2f}"
                total_price += item_total_price

                item_row = (f"{name_and_price[0]: ^15} "
                            f"{item_total_price_str: ^15} "
                            f"{self.items_ordered[name_and_price]: ^10}")

                total_output += item_row + "\n"

            total_price_str = f"Total ($): {total_price:.2f}"
            total_output += "\n" + f"{total_price_str: ^40}" + "\n"

        return total_output

    def display_order_file_info(self, include_path=False):
        """Displays the output file name and output file path if desired.

        Args:
            include_path (bool): Determines if output file path should be
                                 included.
        Return:
            orders_info (string): The output file name and location if desired.
        """

        if include_path:
            cwd = os.getcwd()
            dir_path = os.path.join(cwd, "orders")
            orders_info = os.path.join(dir_path, self.order_id + ".txt")
            return orders_info
        else:
            orders_info = self.order_id + ".txt"
            return orders_info

    def __str__(self):
        """Displays customer and info from output file.

        Return:
            customer_order_information: Customer order information.
        """

        customer_order_information = "\nOrder Information:\n"
        customer_order_information += self.display_customer_info()
        customer_order_information += "\n"
        customer_order_information += self.display_customer_items()

        return customer_order_information

    # Magic class method that displays all class attributes
    def __dir__(self):
        """Displays all class attributes.

        Return:
            customer_attributes (list): A list of all customer attributes.
        """

        customer_attributes = ['customer_first_name',
                               'customer_last_name',
                               'items_ordered',
                               'order_number',
                               'order_id']

        return customer_attributes


if __name__ == '__main__':

    # Unit Test Framework for CustomerOrder

    order_dict = dict()
    order_dict[("Potato", 1.35)] = 100

    customer_test = CustomerOrder(items_ordered= order_dict,
                                  first_name="John",
                                  last_name="Doe")

    # Display customer order output for reference
    print(customer_test.__str__())

    print("")
    print("Running unit tests.")

    # Test case: Testing class constructor was successful. Attributes assigned.
    assert customer_test.customer_first_name == "John"
    assert customer_test.customer_last_name == "Doe"
    assert customer_test.items_ordered == order_dict

    # Test case: Display customer file path info.
    cwd_test = os.getcwd()
    dir_path_test = os.path.join(cwd_test, "orders")
    orders_path_test = os.path.join(dir_path_test,
                                    customer_test.order_id + ".txt")
    assert customer_test.display_order_file_info(True) == orders_path_test

    # Test case: Testing output file generation
    assert os.path.exists(orders_path_test) is True

    # Test case: Display customer info.
    full_name_test = (customer_test.customer_first_name + " "
                      + customer_test.customer_last_name)
    file_name_test = customer_test.order_id + ".txt"
    customer_info_test = (f"Customer Name: {full_name_test}"
                          f"\n"
                          f"Customer Order ID: {customer_test.order_id}"
                          f"\n"
                          f"Customer File Name: {file_name_test}")
    assert customer_test.display_customer_info(True) == customer_info_test

    # Test Case: __dir__ should print out all class attributes.
    expected_attributes = ['customer_first_name',
                           'customer_last_name',
                           'items_ordered',
                           'order_number',
                           'order_id']

    assert customer_test.__dir__() == expected_attributes

    print("")

    print("Unit tests all passed successfully.")
