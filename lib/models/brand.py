from .base_model import BaseModel

class Brand(BaseModel):
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        if not name:
            raise ValueError("Brand name cannot be empty")
        cls.execute_query("INSERT INTO brand (name) VALUES (?)", (name,))
        return cls(name)

    @classmethod
    def delete(cls, brand_id):
        cls.execute_query("DELETE FROM brand WHERE id=?", (brand_id,))

    @classmethod
    def get_all(cls):
        results = cls.fetch_query("SELECT * FROM brand")
        return [cls(result[1], result[0]) for result in results]

    @classmethod
    def find_by_id(cls, brand_id):
        result = cls.fetch_query("SELECT * FROM brand WHERE id=?", (brand_id,))
        return cls(result[0][1], result[0][0]) if result else None
