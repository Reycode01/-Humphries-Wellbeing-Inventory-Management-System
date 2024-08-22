#!/usr/bin/env python3

import sys
import os

# Add the lib directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))

from models.category import Category
from models.supplier import Supplier
from models.products import Product
from models.brand import Brand
from models.base_model import initialize_db

def print_help():
    print("Commands:")
    print("  add_category")
    print("  list_categories")
    print("  find_category")
    print("  delete_category")
    print("  add_supplier")
    print("  list_suppliers")
    print("  find_supplier")
    print("  delete_supplier")
    print("  add_product")
    print("  list_products")
    print("  find_product")
    print("  delete_product")
    print("  add_brand")
    print("  list_brands")
    print("  find_brand")
    print("  delete_brand")

def parse_price(price_str):
    # Remove currency symbols and commas, then convert to float
    price_str = price_str.replace("ksh. ", "").replace(",", "")
    try:
        return float(price_str)
    except ValueError:
        raise ValueError("Invalid price format")

def main():
    initialize_db()

    if len(sys.argv) < 2:
        print("No command provided.")
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "add_category":
            name = input("Enter category name: ")
            Category.create(name)
            print(f'Category "{name}" added.')

        elif command == "list_categories":
            categories = Category.get_all()
            for category in categories:
                print(f'{category.id}: {category.name}')

        elif command == "find_category":
            category_id = int(input("Enter category ID: "))
            category = Category.find_by_id(category_id)
            if category:
                print(f'Found category: {category.id} - {category.name}')
            else:
                print('Category not found')

        elif command == "delete_category":
            category_id = int(input("Enter category ID: "))
            Category.delete(category_id)
            print(f'Category {category_id} deleted.')

        elif command == "add_supplier":
            name = input("Enter supplier name: ")
            contact_info = input("Enter supplier contact info: ")
            try:
                Supplier.create(name, contact_info)
                print(f'Supplier "{name}" added.')
            except Exception as e:
                print(f"An error occurred: {e}")

        elif command == "list_suppliers":
            suppliers = Supplier.get_all()
            for supplier in suppliers:
                print(f'{supplier.id}: {supplier.name} ({supplier.contact_info})')

        elif command == "find_supplier":
            supplier_id = int(input("Enter supplier ID: "))
            supplier = Supplier.find_by_id(supplier_id)
            if supplier:
                print(f'Found supplier: {supplier.id} - {supplier.name} ({supplier.contact_info})')
            else:
                print('Supplier not found')

        elif command == "delete_supplier":
            supplier_id = int(input("Enter supplier ID: "))
            Supplier.delete(supplier_id)
            print(f'Supplier {supplier_id} deleted.')

        elif command == "add_product":
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            category_id = int(input("Enter category ID: "))
            supplier_id = int(input("Enter supplier ID: "))
            price_input = input("Enter product price (e.g., 'ksh. 1500'): ")
            try:
                price = parse_price(price_input)
            except ValueError:
                print(f"Invalid price format: {price_input}")
                sys.exit(1)
            brand_id = int(input("Enter brand ID: "))
            Product.create(name, quantity, category_id, supplier_id, price, brand_id)
            print(f'Product "{name}" added.')

        elif command == "list_products":
            products = Product.get_all()
            for product in products:
                print(f'{product.id}: {product.name} ({product.quantity})')

        elif command == "find_product":
            product_id = int(input("Enter product ID: "))
            product = Product.find_by_id(product_id)
            if product:
                print(f'Found product: {product.id} - {product.name} ({product.quantity})')
            else:
                print('Product not found')

        elif command == "delete_product":
            product_id = int(input("Enter product ID: "))
            Product.delete(product_id)
            print(f'Product {product_id} deleted.')

        elif command == "add_brand":
            name = input("Enter brand name: ")
            Brand.create(name)
            print(f'Brand "{name}" added.')

        elif command == "list_brands":
            brands = Brand.get_all()
            for brand in brands:
                print(f'{brand.id}: {brand.name}')

        elif command == "find_brand":
            brand_id = int(input("Enter brand ID: "))
            brand = Brand.find_by_id(brand_id)
            if brand:
                print(f'Found brand: {brand.id} - {brand.name}')
            else:
                print('Brand not found')

        elif command == "delete_brand":
            brand_id = int(input("Enter brand ID: "))
            Brand.delete(brand_id)
            print(f'Brand {brand_id} deleted.')

        else:
            print("Unknown command.")
            print_help()

    except IndexError:
        print("Missing arguments for the command.")
        print_help()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()



 
        