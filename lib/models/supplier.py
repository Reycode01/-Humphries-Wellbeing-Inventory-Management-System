from lib.models.base_model import BaseModel

class Supplier(BaseModel):
    def __init__(self, name, contact_info, id=None):
        self.id = id
        self.name = name
        self.contact_info = contact_info
    @classmethod
    def create(cls, name, contact_info):
        if not name or not contact_info:
            raise ValueError("Supplier name and contact info cannot be empty")
        cls.execute_query("INSERT INTO supplier (name, contact_info) VALUES (?, ?)", (name, contact_info))
        return cls(name, contact_info)
    @classmethod
    def delete(cls, supplier_id):
        cls.execute_query("DELETE FROM supplier WHERE id=?", (supplier_id,))
    @classmethod
    def get_all(cls):
        results = cls.fetch_query("SELECT * FROM supplier")
        return [cls(result[1], result[2], result[0]) for result in results]
    @classmethod
    def find_by_id(cls, supplier_id):
        result = cls.fetch_query("SELECT * FROM supplier WHERE id=?", (supplier_id,))
        return cls(result[0][1], result[0][2], result[0][0]) if result else None
