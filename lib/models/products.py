from lib.models.base_model import BaseModel
class Product(BaseModel):
    def __init__(self, name, quantity, category_id, supplier_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity 
        self.category_id = category_id 
        self.supplier_id = supplier_id
    @classmethod
    def create(cls, name, quantity, category_id, supplier_id):
        if not name or quantity <0 or not category_id or not supplier_id:
            raise ValueError("Invalid product data")
        cls.execute_query (
            "INSERT INTO product (name, quantity, category_id, supplier_id) VALUES (?, ?, ?. ?)", (name, quantity, category_id, supplier_id) 
        )
        return cls(name, quantity, category_id, supplier_id)
    @classmethod
    def get_all(cls):
        results = cls. fetch_query("SELECT * FROM product")
        return [cls(result[1], result [2], result[3], result[4], result[0]) for result in results]
    @classmethod
    def find_by_id(cls, product_id):
        result = cls.fetch_query("SELECT * FROM product WHERE id=?", (product_id,))
        return cls(result[0][1], result[0][2], result[0][3], result[0][4], result[0][0]) if result else None
        
    
