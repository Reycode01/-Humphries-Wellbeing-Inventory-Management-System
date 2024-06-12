import click
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
if __name__ == '__main__':
    initialize_db() 
    cli()


        
        
    

 
        