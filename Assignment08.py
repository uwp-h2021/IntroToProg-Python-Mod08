# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# HJong, 5/31/2021, Created new script
# HJong, 5/31/2021, Added Product class
# HJong, 5/31/2021, Added FileProcessor class
# HJong, 5/31/2021, Added IO class
# HJong, 5/31/2021, Added Main
# HJong, 5/31/2021, Added exception handling for user choice of option
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
list_of_product_objects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        HJong, 5/31/2021, Created Product class
        HJong, 5/31/2021, Added Exception handling
    """
    def __init__(self, name, price):    # Constructor of product object
        self.__product_name = name
        self.__product_price = price

    @property
    def product_name(self):     # Property getter of product name
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):  # Property setter of product name
        if str(value).isnumeric():
            raise Exception('Product name cannot be numeric!')
        else:
            self.__product_name = value

    @property
    def product_price(self):    # Property getter of product price
        return self.__product_price

    @product_price.setter
    def product_price(self, value):     # Property setter of product price
        if str(value).isnumeric():
            print('Price set!')
            self.__product_price = value
        else:
            raise Exception('Product price must be numeric!')

# Data -------------------------------------------------------------------- #
# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        HJong, 5/31/2021, Created Class
        HJong, 5/31/2021, Added docstrings for methods
    """
    @staticmethod
    def save_data_to_file(filename, list_of_product_objects):   # Save list of product objects into file
        """ Save the list of product objects into file

        :param filename: (string) of file name
        :param list_of_product_objects: (list) of product objects
        :return: nothing
        """
        objFile = open(filename, 'w')
        for obj in list_of_product_objects:
            objFile.write(obj.product_name+','+obj.product_price+'\n')

    @staticmethod
    def read_data_from_file(file_name):     # Read product data from file
        """ Read product objects data from file

        :param: file_name: (string) of file name
        :return: list_of_product_objects: (list) of product objects
        """
        objFile = open(file_name, 'r')
        list_of_product_objects = []
        for row in objFile:
            name, price = row.split(',')
            list_of_product_objects.append(Product(name, price.strip()))
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Perform input and output product data with users:

    methods:
        show_menu():    Display options to users

        get_user_choice(): -> (a string variable of user choice)

        display_data(list_of_product_objects):  Display current data to users

        get_product_data(): -> (product_name, product_price)

    changelog: (When,Who,What)
        HJong, 5/31/2021, Created Class
        HJong, 5/31/2021, Added docstrings for methods
    """

    @staticmethod
    def show_menu():    # Show menu to user
        """ Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        (1) Show Current Product Data
        (2) Add Product Data
        (3) Save Product Data
        (4) Exit
        ''')

    @staticmethod
    def get_user_choice():  # Get user's choice
        """ Get user choice of options

        :return: string
        """
        choice = input('Enter your choice: ')
        return choice

    @staticmethod
    def display_data(obj):    # Show the current data from the file to user
        """ Show the current list of product objects

        :param: obj: (list) of product product objects
        :return: nothing
        """
        print('\nCurrent Inventory \n'+24*'-')
        for item in obj:
            print(item.product_name,' $'+item.product_price, sep=',')
        print(24*'-')

    @staticmethod
    def get_product_data():     # Get product data from user
        """ Receive user input of product data

        :return: (tuple) of product name and product price
        """
        name = input('Enter product name: ')
        if str(name).isnumeric():
            raise Exception('\nAlert! Name cannot be numeric! ')
        price = input('Enter product price: ')
        if not str(price).isnumeric():
            raise Exception('\nAlert! Price must be numeric! ')
        return name, price

# Presentation (Input/Output)  -------------------------------------------- #
# Main Body of Script  ---------------------------------------------------- #


objList = FileProcessor.read_data_from_file(strFileName)    # Load data from file into a list of objects

while True:
    IO.show_menu()  # Show user a menu of options
    user_choice = IO.get_user_choice()  # Receive user choice of option
    try:
        if user_choice == '1':  # Show user the current product data
            IO.display_data(objList)
        elif user_choice == '2':    # Let user add data into the list of product objects
            try:
                product_name, product_price = IO.get_product_data()
                objList.append(Product(product_name, product_price))
            except Exception as error1:
                print(error1)
        elif user_choice == '3':    # Let user save product data into file
            FileProcessor.save_data_to_file(strFileName, objList)
        elif user_choice == '4':    # Exit program
            break
        else:       # Exception handling of user choice out of [1-4]
            raise Exception('\nPlease enter [1-4] only!')
    except Exception as error2:
        print(error2)
# Main Body of Script  ---------------------------------------------------- #

