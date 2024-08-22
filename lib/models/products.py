from .base_model import BaseModel

class Product(BaseModel):
    def __init__(self, name, quantity, category_id, supplier_id, price, brand_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.category_id = category_id
        self.supplier_id = supplier_id
        self.price = price
        self.brand_id = brand_id

    @classmethod
    def create(cls, name, quantity, category_id, supplier_id, price, brand_id):
        if not name or quantity < 0 or not category_id or not supplier_id or price < 0 or not brand_id:
            raise ValueError("Invalid product data")

        query = '''
        INSERT INTO product (name, quantity, category_id, supplier_id, price, brand_id)
        VALUES (?, ?, ?, ?, ?, ?)
        '''

        try:
            cls.execute_query(query, (name, quantity, category_id, supplier_id, price, brand_id))
        except Exception as e:
            print(f"Error inserting product: {e}")
            raise

        return cls(name, quantity, category_id, supplier_id, price, brand_id)

    @classmethod
    def delete(cls, product_id):
        query = "DELETE FROM product WHERE id=?"
        try:
            cls.execute_query(query, (product_id,))
        except Exception as e:
            print(f"Error deleting product: {e}")
            raise

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM product"
        try:
            results = cls.fetch_query(query)
            return [cls(result[1], result[2], result[3], result[4], result[5], result[6], result[0]) for result in results]
        except Exception as e:
            print(f"Error fetching products: {e}")
            return []

    @classmethod
    def find_by_id(cls, product_id):
        query = "SELECT * FROM product WHERE id=?"
        try:
            result = cls.fetch_query(query, (product_id,))
            if result:
                return cls(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][0])
            return None
        except Exception as e:
            print(f"Error finding product: {e}")
            return None





        
    
