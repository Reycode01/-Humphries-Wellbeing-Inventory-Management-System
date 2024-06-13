import sys
import os
import click
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from lib.models.category import Category
from lib.models.supplier import Supplier
from lib.models.products import Product
from lib.models.base_model import initialize_db

@click.group()
def cli():
    pass

# Category commands
@cli.group()
def category():
    pass

@category.command()
@click.argument('name')
def add(name):
    try:
        Category.create(name)
        click.echo(f'Category {name} added.')
    except ValueError as e:
        click.echo(f'Error: {e}')

@category.command()
@click.argument('category_id', type=int)
def delete(category_id):
    Category.delete(category_id)
    click.echo(f'Category {category_id} deleted.')

@category.command()
def list():
    categories = Category.get_all()
    for category in categories:
        click.echo(f'{category.id}: {category.name}')

@category.command()
@click.argument('category_id', type=int)
def find(category_id):
    category = Category.find_by_id(category_id)
    if category:
        click.echo(f'Found category: {category.id} - {category.name}')
    else:
        click.echo('Category not found')

# Supplier commands
@cli.group()
def supplier():
    pass

@supplier.command()
@click.argument('name')
@click.argument('contact_info')
def add(name, contact_info):
    try:
        Supplier.create(name, contact_info)
        click.echo(f'Supplier {name} added.')
    except ValueError as e:
        click.echo(f'Error: {e}')

@supplier.command()
@click.argument('supplier_id', type=int)
def delete(supplier_id):
    Supplier.delete(supplier_id)
    click.echo(f'Supplier {supplier_id} deleted.')

@supplier.command()
def list():
    suppliers = Supplier.get_all()
    for supplier in suppliers:
        click.echo(f'{supplier.id}: {supplier.name} ({supplier.contact_info})')

@supplier.command()
@click.argument('supplier_id', type=int)
def find(supplier_id):
    supplier = Supplier.find_by_id(supplier_id)
    if supplier:
        click.echo(f'Found supplier: {supplier.id} - {supplier.name} ({supplier.contact_info})')
    else:
        click.echo('Supplier not found')

# Product commands
@cli.group()
def product():
    pass

@product.command()
@click.argument('name')
@click.argument('quantity', type=int)
@click.argument('category_id', type=int)
@click.argument('supplier_id', type=int)
def add(name, quantity, category_id, supplier_id):
    try:
        Product.create(name, quantity, category_id, supplier_id)
        click.echo(f'Product {name} added.')
    except ValueError as e:
        click.echo(f'Error: {e}')

@product.command()
@click.argument('product_id', type=int)
def delete(product_id):
    Product.delete(product_id)
    click.echo(f'Product {product_id} deleted.')

@product.command()
def list():
    products = Product.get_all()
    for product in products:
        click.echo(f'{product.id}: {product.name} ({product.quantity})')

@product.command()
@click.argument('product_id', type=int)
def find(product_id):
    product = Product.find_by_id(product_id)
    if product:
        click.echo(f'Found product: {product.id} - {product.name} ({product.quantity})')
    else:
        click.echo('Product not found')

if __name__ == '__main__':
    initialize_db()
    cli()




        
        
    

 
        