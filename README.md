# Humphries Wellbeing Inventory Management System

## Description

This project is a Command-Line Interface (CLI) application for managing an inventory system. The application uses an SQLite database to store data and provides a user-friendly interface to interact with the database.

## Features

- Add, delete, list, and find categories
- Add, delete, list, and find suppliers
- Add, delete, list, and find products

## Dependencies

The project uses the following dependencies:

- Python 3.8
- Click
- DB Browser for SQLite (optional, for database visualization)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone git@github.com:Reycode01/-Humphries-Wellbeing-Inventory-Management-System.git
    cd -Humphries-Wellbeing-Inventory-Management-System
    ```

2. **Set Up the Virtual Environment and Install Dependencies**:
    - Ensure you have `pipenv` installed. If not, install it using `pip`:
      ```bash
      pip install pipenv
      ```
    - Initialize the Pipenv environment with Python 3.8 and install dependencies:
      ```bash
      pipenv install --python 3.8
      pipenv install click
      ```

3. **Activate the Virtual Environment**:
    ```bash
    pipenv shell
    ```

4. **Source the Bash Aliases**:
    ```bash
    source ~/.bash_aliases
    ```

## Usage

Once the virtual environment is activated, you can run the CLI application:
source ~/.bash_aliases
1. **Add a Category**:
    ```bash
    add_category "Your Category Name"
    ```

2. **Add a Supplier**:
    ```bash
    add_supplier "Supplier Name" "Contact Info"
    ```

3. **Add a Product**:
    ```bash
    add_product "Product Name" "Quantity" "Category ID" "Supplier ID"
    ```

4. **List Categories**:
    ```bash
    list_categories
    ```

5. **List Suppliers**:
    ```bash
    list_suppliers
    ```

6. **List Products**:
    ```bash
    list_products
    ```

7. **Find a Category, Supplier, or Product**:
    ```bash
    find_category "Category Name"
    find_supplier "Supplier Name"
    find_product "Product Name"
    ```

8. **Delete a Category, Supplier, or Product**:
    ```bash
    delete_category "Category ID"
    delete_supplier "Supplier ID"
    delete_product "Product ID"
    ```
