from lib.models.base_model import BaseModel

class Category(BaseModel):
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        cls.execute_query("INSERT INTO category (name) VALUES (?)", (name,))
        return cls(name)

    @classmethod
    def delete(cls, category_id):
        cls.execute_query("DELETE FROM category WHERE id=?", (category_id,))

    @classmethod
    def get_all(cls):
        results = cls.fetch_query("SELECT * FROM category")
        return [cls(result['name']) for result in results]

    @classmethod
    def find_by_id(cls, category_id):
        result = cls.fetch_query("SELECT * FROM category WHERE id=?", (category_id,))
        return cls(result[0]['name']) if result else None
